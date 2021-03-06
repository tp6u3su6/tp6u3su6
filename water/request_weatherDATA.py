import pandas as pd
import requests, os
from datetime import datetime
import time
import shutil

shutil.copy('chosen_WeatherStation.csv','WeatherStation.csv')
csv=pd.read_csv('WeatherStation.csv',index_col=False)
rstacode=csv['station code']
URL=csv['URL']
startyear=2012

for ii in range(len(rstacode)):
    if not os.path.isdir(rstacode[ii]):
        os.mkdir(rstacode[ii])
    if not os.path.isfile('%s/%s_202112.csv' %(rstacode[ii],rstacode[ii])):
        print('Download data of %s' %rstacode[ii])
        for year in range(startyear,2022):
            for mon in range(1,13):
                url=URL[ii]+str(year)+'-'+str(mon).zfill(2)
                res=requests.get(url)
                df=pd.read_html(res.text)[1]
                csvname='%s/%s_%s%s.csv'%(rstacode[ii],rstacode[ii],year,str(mon).zfill(2))
                print(csvname)
                df.to_csv(csvname,encoding='utf_8_sig',index=False)
            time.sleep(5)
        time.sleep(15)
