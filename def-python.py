#pake def biasa 
def luas_persegi (s1,s2):
    luas = s1*s2
    print('luas persegi :',luas)

luas_persegi(6,6)
#ditambahi return
def keliling(s):
    kel= 4*s
    return kel
print('kelilingnya adalah: ',keliling(6))

# fungsi operasi
def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

print("hasilnya :", penjumlahan(7,6))
print("hasilnya :", pembagian(7,6))
print("hasilnya :", pengurangan(7,6))
print("hasilnya :", perkalian(7,6))