import requests, argparse, os, platform, urllib
from bs4 import BeautifulSoup
import pyfiglet, termcolor

dev_info = """
VERSION = 1.1.1
DEVELOPED BY = NEEL THAKOR
"""

if(platform.system() == 'Windows'):
    os.system('cls')
if(platform.system() == 'Linux'):
    os.system('clear')

banner_text = pyfiglet.figlet_format("CVE\nSCRAPER", font='starwars', width=500)
print(termcolor.colored(banner_text, 'cyan', attrs=['dark', 'bold']))
print(termcolor.colored(dev_info, 'green', attrs=['dark', 'bold']))

args = argparse.ArgumentParser(usage = "CVE_screp.py -n/--number CVE_number !OR! -q/--query KEYWORD")
muex = args.add_mutually_exclusive_group(required = True)
muex.add_argument("-n", "--number")
muex.add_argument("-q", "--query", type=str, nargs='+')
parser = args.parse_args()
number = parser.number
query = parser.query

def create_url_query(query):
    url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="

    for i in range(len(query)):
        if (i < len(query) - 1):
            url = url + urllib.parse.quote(query[i]) + '+'
        else:
            url = url + urllib.parse.quote(query[i]) 
    return url

def create_url_number(number):
    url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + urllib.parse.quote(number)
    return url

def get_links(url):
    try:
        r = requests.get(url)
    except:
        print('='*100 + '\n' + "[-] Can't connet to the server. Please check your connection and try again..." + '\n' + "OR" + '\n' + "[-] Enter proper CVE..." + '\n' + '='*100)
        exit()

    soup = BeautifulSoup(r.content, 'html.parser')

    text1 = """
    [+] Finding links for CVE...
    """
    print(termcolor.colored(text1, 'magenta', attrs=['bold', 'dark']))
        
    flag = 1
    temp = 0
    for divs in soup.find_all('div', id='TableWithRules'):
        print("="*100 + '\n')
        for info in divs.find_all('td'):
            print(info.text + '\n')
            if(flag % 2 == 0):
                i = 0
                for anchors in divs.find_all('a'):
                    if(temp == i):
                        print('-'*100 + '\n' + "[+] LINK : " + anchors['href'] + '\n' + "="*100)
                    i+=1
                temp+=1
                flag += 1
            else:
                flag += 1   

if (number):
    url = create_url_number(number)
    get_links(url)
else:
    url = create_url_query(query)
    get_links(url)
