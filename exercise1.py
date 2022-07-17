"""Hitung waktu yang telah berlalu semenjak ulang tahun anda"""
from obspy.core import UTCDateTime

x = UTCDateTime(2001, 7, 29)
y = UTCDateTime(2022, 2, 16)

z = y-x
print(z/3600)
