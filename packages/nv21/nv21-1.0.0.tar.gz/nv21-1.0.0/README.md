# nv21
Functions for reading and decoding the data of frames in NV21 format.

Basically it wraps the cv2-based conversion with some check in order to avoid some confusing cv2 errors.

## Available functions

* `nv21_to_rgb`
* `read_nv21_from_file`
* `yuv_to_nv21`

Example
```python
import cv2
import matplotlib.pyplot as plt  # do not forget to install `matplotlib` first

import nv21


# Check the "data" folder of this repository.
img = cv2.imread('./data/example.png')[..., ::-1]  # to RGB
h, w = img.shape[:2]

nv21_data = nv21.yuv_to_nv21(
    cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
)

restored_img = nv21.nv21_to_rgb(nv21_data, w, h)

# Draw results
plt.subplot(1, 3, 1)
plt.axis('off')
plt.imshow(img)

plt.subplot(1, 3, 2)
plt.axis('off')
plt.imshow(nv21_data, cmap='gray')

plt.subplot(1, 3, 3)
plt.axis('off')
plt.imshow(restored_img)

plt.show()
```
