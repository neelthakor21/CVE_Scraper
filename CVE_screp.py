import requests, argparse, os, platform, urllib
from bs4 import BeautifulSoup

if(platform.system() == 'Windows'):
    os.system('cls')
if(platform.system() == 'Linux'):
    os.system('clear')

args = argparse.ArgumentParser(usage = "CVE_screp.py -n/--number CVE_number -q/--query KEYWORD")
args.add_argument("-n", "--number")
args.add_argument("-q", "--query", type=str, nargs='+')
parser = args.parse_args()
number = parser.number
query = parser.query

def create_url(query):
    global url
    url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="

    for i in range(len(query)):
        if (i < len(query) - 1):
            url = url + urllib.parse.quote(query[i]) + '+'
        else:
            url = url + urllib.parse.quote(query[i]) 

def get_links():
    create_url(query)
    try:
        r = requests.get(url)
    except:
        print('='*100 + '\n' + "[-] Can't connet to the server. Please check your connection and try again..." + '\n' + '='*100)
        exit()

    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)
    
get_links()
    
