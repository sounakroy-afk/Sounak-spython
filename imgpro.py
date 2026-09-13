import numpy as np
from PIL import Image

img = Image.open("/home/sounak_pro/Downloads/myname").convert("L")
print(img)
img_array = np.array(img)
print(img_array)
print("Shape (Heigh,Width):", img_array.shape)
print("dimensions:", img_array.ndim)
print(img_array[100:105, 100:105])
maximum_value = img_array.max()
minimum_value = img_array.min()
print(maximum_value)
print(minimum_value)
print(img_array[0:10, 0:10])
inverted_image = 255 - img_array
print(inverted_image[0:10, 0:10])
print(
    "Taking alpha as the constant for contrast and beta as the constant for brightness"
)
print(
    "we will use alpha with multiplication for editing and beta with addition for editing"
)
alpha = float(input("Enter the value of alpha but it not being less than 1:"))
beta = float(input("Enter the value of beta but its not being less than 0:"))
adjusted_img_array = np.clip(img_array * alpha + beta, 0, 255)
print(adjusted_img_array)
crop = img_array[2:10, 2:5]
crop_horizontal = crop[:, ::-1]
print(crop_horizontal)
