print("Menampilkan bilangan terbesar dari 3 input")
nama = input("Masukkan Nama 	: ")
nim = input("Masukkan NIM 	: ")
kelas = input("Masukkan Kelas 	: ")
a = int(input("Masukkan Bilangan A : "))
b = int(input("Masukkan Bilangan B : "))
c = int(input("Masukkan Bilangan C : "))

angka = [a, b, c]
hasil = max(angka)
if a > b and a > c:
	huruf = "A"
elif b > a and b > c:
	huruf = "B"
elif c > a and c > b:
	huruf = "C"
else :
	huruf = "A,B,C"

print("\nNama 		: ",nama)
print("NIM 		: ",nim)
print("Kelas 		: ", kelas)
print("Yang terbesar adalah Bilangan = ",huruf)
print("Dengan nilai : ",hasil)
