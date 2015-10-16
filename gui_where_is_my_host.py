#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#

# APIC-EM REST Script
# created by tsterber@cisco.com
#
# Where is my host
# get all informations to a given host
#
# Syntax:
# GET:
# https://sandboxapic.cisco.com:443/api/v0
# /host/{startIndex}/{recordsToReturn}
# /host/count    == Anzahl der Hosts
# /host/1/10     == Info von Host 1 bis 10
# /network-device/<deviceid>


# Module import
# -------------------------------------------------------------------------------------
import os               # OS commands
import tkinter as tk    # Python3 GUI
import requests		    # REST module
import json		        # json module encoder/decoder

# definitions
#
programmname = "./gui_where_is_my_host.py"
apic_url = "https://sandboxapic.cisco.com/api/v0"
deviceid =""


root = tk.Tk()
root.title('APIC-EM Where is my host            --              created by:     tsterber@cisco.com')



# Fenster definieren

def placeWindow():		# Fenster definieren
  w = 1200
  h = 600

  sw = root.winfo_screenwidth()
  sh = root.winfo_screenheight()
        
  x = (sw - w)/2
  y = (sh - h)/2
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))	  # definierte Bildschirmgroesse mittig


# benötigte Funktionen 
# -------------------------------------------------------------------------------------

def clear():				# Textfenster löschen
  mytext.delete(1.0, tk.END) 
  mytext.pack()


# display the script 
def showsript():
  print ("def show script\n")
  # script-file öffnen und ausgeben
  #
  datei = programmname
  fhandle = open(datei)
  lines = fhandle.read()
  fhandle.close()
  mytext.delete(1.0, tk.END)	# Textfenster löschen
  mytext.insert(tk.END, lines)  
  mytext.pack(side=tk.LEFT)


# count and display the number of available hosts 
def hostcount():
    url = apic_url + "/host/count"
    response = requests.get(url,verify=False)
    response_json = response.json()  # Dictionary erstellen.
    hostcount = str(response_json["response"]) # Zugriff auf gesuchtes Element
    return(hostcount)


# Get for all hosts the informations:
def gethosts():
    mytext.delete(1.0, tk.END) 			# Textfenster löschen
    mytext.insert(tk.END, "Host Count (End Devices) : "+ hostcount+"\n\n")
    mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    mytext.insert(tk.END, "\n")
    url = apic_url + "/host/1/" + hostcount
    response = requests.get(url,verify=False)
    response_json = response.json()
    n = 0
    while n < int(hostcount):
        feld = (response_json["response"][n])
        mytext.insert(tk.END, "Host IP                     : " + feld["hostIp"]+"\n")
        mytext.insert(tk.END, "Host MAC                    : " + feld["hostMac"]+"\n")
        mytext.insert(tk.END, "Host Type                   : " + feld["hostType"]+"\n")
        mytext.insert(tk.END, "Host VLAN ID                : " + feld["vlanId"]+"\n")
        mytext.insert(tk.END, "Host Status                 : " + feld["userStatus"]+"\n")
        mytext.insert(tk.END, "Connected to Device IP      : " + feld["connectedNetworkDeviceIpAddress"]+"\n")
        mytext.insert(tk.END, "             Device ID      : " + feld["connectedNetworkDeviceId"]+"\n")
        mytext.insert(tk.END, "             Interface Name : " + feld["connectedInterfaceName"]+"\n")
        mytext.insert(tk.END, "             Interface ID   : " + feld["connectedInterfaceId"]+"\n")
        mytext.insert(tk.END, "\n")
        mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        mytext.insert(tk.END, "\n")
        n += 1
    mytext.pack(side=tk.LEFT)



# search for a specific host
def search_host():
    field   = str(searchfield.get())
    if field == "Host MAC":
        field = "hostMac"
    elif field == "Host IP":
        field = "hostIp"
    else:
        print("error")
    print(field)
    wert = str(searchinput.get())
    mytext.delete(1.0, tk.END)
    mytext.insert(tk.END, "Searching for: \n\t\t" + str(searchfield.get()) + ": "+ wert + "\n\n")
    mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    mytext.insert(tk.END, "\n")
    mytext.pack(side=tk.LEFT)

    # get hosts
    url = apic_url + "/host/1/" + hostcount
    print(url)
    response = requests.get(url,verify=False)
    response_json = response.json()


    # search
    n = 0
    while n < int(hostcount):
        feld = (response_json["response"][n])
        if feld[field] == wert:
            mytext.insert(tk.END, "Host IP                     : " + feld["hostIp"]+"\n")
            mytext.insert(tk.END, "Host MAC                    : " + feld["hostMac"]+"\n")
            mytext.insert(tk.END, "Host Type                   : " + feld["hostType"]+"\n")
            mytext.insert(tk.END, "Host VLAN ID                : " + feld["vlanId"]+"\n")
            mytext.insert(tk.END, "Host Status                 : " + feld["userStatus"]+"\n")
            mytext.insert(tk.END, "Connected to Device IP        : " + feld["connectedNetworkDeviceIpAddress"]+"\n")
            # mytext.insert(tk.END, "             Device ID        : " + feld["connectedNetworkDeviceId"]+"\n")
            deviceid = feld["connectedNetworkDeviceId"]
            global deviceid
            mytext.insert(tk.END, "             Interface Name   : " + feld["connectedInterfaceName"]+"\n")
            # mytext.insert(tk.END, "             Interface ID     : " + feld["connectedInterfaceId"]+"\n")
            mytext.pack(side=tk.LEFT)
        n += 1
    get_deviceid()

def get_deviceid():
    # infos zu deviceid einlesen
    url = apic_url + "/network-device/" + deviceid
    response = requests.get(url,verify=False)
    response_json = response.json()

    # get deviceinforation
    feld = (response_json["response"])
    mytext.insert(tk.END, "             Device Name      : " + feld["hostname"]+"\n")
    mytext.insert(tk.END, "             Device Type      : " + feld["type"]+"\n")
    mytext.insert(tk.END, "             Device Platform  : " + feld["platformId"]+"\n")
    mytext.insert(tk.END, "             Device Firmware  : " + feld["softwareVersion"]+"\n")
    mytext.insert(tk.END, "             Device Lokation  : " + feld["locationName"]+"\n")
    mytext.insert(tk.END, "\n")
    mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    mytext.insert(tk.END, "\n")
    n += 1
    mytext.pack(side=tk.LEFT)






# ======================================================================================

# Frame1 , links Buttons, ...
# ------------------------------
# 

# Frame1 erstellen

f1 = tk.Frame(root, bg = "orange", width = 200, height = 600)
f1.pack(side=tk.LEFT, fill=tk.BOTH)


# Buttons

abstand = tk.Label(f1, bg = "orange", text="")
abstand.pack()

b1 = tk.Button(f1, text='show hosts',padx = 20, command=gethosts )
b1.pack()

line = tk.Label(f1, bg = "orange", text="---------------------------------")
line.pack(pady = 10, padx = 20)

# option widget
l2 = tk.Label(f1, bg = "orange", text="Choose Search-Field ? ")
l2.pack(pady = 10, padx = 20)
searchfield = tk.StringVar(f1)
searchfield.set("Host MAC")         # default value
w = tk.OptionMenu(f1, searchfield, "Host MAC", "Host IP")
w.pack()

# input widget
l2 = tk.Label(f1, bg = "orange", text="Search - Input: ")
l2.pack(pady = 10, padx = 20)
searchinput = tk.StringVar()
en = tk.Entry(f1, width=20,  textvariable=searchinput)
en.pack()
searchinput.set("00:50:56:8A:27:A3")

abstand = tk.Label(f1, bg = "orange", text="")
abstand.pack()

b3 = tk.Button(f1, text='search    ', padx=20, command=search_host)
b3.pack()

line = tk.Label(f1, bg = "orange", text="---------------------------------")
line.pack(pady = 10, padx = 20)

b4 = tk.Button(f1, text='show script    ', padx=20, command=showsript )
b4.pack()

line = tk.Label(f1, bg = "orange", text="---------------------------------")
line.pack(pady = 10, padx = 20)

abstand = tk.Label(f1, bg = "orange", text="")
abstand.pack()

ClearButton = tk.Button(f1,text="Clear", command=clear )
ClearButton.pack(side = tk.LEFT, pady = 20, padx = 20)

ExitButton = tk.Button(f1, text="Exit",command=root.destroy)
ExitButton.pack(side = tk.LEFT, pady = 20, padx = 20)


# Frame2 , rechts Textausgabe
# ------------------------------
# 
f2 = tk.Frame(root, bg = "white", width = 400, height = 600)
mytext = tk.Text(f2,height=400, width=600)
f2.pack()
mytext.insert(tk.END, "Programm wurde gestartet           ")
mytext.pack(side=tk.LEFT)



# ======================================================================================
# Main
# first it is checked, if Sandbox is available,
# if ok GUI is starting
#

urlcheck = "sandboxapic.cisco.com"
if os.system("ping -c 1 " + urlcheck) == 0:
    # print ("URL ist erreichbar")
    # hostcount holen und gui starten
    hostcount = hostcount()
    frame = placeWindow()
    root.call('wm', 'attributes', '.', '-topmost', '1')   # set window to front
    root.mainloop()
else:
    print ("Cisco Sandbox is not available. SORRY, please try it later.")

