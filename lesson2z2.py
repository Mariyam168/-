sent = input("Введите строку: ") 
words = sent.split(';')  
longest = words[0]  
for i in words:
    if len(i) > len(longest): 
        longest = i  

print("Самое длинное слово:", longest)  
