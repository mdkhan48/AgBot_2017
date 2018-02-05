import h5py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
hdf5_path = '/home/sayem/Desktop/Agbot NN/trai200_new_128pix.hdf5'

# open the hdf5 file
train_dataset = h5py.File(hdf5_path, "r")

for Ds in train_dataset:
    print (Ds, "--------",train_dataset[Ds])

train_set_x_orig = np.array(train_dataset["train_img"][:])
train_set_y_orig = np.array(train_dataset["train_labels"][:])
train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
#print (train_set_x_orig.shape)
#print (train_set_y_orig.shape)
index = 50
#object= str(train_set_y_orig[:, index])
#print (object[1])
'''if (object[1]!=0):
    object="dog"
else:
    object="cat" '''
plt.imshow(train_set_x_orig[index])
plt.show()
print ("y = " + str(train_set_y_orig[:, index]) + ", it's a CAT if y=[0] or DOG if y=[1] ")
print (train_set_x_orig[index].shape)