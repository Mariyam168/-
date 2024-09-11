sent = input("Введите строку: ") 
znak=input("Введите знак :")
words = sent.split(znak)  
short = words[0] 
for i in words:
    if len(i) < len(short): 
        short = i  

print("Самое короткое слово:", short)  
