import urllib.request
import os
dn = os.path.dirname(os.path.realpath(__file__))
print(dn)

def download(tgt,scheme,isVerbose,x_amount,y_amount):
    for x in range(0,x_amount):
        for y in range(0,y_amount):
            currentfile = tgt + scheme.replace("%X", str(x)).replace("%Y", str(y))
            hddtgt = str(x) + "_" + str(y) + ".jpg"
            print(hddtgt)
            urllib.request.urlretrieve(currentfile, hddtgt)
            if isVerbose is "V" or isVerbose is "v":
                print("Downloaded X ", x, " Y ", y)

