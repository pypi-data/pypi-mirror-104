# imhist  
This model calculates the histogram, PMF and CMD of a given matrix fast.  

# Usage  
```python
import cv2
import numpy as np
from imhist import imhist, imcdf
import matplotlib.pyplot as plt

img = cv2.imread('assets/Plane.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

v_hist = imhist(v)
v_pmf = imhist(v, PMF=True)
v_cdf = imcdf(v)

plt.figure(num=1)
plt.plot(np.arange(256), v_hist, 'b', label='Histogram')
plt.ylabel('Number of Occurrences')
plt.xlabel('Brightness')
plt.grid(which="both")
plt.legend()
plt.show()
```  
# Output
This is a sample image:  
![Sample Image](https://raw.githubusercontent.com/Mamdasn/imhist/main/assets/Plane.jpg "Sample Image")  
Histogram of the sample image:  
![Histogram of the Sample Image](https://raw.githubusercontent.com/Mamdasn/imhist/main/assets/Plane-Histogram.jpg "Histogram of the Sample Image")
