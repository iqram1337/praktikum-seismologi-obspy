import obspy

cat = obspy.read("D:/Coding/Python/Obspy/COP.BHZ.DK.2009.050")

meow = obspy.read("D:/Coding/Python/Obspy/COP.BHE.DK.2009.050")
meow += obspy.read("D:/Coding/Python/Obspy/COP.BHN.DK.2009.050")
meow += obspy.read("D:/Coding/Python/Obspy/COP.BHZ.DK.2009.050")

print(cat)

#cat.plot()

"""dt = cat[0].stats.starttime
cat.plot(color="red", number_of_ticks=7,
         tick_rotation=5, tick_format='%I:%M:%P',
         starttime=dt + 60*60, endtime=dt + 60*60 + 120)"""

meow.plot()