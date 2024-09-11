print("Общество в начале XXI века")
print("Введите возраст: ")
a=int(input())
if(a>=0 and a<7):
    print("Вам в детский сад")
elif (a>=7 and a<18):
    print("Вам в школу")
elif (a>=18 and a<25):
    print("Вам в профессиональное учебное заведение")
elif(a>=25 and a<60):
    print("Вам на работу")
elif(a>=60 and a<120):
    print("Вам предоставляется выбор")
else:
    for i in range(5):
        print("ОШИБКА!!!!!")    