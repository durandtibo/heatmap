
import heatmap
from scipy import ndimage
from skimage import io
import numpy as np

# read image
image_filename = '../data/face.png'
image = io.imread(image_filename)

# create heat map
x = np.zeros((101, 101))
x[50, 50] = 1
heat_map = ndimage.filters.gaussian_filter(x, sigma=16)


heatmap.add(image, heat_map, alpha=0.7, save='../data/face_heat_map.png')


for alpha in np.arange(0, 1.1, 0.1):
    print('alpha ' + str(alpha))
    heatmap.add(image, heat_map, alpha=alpha, save='../data/face_heat_map_' + str(alpha) + '.png', axis='off')
