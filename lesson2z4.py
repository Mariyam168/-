sent=input("Введите строку : ")
find=input("Введите слово для поиска : ")
if find in sent:
    print(f"Слово '{find}' найдено в строке")
else:
    print(f"Слово '{find}' нет в строке!")