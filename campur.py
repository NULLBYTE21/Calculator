#!/bin/usr/python
#-*- coding utf-8 -*-
# jangan di copy paste bos,kalo ntar kena copyright baru tau rasa lu
#
# jangan pernah merusak atau mencoba menghancurkan karya orang lain
#
# hargai lah karya orang lain,sehingga karyamu akan di hargai juga oleh orang lain
#
#Tunggu Update Versi Selanjutnya
#
#.   TITLE.  :OPERASI HITUNG BERJALAN
#    AUTHOR. :REKHA GUSTIAWAN
#.   CODE BY :NULL BYTE && REKHA GUSTIAWAN
#.   EMAIL   :REKHAGUSTIAWAN25@GMAIL.COM
#    PROGRAM :OPERASI HITUNG/CALCULATOR VERSI PYTHON
#.   VERSION :ALGORITMA PYTHON 1.0.0
# 

import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
lskt = "\033[0;33m"
a = "\033[30;1m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0/100)
os.system("clear")
sleep (2)
print(m+"")
slowprints("|----------------------------------------------------------------------------|")
os.system("figlet -f slant 'selamat datang' | lolcat")
print(m+"")
slowprints("|----------------------------------------------------------------------------||")
sleep (1)
os.system("date | lolcat")
print(gt+"")
slowprints("|--------------------------------------------------------------|")
slowprints("|                           CREDIT                             |")
slowprints("|--------------------------------------------------------------|")
slowprints("|     [!] TITLE      : OPERASI HITUNG BERJALAN                 |")
slowprints("|     [!] AUTHOR     : REKHA GUSTIAWAN.                        |")
slowprints("|     [!] CODE BY    : NULL BYTE && REKHA GUSTIAWAN.           |")
slowprints("|     [!] EMAIL      : REKHAGUSTIAWAN25@GMAIL.COM              |")
slowprints("|     [!] THANK'S TO : ALLAH SWT-NULL BYTE-ABENK21-MY CREW DAN |")
slowprints("|                    : UNTUK SEMUANYA YANG TELAH SUPPORT SAYA. |")
slowprints("|     [!] PROGRAM    : OPERASI HITUNG/CALCULATOR VERSI PYTHON. |")
slowprints("|     [!] VERSION    : ALGORITMA PYTHON 1.0.0                  |")
slowprints("|--------------------------------------------------------------|")
input('\nPRESS ENTER TO CONTINUE...!!!')
sleep (2)
os.system("clear")
os.system("date | lolcat")
print(M+"")
slowprints("|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|")
os.system("figlet -f slant 'CALCULATOR' | lolcat")
print(M+"")
slowprints("|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|")
slowprints("|                                                         VERSION:1.0.0|")
slowprints("|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|")
input('\nPRESS ENTER TO CONTINUE...!!!')
sleep (2)
os.system("clear")
os.system("date | lolcat")
os.system("figlet -f slant 'calculator' | lolcat")
print(gt+"")
slowprints("|-----------------------------------------------------|")
slowprints("|[!]MEMASUKI METODE PENJUMLAHAN DAN SELAMAT MENGHITUNG|")
slowprints("|-----------------------------------------------------|")
slowprints("|             [+] METODE PENJUMLAHAN...!!!            |")
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
sleep (2)
slowprints("|-----------------------------------------------------|")
a = int(input("|MASUKAN ANGKA PERTAMA OPERASI HITUNG PENJUMLAHAN|--->|="))
slowprints("|-----------------------------------------------------|")
b = int(input("|MASUKAN ANGKA KEDUA OPERASI HITUNG PENJUMLAHAN--|--->|="))
slowprints("|-----------------------------------------------------|")
input('\nPRESS ENTER TO CONTINUE...!!!')
sleep (2)
os.system("clear")
os.system("date | lolcat")
os.system("figlet -f slant 'calculator' | lolcat")
print(gt+"")
slowprints("|-----------------------------------------------------|")
slowprints("|[!]MEMASUKI METODE PENGURANGAN DAN SELAMAT MENGHITUNG|")
slowprints("|-----------------------------------------------------|")
slowprints("|             [-] METODE PENGURANGAN...!!!            |")
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
sleep (2)
slowprints("|-----------------------------------------------------|")
g = int(input("|MASUKAN ANGKA PERTAMA OPERASI HITUNG PENGURANGAN|--->|="))
slowprints("|-----------------------------------------------------|")
h = int(input("|MASUKAN ANGKA KEDUA OPERASI HITUNG PENGURANGAN--|--->|="))
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
input('\nPRESS ENTER TO CONTINUE...!!!')
sleep (2)
os.system("clear")
os.system("date | lolcat")
os.system("figlet -f slant 'calculator' | lolcat")
print(gt+"")
slowprints("|-----------------------------------------------------|")
slowprints("|[!] MEMASUKI METODE PERKALIAN DAN SELAMAT MENGHITUNG!|")
slowprints("|-----------------------------------------------------|")
slowprints("|             [*] METODE PERKALIAN...!!!              |")
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
sleep (2)
slowprints("|-----------------------------------------------------|")
c = int(input("|MASUKAN ANGKA PERTAMA OPERASI HITUNG PERKALIAN-|---->|="))
slowprints("|-----------------------------------------------------|")
d = int(input("|MASUKAN ANGKA KEDUA OPERASI HITUNG PERKALIAN---|---->|="))
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
input('\nPRESS ENTER TO CONTINUE...!!!')
sleep (2)
os.system("clear")
os.system("date | lolcat")
os.system("figlet -f slant 'calculator' | lolcat")
print(gt+"")
slowprints("|-----------------------------------------------------|")
slowprints("|[!] MEMASUKI METODE PEMBAGIAN DAN SELAMAT MENGHITUNG!|")
slowprints("|-----------------------------------------------------|")
slowprints("|             [/:] METODE PEMBAGIAN...!!!             |")
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
sleep (1)
slowprints("|-----------------------------------------------------|")
e = int(input("|MASUKAN ANGKA PERTAMA OPERASI HITUNG PEMBAGIAN--|--->|="))
slowprints("|-----------------------------------------------------|")
f = int(input("|MASUKAN ANGKA KEDUA OPERASI HITUNG PEMBAGIAN----|--->|="))
slowprints("|-----------------------------------------------------|")
slowprints("|_____________________________________________________|")
sleep (1)
input('\nPRESS ENTER TO INPUT...!!!')
os.system("clear")
slowprints("|------------------------------------|")
a = a
b = b
g = g
h = h
c = c
d = d
e = e
f = f
print("|NILAI ANGKA PERTAMA PENJUMLAHAN-|-->|=="+ str(a))
print("|NILAI ANGKA KEDUA PENJUMLAHAN---|-->|=="+ str(b))
slowprints("|------------------------------------|")
print("|NILAI ANGKA PERTAMA PENGURANGAN-|-->|=="+ str(g))
print("|NILAI ANGKA KEDUA PENGURANGAN---|-->|=="+ str(h))
slowprints("|------------------------------------|")
print("|NILAI ANGKA PERTAMA PERKALIAN---|-->|=="+ str(c))
print("|NILAI ANGKA KEDUA PERKALIAN-----|-->|=="+ str(d))
slowprints("|------------------------------------|")
print("|NILAI ANGKA PERTAMA PEMBAGIAN---|-->|=="+ str(e))
print("|NILAI ANGKA KEDUA PEMBAGIAN-----|-->|=="+ str(f))
slowprints("|------------------------------------|")
slowprints("|____________________________________|")
sleep (2)
os.system("date | lolcat")
print(gt+"")
slowprints("|----------------------------|")
s = a + b
g = g - h
h = c * d
k = e / f
r = a / b,g / h,c / d,e * f
print("|HASIL AKHIR PENJUMLAHAN|--->|=="+ str(s))
slowprints("|----------------------------|")
print("|HASIL AKHIR PENGURANGAN|--->|=="+ str(g))
slowprints("|----------------------------|")
print("|HASIL AKHIR PERKALIAN  |--->|=="+ str(h))
slowprints("|----------------------------|")
print("|HASIL AKHIR PEMBAGIAN  |--->|=="+ str(k))
slowprints("|----------------------------|")
slowprints("|----------------------------|")
print("|<-------RATA-RATA----->|--->|=="+ str(r))
slowprints("|____________________________|")
sleep (2)
input('\nPRESS ENTER TO EXITING...!!!')
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/100)
os.system("clear")
print(gt+"")
slowprints("|--------------------|")
slowprints("|       PESAN        |")
slowprints("|--------------------|----------------------------------------|")
slowprints("|TERIMA KASIH TELAH MENGGUNAKAN OPERASI HITUNG/CALCULATOR SAYA|")
slowprints("|SEKIAN DARI SAYA DAN SAMPAI JUMPA LAIN WAKTU...!!!           |")
slowprints("|JANGAN LUPA SENYUM HARI INI :) BYE...!                       |")
slowprints("|SEMOGA BERMANFAAT YAA...!:)                                  |")
slowprints("|                                          #REKHA GUSTIAWAN.  |")
slowprints("|-------------------------------------------------------------|")
os.system("clear")
os.system("date | lolcat")
os.system("figlet -f slant 'thanks for watching' | lolcat")
