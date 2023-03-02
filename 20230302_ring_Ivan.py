
## based on https://stackoverflow.com/questions/10031580/how-to-write-simple-geometric-shapes-into-numpy-arrays

from skimage import draw
import tifffile as tf
import numpy as np

pxl_size          = 2       # instead of 25 nm
img_physize       = 1000    # instead of 5000 nm

desired_width      = 10
desired_diameter   = 60


img_size = int(np.floor(img_physize/pxl_size))
arr      = np.zeros([img_size,img_size])

ring_width    = desired_width / pxl_size
ring_radius   = (desired_diameter/2)/ pxl_size

print(ring_width, ring_radius)

inner_radius = ring_radius - (ring_width // 2) + (ring_width % 2) - 1 
outer_radius = ring_radius + ((ring_width + 1) // 2)

ri, ci = draw.disk((img_size//2, img_size//2),inner_radius, shape=arr.shape)
ro, co = draw.disk((img_size//2, img_size//2),outer_radius, shape=arr.shape)
arr[ro, co] = 1
arr[ri, ci] = 0

tf.imwrite('ring.tif',arr.astype(np.float32),
            resolution=(1E7/pxl_size, 1E7/pxl_size,'CENTIMETER'))## in microns
