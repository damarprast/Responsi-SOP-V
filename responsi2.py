# Damar Prasetyo N
# 5200411104
# SISTEM OPERASI PRAKTEK V

print("___________Responsi 2_____________")
size=[]
jumlah_program = int(input("masukkan jumlah program: "))
jatah_waktu=int(input("Jumlah Quantum time: "))

for nilai in range(jumlah_program):
    nama_program= (input("masukan nama program {}: ".format(nilai+1)))
    lama_program=int(input("lama program {}: ".format(nilai+1)))
    rumus= lama_program-jatah_waktu
    size.append(rumus)
    list.sort(size)
    print("Hasil eksekusi dari metode RR: ", size)
