import obspy

time = obspy.core.UTCDateTime("2012-08-14T02:45:10")
st = obspy.read("D:/Coding/Python/Obspy/exampleData/*mseed")

for i in range(len(st)):
    print(st[i].stats.station)
