import urllib.request


def download(tgt, scheme, isVerbose, x_amount, y_amount):
    for x in range(0, x_amount):
        for y in range(0, y_amount):
            current_file = tgt + scheme.replace("%X", str(x)).replace("%Y", str(y))
            hdd_target = str(x) + "_" + str(y) + ".jpg"
            urllib.request.urlretrieve(current_file, hdd_target)
            if isVerbose is "V" or isVerbose is "v":
                print("Downloaded X ", x, " Y ", y)

