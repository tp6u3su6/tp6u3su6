#python

import shutil, os
from glob import glob

mseeddir="/home/seismograms/SALUTE/Dailymseed"
xmldir="/home/seismograms/SALUTE/sxml"

for stadir in glob("%s/*" %mseeddir):
    sta=stadir.split('/')[-1]
    for path in glob("%s/*" %stadir):
        mseed=path.split('/')[-1]
        net=mseed.split('.')[0]
        sta=mseed.split('.')[1]
        chan=mseed.split('.')[3]
        year=mseed.split('.')[4]
        day=mseed.split('.')[5]

        if os.path.isfile("%s/RESP.%s.%s..%s.txt" %(xmldir,net,sta,chan)):
            os.system("./run_ispaq.py -M psd_corrected,pdf -S %s.%s..%s --starttime %s-%s --dataselect_url %s/%s --station_url %s/%s.%s.xml --resp_dir %s --pdf_type plot" 
                %(net,sta,chan,year,day,mseeddir,sta,xmldir,net,sta,xmldir))
