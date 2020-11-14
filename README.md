#ASS-Checker by Ar1st0

Es handelt sich um ein sehr einfachen und simplen Subdomain scanner der neben den suchen von Subdomains auch allgemeine Informationen zum Host gibt.
Da es sich um eine Beta-Version handelt und ich noch dran bin den code effizienter zu machen und ich gerne noch mehr Funktionen hinzufügen möchte wäre rückmeldung
der bedienlichkeit, Bugs, und generell konstruktive Kritik sehr hilfreich. Ich plane es generell anschaulicher und sichere Funktionen und umfangreichere bedienung.
Aber fürs erste ist die Main-Funktion vorhanden...einen einfachen und simplen Subdomain-scanner deren Bedienung sich fast von selbst erklärt. alles was du tun musst
ist es den beispielen zu folgen und wissen welche Domain du auswählst um nach subdomains zu suchen.

MODULE:
--------------------
Das Python-Script das in Python3 geschrieben ist benötigt folgende Module...

requests
whois
colorama 

INSTALLATION:
--------------------

Linux/Debian: sudo pip3 install requests colorama whois

BEDIENUNG:
--------------------
Führen sie das Script im Terminal aus...
>python3 ass-checker.py 

Geben sie ein Host an: (Host ist der Server auf dem die Domain zugewiesen ist, in dem Beispiel die Domain google.com) | IP-Adressen oder die Protokollbezeichnung (https://) ist nicht nötig.
>google.com

---------------------

Geben sie eine Subdomain-liste an: [default=subdomains.txt]  (Hier wird gefragt welche subdomain-liste sie verwenden möchten, sie können entweder ihre eigene verwenden oder einfach leer lassen dann benutzen sie die default-liste/standart-liste )             
>test.txt

------------------------------------
Zusatzinfo's
----------------

ASS-Checker zeigt ihnen Informationen zum Server im JSON-Format an....


{
  "domain_name": [
    "GOOGLE.COM",
    "google.com"
  ],
  "registrar": "MarkMonitor, Inc.",
  "whois_server": "whois.markmonitor.com",
  "referral_url": null,
  "updated_date": [
    "2019-09-09 15:39:04",
    "2019-09-09 08:39:04"
  ],
  "creation_date": [
    "1997-09-15 04:00:00",
    "1997-09-15 00:00:00"
  ],
  "expiration_date": [
    "2028-09-14 04:00:00",
    "2028-09-13 00:00:00"
  ],
  "name_servers": [
    "NS1.GOOGLE.COM",
    "NS2.GOOGLE.COM",
    "NS3.GOOGLE.COM",
    "NS4.GOOGLE.COM",
    "ns4.google.com",
    "ns1.google.com",
    "ns2.google.com",
    "ns3.google.com"
  ],
  "status": [
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
  ],
  "emails": [
    "abusecomplaints@markmonitor.com",
    "whoisrequest@markmonitor.com"
  ],
  "dnssec": "unsigned",
  "name": null,
  "org": "Google LLC",
  "address": null,
  "city": null,
  "state": "CA",
  "zipcode": null,
  "country": "US"
}

ausserdem speichert ASS-Checker gefundene Subdomains in die Textdatei "ass-checker.txt"
Achten sie darauf das diese Datei nach jeden erneuten ausführen des Scripts geleert wird! 

Happy Hacking und Viel Spaß. Danke das du ASS-Checker ausprobiert hast.
