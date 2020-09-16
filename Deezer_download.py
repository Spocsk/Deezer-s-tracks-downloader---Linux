import urllib.request, json

import time
import subprocess
from subprocess import call



TOKEN = "place your Deezer's token here"
U = "https://api.deezer.com/user/2310249724/tracks?access_token="
songs = []

############# DEEZER CODE ##################""
with urllib.request.urlopen(U + TOKEN) as url:
    data = json.loads(url.read().decode())
print("Accesing to your User songs database...")
time.sleep(0.5)
print("Songs : " + str(data["total"]))
print("Getting all your songs...")

for i in range(0,int(data["total"]/25)+1):

    for a in range(0,len(data["data"])):
        #print(data["data"][a]["title"] + " - " + data["data"][a]["artist"]["name"])
        songs.append(data["data"][a]["title"] + " - " + data["data"][a]["artist"]["name"])

    try:
        next = data["next"]
        U = next
    except KeyError:
        break

    #time.sleep(1)
    #print("\n")

    with urllib.request.urlopen(U + TOKEN) as url:
        data = json.loads(url.read().decode())


for s in songs:
    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate("youtube-dl -f bestaudio \"ytsearch1: {}\"".format(s).encode('utf-8'))
    print(out.decode('utf-8'))
