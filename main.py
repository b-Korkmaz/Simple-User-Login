
sw_id="Burhan"
sw_pass="1234"
kullanici_hakki=3

while (1):

    print("************************\n"
          "KULLANICI GİRİŞİ PROGRAMI\n"
          "*************************\n"
          "1.İşlem Giriş\n"
          "2.İşlem Çıkış (Çıkmak İçin Çıkış Yazınız...)\n")



    islem=input("Yapmak İstediğiniz İşlem :")

    if(islem=="Giriş"):

        girilen_id=input("Kullanıcı Adı :")
        girilen_pass=input("Şifre :")
        if (kullanici_hakki == 0):
            print("Giriş Hakkınız Doldu. Programdan Çıkılıyor....")
            break

        if(girilen_id !=sw_id and girilen_pass != sw_pass):
            print("Kullanıcı Adı ve Şifre Hatalı")
            kullanici_hakki -=1
            print("Kalan Hakkınız {} ".format(kullanici_hakki))
        elif(girilen_id==sw_id and girilen_pass !=sw_pass):
            print("Şifre Hatalı")
            kullanici_hakki -= 1
            print("Kalan Hakkınız {} ".format(kullanici_hakki))
        elif(girilen_id !=sw_id and girilen_pass==sw_pass):
            print("Kullanıcı Adı Hatalı")
            kullanici_hakki -= 1
            print("Kalan Hakkınız {} ".format(kullanici_hakki))
        elif(girilen_id==sw_id and girilen_pass==sw_pass):
            print("Kullanıcı Adı ve Parola Doğru\n"
                  "Hoşgeldiniz...\n")
            kullanici_hakki = 3
            print("Kalan Kullanıcı Hakkı Güncellendi {}".format(kullanici_hakki))
            break

    elif(islem=="Çıkış"):
         print("Sistemden Çıkılıyor....")
         break
    else:
        print("Yanlış Tuşlama Yaptınız...")