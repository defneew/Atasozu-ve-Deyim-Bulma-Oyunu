import os 
import string
import random as rn
import re 

# csv den virgül ile kelime uzunluğu ve öğeleri ayır tek listede tüm öğeleri tut
def ReadFile(pathName, fileName):
  pai = []
  with open(pathName + fileName, encoding='utf-8') as file:
    for line in file: 
       new_line= line.rstrip()
       list = new_line.split(",")
       pai.append(list[0])
    return pai   

#seçilen metnin uzunluğundan hak sayısını hesaplama   
def NumberOfRights(text):
  text_length = len(text.replace(" ", ""))
  return text_length + 3

#harfleri metinde gezerek indexlerini tutuyor birden fazla kez olan harfler de sorun çıkmıyor.    
def sameLetter(text,letter):
    start = -1
    list = []
    while True:
        try:
            indis = text.index(letter,start+1)
        except ValueError:
            break
        else:
            list.append(indis)
            start = indis
    return list    
#kullanıcının girdiği uzunluğa öğe listesi döndürür
def textLen(pathName,fileName,length):
   list = []
   with open(pathName + fileName, encoding='utf-8') as file:
    for line in file: 
        new_line= line.rstrip()
        text, text_length = new_line.split(",")
        if int(length) == int(text_length):
           list.append(text)
    return list   
   
#öğeddeki harf yerlerine tire atarak oyun başında görseli verir.
def Gorsel(text):
    # Cümledeki fazla boşlukları tek bir boşluk haline getir
    cleaned_text = re.sub(' +', ' ', text.strip())
    resultsList = []
    for char in cleaned_text:
       if char.isalpha():
          resultsList.append('-')
       else:
          resultsList.append(char)

    results = ''.join(resultsList)    
    return results

# textList =ReadFile("C:/Users/defne/OneDrive/Masaüstü/kelime_bulma/","ads.csv")
# print(textList)
namesurname = input("Lütfen adınızı ve soyadınızı giriniz:")
mail = input("Lütfen mail adresinizi giriniz: ")

enteredLetter = []
GameContinue = "D"

while GameContinue != "K":
    enteredLetter = []

    while True:
        length = input("Kelime uzunluğu giriniz: ")
        textList = textLen("C:/Users/defne/OneDrive/Masaüstü/kelime_bulma/", "ads.csv", length)
        if textList:
            break
        else:
            print(f"{length} uzunluğunda metin yok, tekrar uzunluk giriniz.")

    text = rn.choice(textList).upper()
    up_text = text.upper()
    haksayısı = NumberOfRights(text)
    print(text)
    print("Hak Sayınız: {}".format(haksayısı))
    print(Gorsel(text))
    result = ["-" if char.isalpha() else char for char in up_text]

    while haksayısı > 0:
        char = input("Lütfen harf giriniz: ").upper()
        if len(char) != 1 or not char.isalpha():
            print("Lütfen tek bir harf giriniz.")
            continue
        if char in enteredLetter:
            print("Bu harfi zaten girdiniz.")
            continue

        enteredLetter.append(char)

        if char in text:
            for i in sameLetter(text, char):
                result[i] = char
            print("".join(result))    
            if "-" not in result:
                print("Tebrikler, kazandınız!")
                break
        else:
            haksayısı -= 1
            print("Yanlış harf! Kalan hak: {}".format(haksayısı))
            print("".join(result))  

    if haksayısı == 0:
        print("Üzgünüm, kaybettiniz. Kelime: {}".format(text))
    enteredLetter.clear()
    GameContinue = input("Devam etmek için 'D', çıkmak için 'K' giriniz: ").upper()