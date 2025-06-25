# Menghitung jumlah penumpang laki-laki dan perempuan, serta berapa persentasenya dari total penumpang.
import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
totalPenumpang = (data['sex']).count()
pria = (data['sex'] == 'male').sum()
wanita = (data['sex'] == 'female').sum()
presenPria = (pria/totalPenumpang)*100
presenWanita = (wanita/totalPenumpang)*100
print("jumlah pria :", pria, "jumlah wanita :", wanita)
print("Presntase pria :", presenPria, "presentase wanita :", presenWanita)

