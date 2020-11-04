import requests
from requests.auth import HTTPBasicAuth


def authenticate_access(url):
    givenUrl = url
    response = requests.get(givenUrl, auth=HTTPBasicAuth('', ''))
    html_string = response.text
    if response.status_code != 200:
        if response.status_code == 404:     # handling 404 error
            html_string = "Page cannot be found"
            print("Page cannot be found")
    return html_string

