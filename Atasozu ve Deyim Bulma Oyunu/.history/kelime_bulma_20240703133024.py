import os 
import string
import random as random
import re 

# csv den virgül ile kelime uzunluğu ve öğeleri ayır tek listede tüm öğeleri tut
def ReadFile(pathName, fileName):
  pai = []
  with open(pathName + fileName) as file:
    for line in file: 
       new_line= line.rstrip()
       list = new_line.split(",")
       pai.append(list[0])
  return pai   
  
# ReadFile("C:/Users/defne/OneDrive/Masaüstü/kelime_bulma/","ads.csv")       

#seçilen metnin uzunluğundan hak sayısını hesaplama   
def NumberOfRights(text):
  text_length = len(text.replace(" ", ""))
  return text_length + 3
    
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



namesurname = input("Lütfen adınızı ve soyadınızı giriniz:")
mail = input("Lütfen mail adresinizi giriniz: ")
enteredLetter = []
GameContinue = "D"
skor = 0

while GameContinue != "K":
   