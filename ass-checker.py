#!/usr/bin/env python
#coding: utf-8
#Author: Ar1st0
import sys
import os
import time
import requests
import random
import whois
from colorama import Fore, Style

r = random.randint(2,5)
open ("ass-checker.txt", "w").close()

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
        |__/  |__/ \______/  \______/          \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/  V.2
        ___________________________________________________________________________________________________________
                                            Ar1st0’s-Simple-Subdomain-Checker 
                                                            |                                                   ''') 
    print (Style.DIM+Fore.GREEN+ "                                                     {BETA-Version}                       ")
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
    print ("         __________________________________________________________________________")
    print ("        |      -DOMAIN-      |   |     -IPv4-     |      |         -IPv6-          |") 
    print (" Example:     google.com     |NOT| 216.58.205.238 |OR NOT| 2a00:1450:4001:81e::200e\n")
    thost = str(input(Fore.WHITE + "Geben sie ein Host an:\n>"))
    if thost == "":
       print (Fore.RED+"\nGeben sie ein Host an.\n")
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
            print (Fore.GREEN + "\n[*] Die angegebene Datei wurde gefunden.")
    except IOError as e:
        print (Fore.RED + "\n[!] Die angegebene Datei wurde nicht gefunden.")
        print (Fore.YELLOW + "\nOS-Error_code: ")
        print (e)
        print (Style.RESET_ALL)
        sys.exit()
    clist = open(sublist, 'r')
    content = clist.read()
    slist = content.splitlines()
sdlist = open("ass-checker.txt", 'w') 
print (Fore.YELLOW + "\n[INFO] Server-Informationen zu: " +("http://")+thost)
print (Style.RESET_ALL)
wd = whois.whois("http://"+thost) 
print (wd)
print (Fore.YELLOW + "\n[INFO] Scan nach Subdomains startet jetzt...")
print (Fore.WHITE + "+------------------------------------------------+")
time.sleep(r)
print (Style.RESET_ALL)
http = str("http://")
pt = str(".")
for sline in slist:
    time.sleep(r)
    subhost = f"{sline}.{thost}"
    try:
        requests.get(http+sline+pt+thost)
    except requests.ConnectionError:
        pass
    else:
        print (Fore.GREEN + (f"[*] Subdomain gefunden...")+Style.BRIGHT+Fore.YELLOW+("[")+subhost+("]"))
        print (Style.RESET_ALL)
        sdlist.write("\n[+] " + (subhost))
print (Fore.WHITE + "+------------------------------------------------+")
print (Fore.WHITE + "\n[+] Liste wurde abgearbeitet.\n")
print (Fore.YELLOW + f"[INFO] Die gefundenen Subdomains sind in 'ass-checker.txt' gespeichert.")
print (Style.BRIGHT+Fore.WHITE + "\n[*] Danke dass du "+Fore.BLUE+"A"+Fore.YELLOW+"S"+Fore.RED+"S"+Style.BRIGHT+Fore.WHITE+"-Checker benutzt hast.")
sdlist.close()
sys.exit()
