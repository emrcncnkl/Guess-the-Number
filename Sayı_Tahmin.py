from random import randint
from art import logo
KOLAY_SEVİYE = 10
ZOR_SEVİYE = 5

def cevap_kontrol(tahmin, cevap, hak):
 if tahmin > cevap:
  print("Çok Yüksek.")
  return hak - 1
 elif tahmin < cevap:
  print("Çok Düşük.")
  return hak - 1
 else:
    print(f"{tahmin} sayıda tahminde buldun! Cevap {cevap} idi.")

def zorluk_seçimi():
 seviye = input("Lütfen bir zorluk seviyesi seçin. 'kolay' ya da 'zor' yazınız.")
 if seviye == "kolay":
     return KOLAY_SEVİYE
 else:
     return ZOR_SEVİYE

def oyun():
 print(logo)
 print("1 ile 100 arasında bir sayı düşünüyorum. Bul bakalım ;)")
 cevap = randint(1, 100)

 hak = zorluk_seçimi()
 tahmin = 0
 while tahmin != cevap:
  print(f"Sayıyı doğru tahmin edebilmek için {hak} kaldı.")

  tahmin = int(input("Bir tahminde bulun bakalım :)"))

  hak = cevap_kontrol(tahmin,cevap,hak)
  if hak == 0:
      print("Tahmin hakkınız doldu, Kaybettiniz. :( ")
      return 
  elif tahmin != cevap:
      print("Tekrar Tahminde bulun. ^_^")
      
game()
