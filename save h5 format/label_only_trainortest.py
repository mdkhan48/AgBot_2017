from random import shuffle
import glob
import cv2

shuffle_data = False  # shuffle the addresses before saving
hdf5_path = '/home/sayem/Desktop/Agbot NN/trai200_new_128pix.hdf5'  # address to where you want to save the hdf5 file
cat_dog_train_path = '/home/sayem/Desktop/Agbot NN/traincatdog200/*.jpg'
# read addresses and labels from the 'train' folder
addrs = glob.glob(cat_dog_train_path)
labels = [0 if 'cat' in addr else 1 for addr in addrs]# 0 = Cat, 1 = Dog
#print (labels)
# to shuffle data
'''if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)'''
train_addrs = addrs[0:int(len(addrs))]
train_labels = labels[0:int(len(labels))]
#print (train_labels)

import numpy as np
import h5py
train_shape = (len(train_addrs), 128, 128, 3)
#print (train_shape)
hdf5_file = h5py.File(hdf5_path, mode='w')
t1=hdf5_file.create_dataset("train_img", train_shape, np.uint8)
l1=hdf5_file.create_dataset("train_labels", (len(train_addrs),), np.int8)
hdf5_file["train_labels"][...] = train_labels

print(l1.shape)

# loop over train addresses
for i in range(len(train_addrs)):
    # print how many images are saved every 1000 images
    if i % 100 == 0 and i > 1:
        print ('Train data: {}/{}'.format(i, len(train_addrs)))
    # read an image and resize to (224, 224)
    # cv2 load images as BGR, convert it to RGB
    addr = train_addrs[i]
    img = cv2.imread(addr)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #save
    hdf5_file["train_img"][i, ...] = img[None]

hdf5_file.close()