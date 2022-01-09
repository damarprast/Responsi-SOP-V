# Damar Prasetyo N
# 5200411104
# SISTEM OPERASI PRAKTEK V

print("__________RESPONSI 1 __________")
ram=int(input("Kapasitas total RAM: "))
petabit = int(input("Kapasitas petabit: "))
SO = int(input("kapasitas yang digunakan oleh sistem operasi: "))
program1=int(input("Kapasitas RAM yang digunakan oleh program 1: "))
program2=int(input("Kapasitas RAM yang digunakan oleh program 2: "))
7
kapasitas_petabit= ram/petabit
gb_mb= kapasitas_petabit*1024
ram_terpakai = ram - SO
programRAM1= ram_terpakai - program1
programRAM2= programRAM1 - program2 
ram_sisa= ram - programRAM2
blok_terpakai= (program1+program2)/ram*petabit



print("__________HASIL_________")
print("jumlah total RAM: ",ram)
print("jumlah total petabit: ",petabit)
print("kapaasitas petabit adalah: ",gb_mb)
print("total RAM yang terpakai: ",ram_sisa)
print("total RAM yang tidak terpakai: ",programRAM2)
print("jumalh blok terpakai: ",blok_terpakai)
print("jumlah program bernilai 1: ",blok_terpakai)
print("jumlah program bernilai 2: ",petabit - blok_terpakai)