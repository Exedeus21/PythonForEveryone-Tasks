kullanici_Adi = "A"    
kullanici_Sifre = "B"
siparis_list=[]
siparis_list2=[]
sepet_list=[]
sepet_list2=[]
dict_Elec={"Laptop":1000,"Telefon":900, "Televizyon":1500,"Lamba":1000,"Buzdolabı":1000}
dict_Kıy={"Gömlek":1000,"Pantalon":900, "Tişört":1500,"Etek":1000,"Hırkan":1000}
dict_mobilya={"Koltuk":1000,"Sehpa":900, "Masa":1500,"Sandalye":1000,"Yatak":1000}
dict_ice={"Limonata":1000,"Kola":900, "Ayran":1500,"Gazoz":1000,"Şerbet":1000}
dict_Yi={"Kırmızı Et":1000,"Ekmek":900, "Elma":1500,"Çikolata":1000,"Balık":1000}
Kategor_lis=[dict_Elec,dict_Kıy,dict_mobilya,dict_ice,dict_Yi]

def ekran1(x,y):
    while True:
        print("------------")
        ka = input("Kullanıcı Adı: ")
        pw = input("Şifre: ")
        print("------------")
        if ka == x:
            if pw == y:
                print("Kullanıcı Adı ve Şifre Doğrulandı. Giriş Başarılı.")
                ekran2()
            else:
                print("Şifre hatalı. Lütfen tekrar giriniz!")
                    
        else:
            print("Kullanıcı adı hatalı. Lütfen tekrar giriniz!")

def ekran2():
    print("-----------------")
    secenek = int(input("1- Siparişlerim\n2- Sepetim\n3- Alışveriş\n4- Geri Dön\n5- ÇIKIŞ\n"))
    print("-----------------")
    if secenek==1:
        ekran2_1() #Siparişlerim
    elif secenek==2:
        ekran2_2() #Sepetim
    elif secenek==3:
        ekran2_3() #Alışveriş
    elif secenek==4:
        ekran1()
    elif secenek==5:
        exit()
    else:
        print("Yanlış Seçim Yaptınız!!")
        ekran2()
    

def ekran2_1():
    siparistop=0
    for i in siparis_list2:
        siparistop +=i
    for i in range(len(siparis_list)):
        print(siparis_list[i]," : ", siparis_list2[i])
    print("Toplam : ",siparistop)
    ekran2()


def ekran2_2():
    print("-----------------")
    secenekk=int(input("1- Sepettekileri Listele\n2- Siparişleri Onayla\n3- Geri Dön\n"))
    print("-----------------")
    if secenekk==1:
        for i in range(len(sepet_list)):
            print("{} : {}".format(sepet_list[i],sepet_list2[i]))
        ekran2_2()
        
    elif secenekk==2:
        print("Siparişleriniz onaylanmıştır.")
        for f in range(len(sepet_list)):
            siparis_list.append(sepet_list[f])
            siparis_list2.append(sepet_list2[f])
        ekran2_2()
    elif secenekk==3:
        ekran2()



def ekran2_3():
    print("--------------------------")
    secim=int(input("-1 Elektronik\n-2 Kıyafet\n-3 Mobilya\n-4 İçecek\n-5 Yiyecek\n-6 Geri Dön\n"))
    print("--------------------------")
    if secim==1:
        kat_sec(1)
    if secim==2:
        kat_sec(2)
    if secim==3:
        kat_sec(3)
    if secim==4:
        kat_sec(4)
    if secim==5:
        kat_sec(5)
    if secim==6:
        ekran2()



def kat_sec(x):
    secilendic=Kategor_lis[x-1]
    a=1
    for i in secilendic:
        print("-",a," {} : {}".format(i,secilendic[i]))
        a+=1
    print("- 6"," Geri dön")
    sec=int(input())
    if sec==1 or sec== 2 or sec==3 or sec==4 or sec==5:
        sepet_list.append(list(secilendic.keys())[sec])
        sepet_list2.append(list(secilendic.values())[sec])
        print("Sepete ekleme başarılı.")
        ekran2_3()
    elif sec==6:
        ekran2_3()
    else:
        print("Yanlış Seçim yaptınız!")
        kat_sec(x)


ekran1(kullanici_Adi,kullanici_Sifre)