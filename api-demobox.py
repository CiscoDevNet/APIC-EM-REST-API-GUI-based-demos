#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Version: Python 3
#
# created by tsterber@cisco.com
#

'''
This can be used as the master gui for all gui based programs in this folder.
All gui based programs can also run on their own.
'''



import os			# ausführen von System Befehlen ermöglichen
import webbrowser		# Webbrowser Optionen ermöglichen
import tkinter as tk		# Tkinter laden

root = tk.Tk()
root.wm_title("   Python -  APIC-EM API's Toolbox  		--			created by:   tsterber@cisco.com")



#
#	functions  , menue-functions
#
# ------------------------------------------
def hello():
  print ("hallo")           # just for tests

def hosts():
  os.system('./gui_get_hosts.py')

def devices():
  os.system('./gui_get_devices.py')

def device_config():
  os.system('./gui_get_device_config.py')

def my_device():
  os.system('./gui_where_is_my_host.py')


def hilfe():
  new = 2 			# neuen Tab verwenden, sofern möglich
  url = "http://www.google.de"
  webbrowser.open(url,new=new)

def devnet_web():
  new = 2
  url = "https://developer.cisco.com"
  webbrowser.open(url,new=new)

def devnet_web_apicem():
  new = 2
  url = "https://developer.cisco.com/site/apic-em/documents/api-reference/"
  webbrowser.open(url,new=new)

def apic_em_sanbox():
  new = 2
  url = "https://sandboxapic.cisco.com"
  webbrowser.open(url,new=new)



# -------------------------------------------------

def placeWindow():
  w = 1024
  h = 768

  sw = root.winfo_screenwidth()
  sh = root.winfo_screenheight()
        
  x = (sw - w)/2
  y = (sh - h)/2
#  root.geometry('%dx%d+%d+%d' % (w, h, x, y))	  # definierte Bildschirmgroesse mittig
  root.geometry('%dx%d+%d+%d' % (sw, sh, 0, 0))   # Vollbild erstellen



#
# Window with Menues
#

menubar = tk.Menu(root)

#
# Text ,  LOGO
# -----------------------------------------------------------------------
#  Logo and Text 
#
text1 = """       

"""
w1 = tk.Label(root,justify=tk.LEFT,
           padx = 10, 
           text=text1).pack(side="top")

logo = tk.PhotoImage(file="./ciscodevnet.gif")
w2 = tk.Label(root, image=logo).pack(side="top")

w3 = tk.Label(root,justify=tk.LEFT,
           padx = 10, 
           text=text1).pack(side="top")

text3 = """Cisco German API Community - tsterber@cisco.com"""
w3 = tk.Label(root,justify=tk.LEFT,
           padx = 10, 
           text=text3).pack(side="top")

w4 = tk.Label(root,justify=tk.LEFT,
           padx = 10, 
           text=text1).pack(side="top")

text3 = """This APIC-EM-API Toolbox is for demonstration only. 
You must not use any of this scripts in your live Network"""
w5 = tk.Label(root, 
           justify=tk.CENTER,
           padx = 10, 
           text=text3).pack(side="top")

# -------------------------------------------------------------------------

# APIC-EM-API Menue 
#

apimenu = tk.Menu(menubar, tearoff = 0)		
menubar.add_cascade(label="APIC-EM & REST   ", menu=apimenu)

apic_read = tk.Menu(apimenu, tearoff = 0)
apimenu.add_cascade(label="Tools: APIC-EM READ", menu=apic_read)
apic_read.add_command(label="01: Show or Search Hosts", command=hosts)
apic_read.add_command(label="02: Show or Search Devices", command = devices)
apic_read.add_command(label="03: Show Device Config", command = device_config)
apic_read.add_command(label="04: Where is my Host", command = my_device)

'''
apic_write = tk.Menu(apimenu, tearoff = 0)
apimenu.add_cascade(label="Tools: APIC-EM WRITE", menu=apic_write)
apic_write.add_command(label="01: Set new Device", command=hello)
apic_write.add_command(label="02: ", command = hello)
'''

apimenu.add_separator()
apimenu.add_command(label="EXIT", command=quit)


# HELP Menu
#
helpmenu = tk.Menu(menubar, tearoff = 0)	
menubar.add_cascade(label="    HELP",  menu=helpmenu)
helpmenu.add_command(label="Cisco Dev-Net", command=devnet_web)
helpmenu.add_command(label="Cisco APIC-EM Sandbox", command=apic_em_sanbox)



# Windows Menues ausgeben
#
root.config(menu=menubar)


frame = placeWindow()
root.call('wm', 'attributes', '.', '-topmost', '1')   # set window to front
root.mainloop()




