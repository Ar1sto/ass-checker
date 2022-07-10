#ASS-Checker by Ar1st0

![ASS-Checker - Version 1.0 Menü](https://github.com/Ar1sto/ass-checker/blob/main/assicon.ico)

Es handelt sich um ein sehr einfachen und simplen Subdomain scanner der neben dem suchen von Subdomains auch Whois-Informationen (falls gegeben) angibt.
Dies ist die erste richtige Version (Insgesamt die Version 2.1.1). Ich möchte gerne noch mehr Funktionen hinzufügen, daher wäre Rückmeldung zu
der bedienlichkeit, Bugs, und generell konstruktive Kritik sehr hilfreich.
Aber für's erste ist die Main-Funktion vorhanden...einen einfachen und simplen Subdomain-scanner deren Bedienung sich fast von selbst erklärt. Alles was du tun musst
ist es den beispielen zu folgen und wissen welche Domain du auswählst um nach Subdomains zu suchen.

MODULES:
--------------------
Das Python-Script das in Python3 geschrieben ist benötigt folgende Module...

requests
colorama 

INSTALLATION:
--------------------

Linux/Debian: sudo pip3 install requests colorama whois
(Developed for Linux-based OS's and tested on a Debian-based system)

BEDIENUNG:
--------------------
Führen sie das Script im Terminal aus...
>python3 ass-checker.py 

Geben sie eine Subdomain-liste an: [default=subdomains.txt]  (Hier wird gefragt welche subdomain-liste sie verwenden möchten, sie können entweder ihre eigene verwenden oder einfach leer lassen dann benutzen sie die default-liste/standart-liste )             
>subdomains.txt

------------------------------------
Zusatzinfo's
----------------

ASS-Checker zeigt ihnen Whois-Informationen zur Domain an....

Ausserdem speichert ASS-Checker gefundene Subdomains in die Textdatei die angelegt wird mit dem Namen der Domain.

Happy Hacking und Viel Spaß. Danke das du ASS-Checker ausprobiert hast.
