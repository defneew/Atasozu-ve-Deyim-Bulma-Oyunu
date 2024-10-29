from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from gameUI import Ui_MainWindow3
import sqlite3
import re
import cv2
import torch
import numpy as np
from torchvision import transforms
# from models.yolo import Model

class GamePage(QMainWindow): 
    known_words = []
    unknown_words = []
    def __init__(self,category, length, userID,random_sentence,currentTextID,currentTextCategoryID) -> None:
        super().__init__()
        self.gameform = Ui_MainWindow3()
        self.gameform.setupUi(self)
        self.category = category
        self.length = length
        self.userID = userID
        self.random_sentence = random_sentence
        self.currentTextID = currentTextID
        self.currentTextCategoryID = currentTextCategoryID
        self.enteredLetter = []
        self.category_page = None
        self.login_page = None
        # self.model = self.load_model()
        # self.transform = transforms.Compose([
        #     transforms.ToPILImage(),
        #     transforms.Resize((640, 640)),
        #     transforms.ToTensor(),
        # ])        
        self.Game() 

    # def load_model(self):
    #     model_path = 'runs/detect/train/weights/best.pt'
    #     model = Model(cfg='models/yolov5s.yaml')  # Model yapısını tanımlayın
    #     model.load_state_dict(torch.load(model_path)['model'])  # Model ağırlıklarını yükleyin
    #     model.eval()  # Modeli değerlendirme moduna alın
    #     return model 

    # def recognize_letter_with_camera(self):
    #     cap = cv2.VideoCapture(0)
    #     while True:
    #         ret, frame = cap.read()
    #         if not ret:
    #             break
    #         cv2.imshow('Camera', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break

    #         # YOLO modeli ile tahmin yapma
    #         results = self.model(frame)
    #         predictions = results.pred[0]  # Tahmin sonuçları

    #         # Tahmin edilen harfi metin kutusuna yazma
    #         if len(predictions) > 0:
    #             predicted_letter = chr(int(predictions[0, -1].item()) + ord('A'))
    #             self.gameform.harf_line.setText(predicted_letter)

    #         break  # Tek harf tanıdıktan sonra döngüden çık

    #     cap.release()
    #     cv2.destroyAllWindows()

    def connection(self):
        self.connect = sqlite3.connect("word_game.db")    
        self.operation = self.connect.cursor()

    #seçilen metnin uzunluğundan hak sayısını hesaplama   
    def NumberOfRights(self,text):
        text_length = len(text.replace(" ", ""))
        result = str(text_length +3)
        return self.gameform.label_hak.setText(result)   
    
    #harfleri metinde gezerek indexlerini tutuyor birden fazla kez olan harfler de sorun çıkmıyor.    
    def sameLetter(self,text,letter):
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
    
    #öğedeki harf yerlerine tire atarak oyun başında görseli verir.
    def Gorsel(self,text):
        #Cümledeki fazla boşlukları tek bir boşluk haline getir
        cleaned_text = re.sub(' +', ' ', text.strip())
        resultsList = []
        for char in cleaned_text:
            if char.isalpha():
                resultsList.append('-')
            else:
                resultsList.append(char)

        results = ''.join(resultsList)   
        return  self.gameform.label_kelime.setText(results)   
                
    def Game(self):
        self.connection()
        # self.recognize_letter_with_camera()
        add = "INSERT INTO tbl_texts(personID, categoryID, adwID) VALUES (?, ?, ?)"
        self.operation.execute(add, (self.userID, self.currentTextCategoryID, self.currentTextID))
        self.connect.commit()        

        self.Gorsel(self.random_sentence)
        self.NumberOfRights(self.random_sentence)
        self.gameform.yaz_Button.clicked.connect(self.Guess)   
        self.gameform.devam_Button.clicked.connect(self.Continue) 
        self.gameform.bitir_Button.clicked.connect(self.Finish)             
    def Guess(self):        
        entered_char = self.gameform.harf_line.text().strip().upper()
        self.gameform.harf_line.clear()
        haksayısı = int(self.gameform.label_hak.text())

        if len(entered_char) != 1 or not entered_char.isalpha():
            self.gameform.label_bilgi.setText("Lütfen tek bir harf giriniz.")
            return
        if entered_char in self.enteredLetter:
            self.gameform.label_bilgi.setText("Bu harfi zaten girdiniz.")
            return 
        
        result = list(self.gameform.label_kelime.text())
        self.enteredLetter.append(entered_char)
        if entered_char in self.random_sentence:
            for i in self.sameLetter(self.random_sentence, entered_char):
                result[i] = entered_char 
            self.gameform.label_bilgi.clear()       
            self.gameform.label_kelime.setText("".join(result))        
            if "-" not in result:
                self.gameform.label_bilgi.setText("Tebrikler Kazandınız!")
                self.gameform.yaz_Button.setEnabled(False)

        else:
            haksayısı -= 1
            self.gameform.label_hak.setText(str(haksayısı))
            self.gameform.label_bilgi.setText("Yanlış harf! ") 

        if haksayısı <= 0:
            self.gameform.label_bilgi.setText("Üzgünüm, kaybettiniz.")
            self.gameform.label_kelime.setText(self.displayCorrectWord())
            self.gameform.yaz_Button.setEnabled(False)
            self.unknown_words.append(self.random_sentence)    
        self.gameform.devam_Button.clicked.connect(self.Continue) 
        self.gameform.bitir_Button.clicked.connect(self.Finish)  
    def displayCorrectWord(self):
        result = []
        for char in self.random_sentence:
            if char in self.enteredLetter:
                result.append(char)
            elif char.isalpha():
                result.append(f'<span style="color:red;">{char}</span>')
            else:
                result.append(char)
        return ''.join(result)    
    def Continue(self):
        if self.gameform.label_bilgi.text() == "Tebrikler Kazandınız!":
            if self.random_sentence not in self.known_words:
                self.known_words.append(self.random_sentence)
        else:
            if self.random_sentence not in self.unknown_words:
                self.unknown_words.append(self.random_sentence)   

        if self.category_page is None:
            from category import CategoryPage  
            self.category_page = CategoryPage(self.userID)
        self.hide()
        self.category_page.show()
    def Finish(self):
        if self.gameform.label_bilgi.text() == "Tebrikler Kazandınız!":
            self.known_words.append(self.random_sentence)
        else:
            self.unknown_words.append(self.random_sentence)    
        known_words_str = "\n".join(self.known_words)
        unknown_words_str = "\n".join(self.unknown_words)

        summary_message = (
            f"Bildiğiniz kelimeler:\n{known_words_str}\n\n"
            f"Bilmediğiniz kelimeler:\n{unknown_words_str}"
        )
        print("Oyun Özeti:\n", summary_message)
        QMessageBox.information(self, "Oyun Özeti", summary_message)
        GamePage.known_words = []  
        GamePage.unknown_words = []  
                       
        if self.category_page is None:
            from category import CategoryPage 
            self.category_page = CategoryPage(self.userID)
        
        if self.category_page is not None:
            self.category_page.close()

        if self.login_page is None:
            from login import LoginPage 
            self.login_page = LoginPage()
        
        if self.login_page is not None:
            self.login_page.close()
        
        self.close()                       

