import numpy as np
from PIL import Image

img = Image.open("/home/sounak_pro/Downloads/myname").convert("L")
print(img)
img_array = np.array(img)
print(img_array)
