RehberDict = {}

def KeyBulma(dicto,değer):
    for k,v in dicto.items():
        if v==değer:
            return k
        elif k==değer:
            return k


while True:
    islem = input("Yapmak istediğiniz işlem nedir?\n-1 Rehbere Kişi Ekle\n-2 Rehberden Kişi Silme\n-3 İsim & Numara Güncelleme\n-4 Rehberi Görüntüle\n-5 Çıkış\n")
    sayac1=0
    if islem == "1":
        isim = input("İsmi giriniz.")
        numara = input("Numarayı Giriniz.")
        for i in RehberDict:
            if isim == i:
                sayac1+=1
        if sayac1==0:
            RehberDict[isim] = numara
        else:
            print("Bu isimde bir kayıt bulunmaktadır. Lütfen başka isimle giriş yapınız")
    
    elif islem == "2":
        sil_num = input("Silinecek isim veya numarayı giriniz.")
        Keyler=KeyBulma(RehberDict,sil_num)
        try:
            RehberDict.pop(Keyler)
        except:
            print("Girdiğiniz isim veya numara rehberde bulunmamaktadır.")

    
    elif islem == "3":
        degis_isim = input("Numarasını değiştirmek istediğiniz kişiyi giriniz.")
        degis_num = input("Yeni numarayı giriniz.")
        if degis_isim in RehberDict:
            RehberDict.pop(degis_isim)
            RehberDict[degis_isim] = degis_num
            print("Numara Güncellenmiştir.")
        else:
            print("Girdiğiniz isim rehberde bulunmamaktadır.")
    
    
    elif islem == "4":
        for i in RehberDict:
            print(i,":", RehberDict[i])

    elif islem=="5":
        exit()

    else:
        print("Yanlış giriş yaptınız.")
        exit()
    