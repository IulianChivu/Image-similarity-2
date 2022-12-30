from skimage import color
import time
import glob
import os
import numpy as np
from PIL import Image
from skimage.io import imsave

def window_processing(roi, current_value, mask, window_size):

    roi = (roi > current_value).astype(int)
    roi[window_size//2, window_size//2] = 0
    
    return np.sum(roi * mask)



def lbp(img, window_size, mask):
    
    img = color.rgb2gray(img)
    h,w=img.shape
    
    I1 = img[1:h-1,1:w-1]<img[0:h-2,0:w-2]
    I2 = img[1:h-1,1:w-1]<img[0:h-2,1:w-1]
    I3 = img[1:h-1,1:w-1]<img[0:h-2,2:w]
    
    I4 = img[1:h-1,1:w-1]<img[1:h-1,2:w]
    I5 = img[1:h-1,1:w-1]<img[2:h,2:w]
    
    I6 = img[1:h-1,1:w-1]<img[2:h,1:w-1]
    I7 = img[1:h-1,1:w-1]<img[2:h,0:w-2]
    I8 = img[1:h-1,1:w-1]<img[1:h-1,0:w-2]
    
    I1 = I1*(2**7)
    I2= I2*(2**6)
    I3 = I3*(2**5)
    I4= I4*(2**4)
    I5= I5*(2**3)
    I6 = I6*(2**2)
    I7 = I7*2
    I8= I8*1

    new_img = I1+I2+I3+I4+I5+I6+I7+I8
    
    return new_img
    
def compute_lbp_on_single_image(image_path):
    '''
    input: [str] image_path
    oruput: [numpy_array] lbp_image
    '''
    mask = np.array([[7,6,5], [0,0,4], [1,2,3]])
    mask = pow(2, mask)
    
    new_img = Image.open(image_path)
    new_img = new_img.resize((384, 256))
    new_img = np.array(new_img)
    new_img = lbp(new_img, 3, mask)
    #new_img = new_img.astype(int)
    
    return new_img
    
train_image_files = glob.glob('./oxford_dataset_splited/train/*/*.jpg')

#save lbp data
start = time.time()
for i in range(17):
    if not os.path.exists(os.path.join("data_lbp", str(i+1))):
        os.makedirs(os.path.join("data_lbp", str(i+1)))

current_class = 1
counter_class = 0
no_samples_in_class = 40
for e in train_image_files:
    #get only the first 50 samples from every class
    if int(e.split('\\')[1]) == 10 and (int(e[-8:-4])) == 0:
        current_class = 10
        counter_class = 0
    elif int(e.split('\\')[1]) == 2 and (int(e[-8:-4])) == 0:
        current_class = 2
        counter_class = 0
    elif int(e.split('\\')[1]) == current_class + 1:
        current_class += 1
        counter_class = 0
    
    if int(e.split('\\')[1]) == current_class and counter_class < no_samples_in_class:
        print(e)
        #print(int(e.split('\\')[1]))
        new_location = e[:2] + 'data_lbp' + e[30:]

        #img_lbp = lbp(plt.imread(e), 3, mask)
        img_lbp = compute_lbp_on_single_image(e)

        imsave(new_location, img_lbp.astype(np.uint8))
        
        counter_class += 1
    #else:
        #do nothing
        #print(int(e[-7:-4]))

print()
print(time.time() - start)