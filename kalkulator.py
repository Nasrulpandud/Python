# fungsi operasi
def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

#pilihan operasi
print("Pilih Operasi Bilangan:\n1.Penjumlahan \n2.Pengurangan \n3.Perkalian \n4.Pembagian")

#meminta pilihan input dari user 
pilihan= input("Masukan pilihan kamu: 1/2/3/4  ")

num1=int(input("Masukan bilangan pertama:"))
num2=int(input("Masukan bilangan kedua : "))

if pilihan == '1':
    print("num1 + num2 =", penjumlahan(num1,num2))

elif pilihan == '2':
    print("num1 - num2 =", pengurangan(num1,num2))