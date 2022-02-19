class Text:
    def __init__(self,text):
        self.text=text
    def lite_text(self):
        print(f"Цитируемый текст: {self.text}")
    def caps_text(self):
        print(self.text.upper())
text=(input("Введите текст --> "))
tx1=Text(text)
tx1.lite_text()
tx1.caps_text()
        
