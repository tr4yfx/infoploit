import os
import time
import sys
import requests
import json
from bs4 import BeautifulSoup
import colorama
import random

#main

def loading():
    for i in range(101):
        print("\n" * 100)
        os.system("clear")
        print("")
        print("CARREGANDO")
        print(str(i)+"%",colorama.Back.WHITE+colorama.Style.BRIGHT+" "*int((i/100.0)*73)+colorama.Style.RESET_ALL)
        time.sleep(1/random.randint(10,20))


def main():
   os.system("clear")
   print("""

 _________        .---            ---.
:______.-':      :  .--------------.  : 
| ______  |      | :                : |             
|:______B:|      | |      x0rx      | |             
|:______B:|      | |                | |             
|:______B:|      | |  Kernel Panic  | |             
|         |      | |                | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:

Ferramenta criada por Felipe Santos - (x0rx)

""")
loading()
main()
head = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

site = str(input("[*] Digite o site: "))
print("[*] Certificando o WordPress...")
time.sleep(2)

cms = "https://whatcms.org/?s={}".format(site)
r = requests.get(cms,headers=head)
soup = BeautifulSoup(r.text,'lxml')
soup2 = soup.find_all('a')[6].get_text()
version = soup.find_all('span')[7].get_text()

if("WordPress" in soup2):
    print("[*] CMS: WordPress")
    print("[*] Versão: {}".format(version))
    url = '/wp-json/wp/v2/users'
    r2 = requests.get(site+url,headers=head)
    if(r2.status_code==200):
        json = json.loads(r2.content.decode('utf-8'))
        for x in json[0:20]:
            print("\n[*] USER: {u}\n[*] ID: {i}".format(u=x['name'],i=x['id']))
    else:
	print("[*] Não encontramos o campo json")
	sys.exit(0)
else:
    print("[*] O site não é baseado em WordPress")
    sys.exit()
