#python

import shutil, os
from glob import glob

datadir="/home/seismograms/SALUTE/sxml"

for path in glob("%s/*.dataless" %(datadir)):
    os.system("/home/nancy/rdseedv5.3.1/rdseed.rh6.linux_64 -f %s -R" %(path))

for path in glob("RESP*"):
    resp=path.split('/')[-1]
    out=datadir+"/"+resp+".txt"
    shutil.move(path,out)
