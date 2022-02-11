#python

import shutil, os
from glob import glob

xmldir="/home/seismograms/SALUTE/sxml"

for path in glob("%s/*.xml" %(xmldir)):
    xml=path.split('/')[-1]
    net=xml.split('.')[0]
    sta=xml.split('.')[1]
    out=xmldir+"/"+net+"."+sta+".dataless"
    os.system(" java -jar stationxml-seed-converter-2.1.0.jar --input %s --output %s" %(path,out))
