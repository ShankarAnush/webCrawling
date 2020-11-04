from bs4 import BeautifulSoup
from html_parser import MyHTMLParser
from session_authenticate import authenticate_access
import csv
import os
import io
from pandas import read_csv     # to add the headers into csv file


def fetch_links(html_string, counter, library, append_number):
    soup = BeautifulSoup(html_string, "html.parser")
    # first check if the html string contains frame tag.
    # If so, the string has to be forwarded to a different function
    append_number += 5
    base_url = 'http://doc2/FIISDEVTECPUB/techpubs/browser/'
    parser = MyHTMLParser(base_url)
    parser.feed(html_string)
    # fetch the dictionary create after html parsing
    # dictionary_of_links = dict()
    dictionary_of_links = parser.send_links_and_data()
    if not bool(dictionary_of_links):
        pass
    else:
        print(dictionary_of_links)
        file = os.path.join(library + '/' + library + str(append_number) + '.csv')
        print(file)
        if not os.path.isfile(file):
            with io.open(file, "w", newline="", encoding="utf-8") as f:
                write_into_csv = csv.writer(f)
                write_into_csv.writerow(['Product Doc Suites', 'Link'])
                f.close()
                # even if the file exists overwrite it with empty character
        with open(file, 'w', newline="", encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Product Doc Suites', 'Link'])
            for x, y in dictionary_of_links.items():
                append_number += 2
                if x is None:
                    pass
                else:
                    temp = x.split()
                    temp2 = str(temp[-1]).lower().replace('_fram', '-1')
                    temp[-1] = temp2
                    print(temp)
                    writer.writerow([y, ''.join(temp)])     # converting list type to string using join
            csv_file.close()

        # you have a dictionary consisting of product name and links from the html table
        # crawl these sub pages to get all the nested links
        # thus authenticate again and collect the html string
        for key, value in dictionary_of_links.items():
            if key is None or not key:
                pass  # checking if the key is empty or not
            elif key == 'mailto:www.com':
                pass
            elif counter >= 2:
                pass
            else:
                second_html_string = authenticate_access(key)
                if second_html_string == "Page cannot be found":
                    print("The Url gave 404 Error")
                else:
                    counter += 1
                    append_number += 3  # randomly increasing the number
                    fetch_links(second_html_string, counter, library, append_number)
                    append_number += 2  # randomly increasing the number
                    counter -= 1  # so that it wont eliminate the rest of the keys after it
        counter -= 1
