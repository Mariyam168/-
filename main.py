print("Введите число от 1 до 9")
a=int(input())
if(a>=1 and a<=3):
    print("Введите строку:")
    s=input()
    print("Введитеь число повторов строки:")
    n=int(input())
    for i in range (n):
        print(s)    
elif(a>=4 and a<6):
    print("Введите степень :")
    m=int(input())
    print(a**m)
elif(a>=6 and a<=9):
    for i in range (9):
        l=a+i
        print(l)    
else:
    print("Ошибка!!!!!")    