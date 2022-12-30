import sys
from skimage import color
import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt

def euclidean_distance(img1, img2):
    return np.sqrt(np.sum(np.power(img1 - img2, 2)))
    
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
 
lbp_image_files = glob.glob('./data_lbp/*/*.jpg')
 
ref = sys.argv[1]

new_img = compute_lbp_on_single_image(ref)

#get min euclidean distance from database
ed_list = []
for e in lbp_image_files:
    img_database = plt.imread(e)

    ed_list.append(euclidean_distance(img_database, new_img))

minimum = min(ed_list)
min_index = ed_list.index(minimum)
pred_lbp = lbp_image_files[min_index]
pred = pred_lbp[:6] + pred_lbp[10:]
#print(minimum)
#print(min_index)
print(pred)

fig, (ax1, ax2) = plt.subplots(1, 2)

image1 = plt.imread(ref)
image2 = plt.imread(pred)

# Show the first image on the left subplot
ax1.imshow(image1)
ax1.set_title("reference")

# Show the second image on the right subplot
ax2.imshow(image2)
ax2.set_title("predicted")

plt.show()