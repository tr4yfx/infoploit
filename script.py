import time
import os,sys
import requests
import re
from bs4 import BeautifulSoup
import vulners


#// pip3 install vulners
#// pip3 install bs4


def main():
	os.system("clear")
	print("""
 _____          __        ______  _         _  _   
|_   _|        / _|       | ___ \| |       (_)| |  
  | |   _ __  | |_   ___  | |_/ /| |  ___   _ | |_ 
  | |  | '_ \ |  _| / _ \ |  __/ | | / _ \ | || __|
 _| |_ | | | || |  | (_) || |    | || (_) || || |_ 
 \___/ |_| |_||_|   \___/ \_|    |_| \___/ |_| \__|
                                                   
Criado Por Tr4yfx

EXEMPLOS

==> python3 infoploit.py cve "cve-000-000"
==> python3 infoploit.py exp "Vulnerabilidade" limite_de_buscas, EX: 5,10,20.                                                
""")

main()

def cve(cve):
	base = "https://www.cvedetails.com/cve/"+cve
	r = requests.get(base)
	code = r.content.decode("utf-8")
	soup = BeautifulSoup(code,'lxml')
	for x in soup:
		time.sleep(1)
		print("\n[*] CVE: {}".format(cve))
		print("\n[*] Vulnerability: {}\n".format(soup.find_all("span")[21].get_text()))
		string = soup.find_all("div",{"class":"cvssbox"})
		for div in string:
		    print("[*] CVS Score: {}".format(div.text))
		    break
		break

def vuln(exp,var):
    api = vulners.Vulners()
    busca = api.search(exp,limit=var)
    print("[#] Searching...[{}]\n".format(exp))
    print("[#] Limite...[{}]".format(var))
    for x in busca:
    	time.sleep(1)
    	print("\n\n[*] Title: {}\n".format(x['title']))
    	print("[*] ID: {}\n".format(x['id']))
    	print("[*] Href: {}\n".format(x['href']))


    
if(sys.argv[1]=="cve"):
	bs = str(sys.argv[2])
	cve(bs)
if(sys.argv[1]=="exp"):
	ex = str(sys.argv[2])
	quant = int(sys.argv[3])
	vuln(ex,quant)
