# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import requests
import re
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Search HTML tags' values on a URL")

parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='The url to be searched')
parser.add_argument('-t', '--tag', type=str, metavar='', required=True, help='The tag to be searched')
parser.add_argument('-a', '--attr', type=str, metavar='', required=False, help="The tag's attribute to be searched")
parser.add_argument('-r', '--regex', type=str, metavar='', required=False, help='The tag to be searched')

args = parser.parse_args()

def show_all(url, tag, attr, regex_str):
    if url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        url = "http://" + url

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    if attr is not None:
        s = soup.select(tag + '[' + attr + ']')
        ll = []
        for elm in s:
            ll.append(str(elm))

        if regex_str is not None:
            user_str = re.compile(regex_str)
            for tag_ in ll:
                for match in re.findall(user_str, tag_):
                    print("[Regex Match] ", tag_)
        else:
            print("[*] Tags found: ")
            for tag_ in ll:
                print(tag_)
    else:
        s = soup.select(tag)
        ll = []
        for elm in s:
            ll.append(str(elm))
        print("[*] Tags found: ")
        for tag_ in ll:
            print(tag_)


if __name__ == '__main__':
    show_all(args.url, args.tag, args.attr, args.regex)
