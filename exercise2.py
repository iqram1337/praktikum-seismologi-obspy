"""
Buat 20 UTCDateTime objects dimulai semenjak ulang tahun anda pukul 09:00 dengan spasi 12 jam.
"""
import obspy as kanye

tahun = kanye.core.UTCDateTime(2021, 7, 29, 9, 0, 0)

spasi12jam = 12*3600

tb = []
for i in range(20):
    temp = tahun + (spasi12jam*i)
    
    tb.append(temp)

for i in range(len(tb)):
    print(tb[i])