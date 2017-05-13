from PIL import Image

def stitch(x_amount, y_amount, isVerbose, outimage):
    output = Image.new("RGB", (x_amount * 256, y_amount * 256))
    for x in range(x_amount):
        for y in range(y_amount):
            inputimg = Image.open(str(x) + "_" + str(y) + ".jpg")
            output.paste(inputimg, (x * 256, y * 256))
            if isVerbose is "V" or isVerbose is "v":
                print(str(x) + "_" + str(y) + ".jpg")
    output.save(outimage + ".jpg")