import pandas as pd
import requests, os
from datetime import datetime
from obspy.geodetics.base import gps2dist_azimuth
import matplotlib.pyplot as plt
import time
import shutil

#read weather station information 找距地震測站15公里以內的氣象測站
## 氣象局沒有資料: 宜蘭古魯 花蓮豐里

rainsta_exc=pd.read_excel('rainfall_station.xlsx')
renddate=pd.to_datetime(rainsta_exc['撤站日期']).dt.strftime("%Y%m%d").fillna(99999999)
rainsta_exc=rainsta_exc[renddate.astype(int)>=20170101].reset_index()
rstacode=rainsta_exc['站號']
rstaname=rainsta_exc['站名']
rlon=rainsta_exc['經度']
rlat=rainsta_exc['緯度']
rcon=rainsta_exc['城市']
rstartdate=pd.to_datetime(rainsta_exc['資料起始日期']).dt.strftime("%Y%m%d")
renddate=pd.to_datetime(rainsta_exc['撤站日期']).dt.strftime("%Y%m%d").fillna(99999999)


#read seismic station information
seissta_exc=pd.read_csv('/home/nancy/GMT/stn_info_hualien',header=None,sep=',')
sstacode=seissta_exc[0]
slon=seissta_exc[2]
slat=seissta_exc[1]

chosen_stacode=[]
chosen_staname=[]
chosen_lon=[]
chosen_lat=[]
chosen_con=[]
for i in range(len(sstacode)):
    print(sstacode[i])
    for j in range(len(rstacode)):
        dis=gps2dist_azimuth(slat[i],slon[i],rlat[j],rlon[j])[0]
        if dis/1000 <= 15:
            chosen_stacode.append(rstacode[j])
            chosen_staname.append(rstaname[j])
            chosen_lon.append(rlon[j])
            chosen_lat.append(rlat[j])
            chosen_con.append(rcon[j])
chosen=pd.DataFrame({'station code':chosen_stacode,'Country':chosen_con,'station name':chosen_staname,
                     'longitude':chosen_lon,'latitude':chosen_lat})
chosen=chosen.drop_duplicates().reset_index()
chosen=chosen.drop('index',axis=1)
chosen=chosen.sort_values(['Country'])
chosen.to_csv('chosen_WeatherStation.csv',encoding='utf_8_sig',index=False)
## After, NEED get URL by self.
