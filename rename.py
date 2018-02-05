import os
#take file names of a folder rename them
#Use this for 1 folder at a time
#use inside a pen drive is possible just to be safe
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        for i, filename in enumerate(os.listdir(dirname)):
            os.rename(dirname + "/" + filename, dirname + "/" +"Pigweed"+ "."+ str(i) + ".jpg")

'''for root, dirs, files in os.walk(".", topdown=False):
    for dirname in os.listdir("."):
        if os.path.isdir(dirname):
            for i, filename in enumerate(os.listdir(dirname)):
                os.rename(dirname + "/" + filename, dirname + "/" + dirname  + "." + str(i) + ".jpg")'''
