#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#

#
# APIC-EM REST Script
# - - - - - - - - - - -
#
# created by tsterber@cisco.com
#
# 1- Get_Devices
# 2- Search for specific devices
#
# Syntax:
# GET:
# /network-device/{startIndex}/{recordsToReturn}
# /network-device/count    == Anzahl der Device
# /network-device/1/10     == Info von Device 1 bis 10
#


# Module import
# -------------------------------------------------------------------------------------
import os               # OS commands
import tkinter as tk    # Python3 GUI
import requests		    # REST module
import json		        # json module encoder/decoder

# definitions
#
programmname = "./gui_get_devices.py"
apic_url = "https://sandboxapic.cisco.com/api/v0"



root = tk.Tk()
root.title('APIC-EM Network-Devices            --              created by:     tsterber@cisco.com')



# window definition

def placeWindow():
  w = 1200
  h = 600

  sw = root.winfo_screenwidth()
  sh = root.winfo_screenheight()

  x = (sw - w)/2
  y = (sh - h)/2
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))	  # definition of screen


# functions
# -------------------------------------------------------------------------------------

def clear():				# clear window
  mytext.delete(1.0, tk.END)
  mytext.pack()


# display the script
def showsript():
  print ("def show script\n")
  #
  datei = programmname
  fhandle = open(datei)
  lines = fhandle.read()
  fhandle.close()
  mytext.delete(1.0, tk.END)	# clear window
  mytext.insert(tk.END, lines)
  mytext.pack(side=tk.LEFT)


# count and display the number of available hosts
def devicecount():
    url = apic_url + "/network-device/count"
    response = requests.get(url,verify=False)
    response_json = response.json()  # create dictionary
    devicecount = str(response_json["response"]) # get element
    return(devicecount)


# Get for all hosts and their informations:
def getdevices():
    mytext.delete(1.0, tk.END) 			# clear window
    mytext.insert(tk.END, "Network Device Count : "+ devicecount+"\n\n")
    mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    mytext.insert(tk.END, "\n")
    url = apic_url + "/network-device/1/" + devicecount
    response = requests.get(url,verify=False)
    response_json = response.json()
    n = 0
    while n < int(devicecount):
        feld = (response_json["response"][n])
        mytext.insert(tk.END, "Device Host Name        : " + feld["hostname"]+"\n")
        mytext.insert(tk.END, "Device Platform Id      : " + feld["platformId"]+"\n")
        mytext.insert(tk.END, "Device Serial Number    : " + feld["serialNumber"]+"\n")
        mytext.insert(tk.END, "Device Software Version : " + feld["softwareVersion"]+"\n")
        mytext.insert(tk.END, "Device Memory Size      : " + feld["memorySize"]+"\n")
        mytext.insert(tk.END, "Device Mgmt IP          : " + feld["managementIpAddress"]+"\n")
        mytext.insert(tk.END, "Device MAC Address      : " + feld["macAddress"]+"\n")
        mytext.insert(tk.END, "Device Up Time          : " + feld["upTime"]+"\n")
        mytext.insert(tk.END, "\n")
        mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        mytext.insert(tk.END, "\n")
        n += 1
    mytext.pack(side=tk.LEFT)


# search for a specific device based on the MAC, IP, Hostname,..
def search_device():
    field   = str(searchfield.get())
    if field == "Serial Number":
        field = "serialNumber"
    elif field == "Mgmt IP":
        field = "managementIpAddress"
    elif field == "MAC Address":
        field = "macAddress"
    elif field == "Host Name":
        field = "hostname"
    elif field == "PlatformId":
        field = "platformId"
    else:
        print("error")
    print(field)
    wert = str(searchinput.get())
    mytext.delete(1.0, tk.END)
    mytext.insert(tk.END, "Searching for: \n\t\t" + str(searchfield.get()) + ": "+ wert + "\n\n")
    mytext.insert(tk.END, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    mytext.insert(tk.END, "\n")
    mytext.pack(side=tk.LEFT)

    url = apic_url + "/network-device/1/" + devicecount
    response = requests.get(url,verify=False)
    response_json = response.json()


    # search for device and print his informations
    n = 0
    while n < int(devicecount):
        feld = (response_json["response"][n])
        if feld[field] == wert:
            feld = (response_json["response"][n])
            mytext.insert(tk.END, "Device Host Name        : " + feld["hostname"]+"\n")
            mytext.insert(tk.END, "Device Platform Id      : " + feld["platformId"]+"\n")
            mytext.insert(tk.END, "Device Serial Number    : " + feld["serialNumber"]+"\n")
            mytext.insert(tk.END, "Device Software Version : " + feld["softwareVersion"]+"\n")
            mytext.insert(tk.END, "Device Memory Size      : " + feld["memorySize"]+"\n")
            mytext.insert(tk.END, "Device Mgmt IP          : " + feld["managementIpAddress"]+"\n")
            mytext.insert(tk.END, "Device MAC Address      : " + feld["macAddress"]+"\n")
            mytext.insert(tk.END, "Device Up Time          : " + feld["upTime"]+"\n")
            mytext.insert(tk.END, "\n")
            mytext.pack(side=tk.LEFT)
        n += 1






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

b1 = tk.Button(f1, text='show devices',padx = 20, command=getdevices)
b1.pack()

line = tk.Label(f1, bg = "orange", text="---------------------------------")
line.pack(pady = 10, padx = 20)

# option widget
l2 = tk.Label(f1, bg = "orange", text="Choose Search-Field ? ")
l2.pack(pady = 10, padx = 20)
searchfield = tk.StringVar(f1)
searchfield.set("PlatformId")         # default value
w = tk.OptionMenu(f1, searchfield, "Serial Number", "Mgmt IP", "MAC Address", "Host Name", "PlatformId")
w.pack()


# input widget
l2 = tk.Label(f1, bg = "orange", text="Search - Input: ")
l2.pack(pady = 10, padx = 20)
searchinput = tk.StringVar()
en = tk.Entry(f1, width=20,  textvariable=searchinput)
en.pack()
searchinput.set("ASR1002")

abstand = tk.Label(f1, bg = "orange", text="")
abstand.pack()

b3 = tk.Button(f1, text='search    ', padx=20, command=search_device)
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


# Frame2 , text on the right
# ------------------------------
#
f2 = tk.Frame(root, bg = "white", width = 400, height = 600)
mytext = tk.Text(f2,height=400, width=600)
f2.pack()
mytext.insert(tk.END, "Program was started           ")
mytext.pack(side=tk.LEFT)



# ======================================================================================
# Main
# first it is checked, if Sandbox is available,
# if ok GUI is starting
#
if __name__ == "__main__":
    urlcheck = "sandboxapic.cisco.com"
    if os.system("ping -c 1 " + urlcheck) == 0:
        # print ("URL ist erreichbar")
        # hostcount holen und gui starten
        devicecount = devicecount()
        frame = placeWindow()
        root.call('wm', 'attributes', '.', '-topmost', '1')   # set window to front
        root.mainloop()
    else:
        print ("Cisco Sandbox is not available. SORRY, please try it later.")

