import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from unicodedata import numeric



# URL adresa k zip archívu
url = "https://archive.ics.uci.edu/static/public/519/heart+failure+clinical+records.zip"

data_hf = pd.read_csv(url, compression='zip')

print(data_hf.head())
print(data_hf.info())
print(data_hf.describe())

print("Uloha 1")
print("     A) Obsahuje dataset chýbajúce hodnoty (NA) ?")
print("         pocet NA hodnot", data_hf.isnull().sum())
print("     B) Aký typ majú vybrané premenné v datasete ? (numerické/kategorické) (Ak by ste si pri niektorých premenných neboli istí, zdôvodnite svoju odpoveď.)")
print("        1)Age -> numericke, "
      "        2)Aanaemia -> kategoricke,   "
      "        3)high_blood_pressure -> kategoricke ,   " 
      "        4)serum_sodium -> numericke, "
      "        3)death_event -> kategoricke,  " )
print("     C) Obsahuje dataset duplicitné záznamy?")
print("             Pocet duplikatov v datach", data_hf.duplicated().sum())


print("Uloha 2")
pocet = data_hf['sex'].value_counts()

print("     A) Koľko záznamov mužov a žien obsahuje dataset?")
print("         Dataset obsahuje muzov :", pocet[1], " | ",
                                "Zien : ", pocet[0])
print("     B) Koľko mužov a žien je nefajčiarov ? (0 = nefajčiar, 1 = fajčiar)")

nefajciarMuz = data_hf[(data_hf['sex'] == 1) & (data_hf['smoking'] == 0)]
nefajciarZena = data_hf[(data_hf['sex'] == 0) & (data_hf['smoking'] == 0)]
print("         nefajciari muzi: ", len(nefajciarMuz))
print("         nefajciari zeny: ", len(nefajciarZena))


print("Uloha 3")

minAge = data_hf['age'].min()
maxAge = data_hf['age'].max()
priemerAge = data_hf['age'].mean()
modeAge = data_hf['age'].mode()

print("     A) Age -> min: ", minAge)
print("     B) Age -> max: ", maxAge)
print("     C) Age -> mean: ", priemerAge)
print("     D) Age -> mode: ", modeAge)

print("Uloha 4")

print("     A) V akom veku je riziko zlyhania srdca najväčšie?")
print("         v 60 rokoch")
print("     B) Koľko záznamov (približne) je v datasete v tejto vekovej kategórii?")
print("         priblizne 23")
print("     C) Nie su ziadne NA na stranke bol kod ktorym som najskor pracoval a tam bolo ukazane ze nie su ziande NA tiez")


corr_matrix = data_hf.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()
print("Uloha 5")
print("     A) Ktoré atribúty majú medzi sebou najväčšiu zápornú koreláciu? (uveďte prvé dve dvojice)")
print("         Death-Event - Time | DeathEvent - Ejection Fruction")

print("     B) Ktoré atribúty majú medzi sebou najväčšiu kladnú koreláciu? (uveďte prvú dvojicu)")
print("         sex - smoking | ")

data_hf['risk'] = data_hf.apply(lambda row: 'High' if row['age'] > 50 and row['serum_creatinine'] > 1.2 else 'Low', axis=1)

# Visualize high risk by age
high_risk = data_hf[data_hf['risk'] == 'High']
plt.hist(high_risk['age'], bins='auto')
plt.title('High Risk by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


