from PIL import Image
import os


def stitch(x_amount, y_amount, is_verbose, out_image):
    output = Image.new("RGB", (x_amount * 256, y_amount * 256))
    for x in range(x_amount):
        for y in range(y_amount):
            input_img = Image.open(str(x) + "_" + str(y) + ".jpg")
            output.paste(input_img, (x * 256, y * 256))
            if is_verbose is "V" or is_verbose is "v":
                print("Stitched : " + str(x) + "_" + str(y) + ".jpg")
    output.save(out_image + ".jpg")
    cleanup(x_amount, y_amount, is_verbose)


def cleanup(x_amount, y_amount, is_verbose):
    for x in range(x_amount):
        for y in range(y_amount):
            try:
                os.remove(str(x) + "_" + str(y) + ".jpg")
                if is_verbose is "V" or is_verbose is "v":
                    print("Deleted : " + str(x) + "_" + str(y) + ".jpg")
            except:
                print("Couldn't delete : " + str(x) + "_" + str(y) + ".jpg")
