import json

with open('mahasiswa.json','r') as datafile:
    data = json.load(datafile)

a = dict()
n = int(input('Masukkan jumlah mahasiswa baru: '))

for jumlah in range(0,n):
    nama  = input('Masukan Nama anda:') 
    countm = []
    hobi_a = []
    m = int(input('Masukkan Jumlah hobi anda: '))
    for j in range(0,m):
        hobi = input(f'Masukkan hobi ke-{j+1} : ')
        hobi_a.append(hobi)
    prestasi = input('Masukan prestasi anda :')
    print('===Data Berhasil ditambahkan===')
    print()

a[nama] =[{'BioData:': {'Hobi': hobi,'Prestasi':prestasi}}]
data.update(a)

with open('mahasiswa.json','w') as datafile:
     json.lump(datafile)

    