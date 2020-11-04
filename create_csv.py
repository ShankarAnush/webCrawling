import requests
from requests.auth import HTTPBasicAuth
from session_authenticate import authenticate_access
import general_functions
from html_parser import MyHTMLParser
from bs4 import BeautifulSoup
from parseLinksFromHTMLFrame import fetch_links
import csv

# from parse_html_tags import MyHTMLParser

# Dictionary of technical libraries
dictTechnicalLibraries = {
     "Internal Reference": "http://doc2/FIISDEVTECPUB/techpubs/browser/DS_Lib.htm",
     "Electronic Security": "http://doc2/FIISDEVTECPUB/techpubs/browser/ESD_Lib.htm",
     "Physical Security": "http://doc2/FIISDEVTECPUB/techpubs/browser/PSD_Lib.htm",
     "Self-Service Systems": "http://doc2/FIISDEVTECPUB/techpubs/browser/SSS_Lib.htm"
}

print(dictTechnicalLibraries)
counter = 0
append_number = 12345
for x, y in dictTechnicalLibraries.items():
    # create a directory in the name of the library
    general_functions.create_project_dir(x)
    # create a csv file for each of the libraries
    # general_functions.create_data_files(x) //no need to create the files. They are created explicitly in the next func
    # get the html content of each of the libraries
    html_string = authenticate_access(y)
    # print(html_string)
    if html_string == "Page cannot be found":
        print("The Url gave 404 Error")
    else:
        counter += 1
        fetch_links(html_string, counter, x, append_number)
        counter -= 1
