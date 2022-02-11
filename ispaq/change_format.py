#python
#IRIS format TW.TR06..HHZ.2021.330
#our data format CC03.TW..BHE.2021.290

import shutil, os 
from glob import glob

dirc="/home/guest/SALUTE/DailyMSEED"
outdirc="/home/seismograms/SALUTE"

for path in glob("%s/*/*" %dirc):
    mseed=path.split('/')[-1]
    net=mseed.split('.')[1]
    sta=mseed.split('.')[0]
    loc=mseed.split('.')[2]
    cha=mseed.split('.')[3]
    year=mseed.split('.')[4]
    day=mseed.split('.')[5]
    out=outdirc+"/"+sta+"/"+"/"+net+"."+sta+"."+loc+"."+cha+"."+year+"."+day
    if not os.path.isdir("%s/%s" %(outdirc,sta)):
        os.mkdir("%s/%s" %(outdirc,sta))
    shutil.copy(path,out)
