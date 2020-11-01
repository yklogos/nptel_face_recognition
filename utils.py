import cv2

def make_dict_from_lists(list1, list2, one2two = True):
    if one2two:
        final = {list1[i]:list2[i] for i in range(len(list1))}
    else:
        final = {list2[i]:list1[i] for i in range(len(list1))}

def make_rgb_bgr(img):
    b,g,r = cv2.split(img)          
    rgb_img = cv2.merge([r,g,b]) 
    return rgb_img

def read_bgr(path):
    return make_rgb_bgr(cv2.imread("sample.jpg", -1))

def imshowg(gray):
    plt.imshow(gray, cmap='gray')
    
def plot_image_list(img_list, figsize=(12, 12), subplot_n_cols=2):
    plt.figure(figsize=(12, 12))
    for i,img in enumerate(img_list):
        plt.subplot(int(len(img_list)/subplot_n_cols)+1, subplot_n_cols, i+1)
        try:
            plt.imshow(img)
        except:
            pass