Sikert - Sikert is an subdomain enumeration tool which collect subdomain from different sources.

Sources include :

1 - Alien Vault

2 - Anubis

3 - Binary edge

4 - Certspotter

5 - Chaos

6 - Crtsh

7 - ReconDev

8 - Security Trails

9 - Shodan

10 - Sonar

11 - Spyse

12 - Sublist3r

13 - Threatcrowd

14 - Threatminer

15 - VirusTotal

Installation :

        pip install sikert

Usage :

       from sikert import <source name>

       <source name>.enum(domain name,  output filename)

Example :

       from sikert import alienvault

       alienvault.enum('domain name', 'result.txt')

       binaryedge('domain name', 'api key', 'result.txt')

Troubleshooting :

       Cannot run source - This means that no api key was given.
               
       If you run sikert against a domain but can't see sources along with subdomain name that means it is not into that particular source
      