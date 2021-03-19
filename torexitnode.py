import os
import socks
import requests
import pyfiglet

os.system(chr(27)+"[36m")
os.system("clear")


banner=pyfiglet.figlet_format("TorExitNode",font="standard")
print(banner)

print("          Author : Rahat Khan Tusar(rkt)")
print("          Github : https://github.com/r3k4t")
print
session=requests.session()
session.proxies={}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
r=session.get("https://ipinfo.io/ip")
r2=session.get("https://ipinfo.io/hostname")
r3=session.get("https://ipinfo.io/city")
r4=session.get("https://ipinfo.io/region")
r5=session.get("https://ipinfo.io/country")
r6=session.get("https://ipinfo.io/loc")
r7=session.get("https://ipinfo.io/org")
r8=session.get("https://ipinfo.io/postal")
r9=session.get("https://ipinfo.io/timezone")
r10=session.get("https://ipinfo.io/loc")
print("Tor Exit Node Ip   :  " +r.content)
print
print("Hostname           :  " +r2.content)
print("City               :  " +r3.content)
print("Region             :  " +r4.content)
print("Country            :  " +r5.content)
print("Latitude&Longitude :  " +r6.content)
print("Organization       :  " +r7.content)
print("Postal             :  " +r8.content)
print("Timezone           :  " +r9.content)
print("Google Map         :  https://www.google.com/maps/place/" +r10.content)





