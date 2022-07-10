#!/usr/bin/env python3
#!/usr/bin/python3
#coding: utf-8
#Author: Ar1st0

import sys, os, time, threading, requests, random
from colorama import Fore, Style

r = random.randint(2,5)
pt = "."

def end():
    clear()
    banner()
    hostabfrage()

def banner():
    print (Style.BRIGHT+Fore.YELLOW)
    print ('''

          /$$$$$$   /$$$$$$   /$$$$$$           /$$$$$$  /$$                           /$$                          
         /$$__  $$ /$$__  $$ /$$__  $$         /$$__  $$| $$                          | $$                          
        | $$  \ $$| $$  \__/| $$  \__/        | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
        | $$$$$$$$|  $$$$$$ |  $$$$$$  /$$$$$$| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
        | $$__  $$ \____  $$ \____  $$|______/| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
        | $$  | $$ /$$  \ $$ /$$  \ $$        | $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
        | $$  | $$|  $$$$$$/|  $$$$$$/        |  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
        |__/  |__/ \______/  \______/          \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/  V2.1.1
        ___________________________________________________________________________________________________________
                                            Ar1st0’s-Simple-Subdomain-Checker 
                                                            |                                                   ''') 
    print (Style.DIM+Fore.GREEN+ "                                                         {v1.0}                       ")
    print (Style.RESET_ALL)
banner()
def clear():
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
def hostabfrage():
    global thost
    print (Style.RESET_ALL)
    print ("""       __________________________________________________________________________)
                    |      -DOMAIN-      |   |     -IPv4-     |      |         -IPv6-          |
             Example:     google.com     |NOT| 216.58.205.238 |OR NOT| 2a00:1450:4001:81e::200e\n""")
    thost = str(input(Fore.WHITE + "Geben sie eine Domain an:\n>"))
    if thost == "":
       print (Fore.RED+"\nGeben sie eine Domain an.\n")
       hostabfrage()
    if "127.0.0.1" in thost or "localhost" in thost:
        print (Fore.RED + "\n[-] Lokaler Host nicht möglich.")
        end()
    elif "http://" in thost or "https://" in thost:
        print (Fore.RED + "\n[-] Protokollbezeichnung nicht notwendig.") 
        time.sleep(r)
        clear()
        hostabfrage()
    print (Fore.YELLOW + "\n[+] Host wird überprüft...")
    try:
          requests.get("http://"+thost)
    except requests.ConnectionError:
          print (Fore.RED + "\n[-] "+thost+(" existiert nicht und/oder ist offline.\n"))
          print (Fore.WHITE + "ja = [y] | nein = [n] ")
          again = str(input(Fore.WHITE+"[?] Möchtest du ein neuen Host angeben?:\n>"))
          if again == "":
              print (Style.DIM+Fore.WHITE + "\n[-_-] Offensichtlich nicht...")
              sys.exit(2)
          elif again == "y":
              banner(), hostabfrage()
          elif again == "n":
              print (Style.BRIGHT+Fore.WHITE + "\n[*] Danke dass du "+Fore.BLUE+"A"+Fore.YELLOW+"S"+Fore.RED+"S"+Style.BRIGHT+Fore.WHITE+"-Checker benutzt hast.")
              print (Style.RESET_ALL)
              sys.exit(2)
          else:
              print (Fore.RED + "\n[-] Ja oder Nein, nach etwas anderem habe ich nicht gefragt...")
              sys.exit(2)
    else:
         print (Fore.GREEN + "\n[*] "+thost+(" existiert und ist online."))
         print (Style.RESET_ALL)
hostabfrage()

sublist = input (Fore.WHITE + "Geben sie eine Subdomain-liste an: [default=subdomains.txt] \n>")
if sublist == "":
    slist = open("subdomains.txt", 'r')
    print (Fore.GREEN + "\n[*] Eingabe wurde auf >>default<< (subdomains.txt) gesetzt...")
    content = slist.read()
    slist = content.splitlines()
else:
    try:
        with open(sublist, 'r') as file:
            print (Fore.GREEN + "\n[*] Die "+sublist+"-Datei wurde gefunden.")
    except IOError as e:
        print (Fore.RED + "\n[!] Die angegebene Datei wurde nicht gefunden.")
        print (Fore.YELLOW + "\nOS-Error_code: ")
        print (e)
        print (Style.RESET_ALL)
        sys.exit()
    clist = open(sublist, 'r+')
    content = clist.read()
    slist = content.splitlines()

txt = "txt"
rname = thost+pt+"txt"
sdlist = open(rname, 'w') # Datei wird mit ensprechender Domainname angelegt und in Variable gespeichert
print (Fore.YELLOW + "\n[INFO] Whois-Informationen zu: " +thost)
print (Style.RESET_ALL)
wd = os.system(f"whois {thost}")
print (wd)
print (Fore.YELLOW + "\n[INFO] Scan nach Subdomains startet jetzt...")
print (Fore.WHITE + "+------------------------------------------------+")
time.sleep(r)
print (Style.RESET_ALL)
http = str("http://")

def process():
    load_str = "Subdomains werden ermittelt... "
    ls_len = len(load_str)
    animation = "|/-\|"
    anicount = 0
    counttime = 0
    i = 0
    while (counttime != 11):
        time.sleep(0.1)
        load_str_list = list(load_str)
        res =''
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r"+res+animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len # i+=1 % ls_len
        counttime = counttime + 1

for sline in slist:
    time.sleep(0.25)
    process()
    subhost = f"{sline}.{thost}"
    try:
        requests.get(http+sline+pt+thost)
    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print (Fore.RED+"[+] Programm wird beendet. Bisherige gefundene Subdomains finden sie in "+rname+". Bye!")
        sys.exit(3)
    else:
        print (Fore.GREEN + (f" [*] Subdomain gefunden...")+Style.BRIGHT+Fore.YELLOW+("[")+subhost+("]"))
        print (Style.RESET_ALL)
        sdlist.write(f"[+] {subhost}\n")
print (Fore.WHITE + "+------------------------------------------------+")
print (Fore.YELLOW + "\n[INFO] Liste wurde abgearbeitet.\n")
sdlist.close()

if os.path.getsize(rname) > 0:
    print (Fore.YELLOW + f"[INFO] Die gefundenen Subdomains sind in '"+rname+"' gespeichert.")
    print (Style.BRIGHT+Fore.WHITE + "\n[*] Danke dass du "+Fore.BLUE+"A"+Fore.YELLOW+"S"+Fore.RED+"S"+Style.BRIGHT+Fore.WHITE+"-Checker benutzt hast.")
    sys.exit(1)
else:
    print (Fore.RED + "[-] Es wurden keine Subdomains gefunden.")
    try:
        pass # os.remove(thost+pt+"txt")
    except OSError as error:
        print (Fore.RED + error)
        print (Style.RESET_ALL)
    pass
sys.exit()
# TODO:

# Automatisches erkennen ob Webserver TLS/SSL ((https) Zertifikat überprüfen) für den Kommunikationsaufbau verwendet
# Namensspezifische Dateien anlegen für die Resultate, falls leer (keine gefunden) angelegte Datei löschen, andernfalls in die datei schreiben
