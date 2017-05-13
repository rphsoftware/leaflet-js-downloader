import downloader
import stitcher
import time

print("Welcome to leaf-dl!")
domain = input("Please specify a domain of the map!\n")
folder = input("Please specify a folder on the map-server!\n")
tgt = domain + folder
scheme = input("Please specify a scheme for the file (as an example 3_%X_%Y.jpg)\n")
isVerbose = input("Type in V if you want the program to be verbose!\n")
x_amount = 0
y_amount = 0
try:
    x_amount = int(input("Enter the amount of tiles on the X axis!\n"))
    y_amount = int(input("Enter the amount of tiles on the Y axis!\n"))
except ValueError:
    print("That's not an int!")
    time.sleep(3)
    exit()

print("Starting download.")
try:
    downloader.download(tgt, scheme, isVerbose, x_amount, y_amount)
except:
    print("An error occured while downloading. Program will now clean up and quit")
    stitcher.cleanup(x_amount, y_amount, isVerbose)
    time.sleep(3)
    quit()
print("Download done without any errors!")
out_image = input("Output image name?\n")
try:
    stitcher.stitch(x_amount, y_amount, isVerbose, out_image)
except:
    print("An error occured while stitching. Program will now clean up and quit!")
    stitcher.cleanup(x_amount, y_amount, isVerbose)
    time.sleep(3)
    quit()

print("All done!")
