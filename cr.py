#!/usr/bin/python
#######################
#CIEEE MAU RECODE YA??#
#######################
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'

# module

import os,sys,time
from time import sleep

# tampilan
os.system("clear")
sleep(1)
banner ="""\033[36;1m 
 _          _          ____                _           _               | |    ___ | | ___    / ___|_ __ ___ _   _| |__   __ _| |_             | |   / _ \| |/ _ \  | |  _| '__/ _ \ | | | '_ \ / _` | __|            | |__| (_) | | (_) | | |_| | | |  __/ |_| | | | | (_| | |_
|_____\___/|_|\___/   \____|_|  \___|\__, |_| |_|\__,_|\__|                                                 |___/

#Author : Lolo Greyhat
#Script Deface By Lolo
========================================================"""
sleep(1)
print(banner)
title = raw_input("\033[32;1m==|Title: ")
heading = raw_input("\033[32;1m==|Hacked by: ")
bgcolor = raw_input("\033[32;1m==|background color(contoh=black): ")
image = raw_input("\033[32;1m==|link gambar (tengah): ")
message = raw_input("\033[32;1m==|Pesan. gunakan kode <br> untuk text selanjutnya! : ")
textcolor = raw_input("\033[32;1m==|Warna text (contoh=green): ")
audio = raw_input("\033[32;1m==|link (MUSIK): ")
greet = raw_input("\033[32;1m==|Greetz: ")


#Open the index
fo = open("your-sc.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<body bgcolor="""

messagescript4 = bgcolor

messagescript5 = """><center><br><br><<font color="red" size="6" face="courier">"""


messagescript6 = heading

messagescript7 = """</font><br><br><img src="""

messagescript8 = image

messagescript9 = """ width=450px height=auto><br><br><font face="courier" color="""


messagescript10 = textcolor


messagescript11 = """ size="6">//----------[mesej]-----------------//<br>"""

messagescript12 = message

messagescript13 =  """<br>//----------[mesej]-----------------//<br><font face="courier new" size="5">
   <audio autoplay="autoplay" controls="controls" width="55px" height="20px"> <source src="""
   
messagescript14 = audio

messagescript15 = """></audio><br><br>-=|<marquee behavior="scroll" scrollamount="5" style="border:0px solid;" width="80%"><font color="red" face="courier">"""

messagescript16 = greet

messagescript17 ="""</font></marquee>|=-"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)
fo.write(messagescript17)

os.system("clear")
os.system("figlet Done")
print("file script bernama your-sc.html")
fo.close()
