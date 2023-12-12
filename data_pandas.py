# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:36:41 2023

@author: Huawei
"""

import pandas as pd
    
Data = {
        'Model' : ['High Hell', 'Wedges', 'Flat','Sneaker', 'Boots', 'Oxford', 'Derby', 'Loafer', 'Fantofel'],
        'Retail' : [2000, 1500, 800, 900, 1300, 2200, 2200, 1000, 1100],
        'Jakarta' : [150, 96, 150, 130, 50, 200, 180, 125, 80],
        'Surabaya' : [90, 100, 105, 140, 35, 150, 150, 100, 75],
        'Bali' : [155, 100, 100, 125, 30, 150, 100, 125, 90],
        'Makassar' : [130, 130, 120, 110, 30, 150, 160, 160, 100]
}

df = pd.DataFrame(Data)
print(df)
print()

df['T Penjualan'] = df["Jakarta"] + df["Surabaya"] + df["Bali"] + df["Makassar"]
print(df)
print()

df['TRP Makassar'] = df["Retail"] * df["Makassar"]
print(df)
print()

df = df.drop(labels=[8])
print(df)
print()

df.to_csv('penjuala_sepatu.csv')
