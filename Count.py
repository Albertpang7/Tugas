import sys


Contoh = ""
huruf = angka = simbol = 0

for line in sys.stdin:
    Contoh = line
    for i in range(len(Contoh)):
        if((Contoh[i] >= 'a' and Contoh[i] <= 'z') or (Contoh[i] >= 'A' and Contoh[i] <= 'Z')): 
            huruf = huruf + 1 
        elif(Contoh[i] >= '0' and Contoh[i] <= '9'):
            angka = angka + 1
        else:
            simbol = simbol + 1

sys.stdout.write("Total angka: " + str(angka))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(huruf))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(simbol))
sys.stdout.write('\n')
