"""
Exercise 2, Part 2
"""

# Load tools
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as io

# Load movie as array
mov = 'TEST_MOVIE_00001-small.tif'  # movie should be in the same directory
mov_frames = io.imread(mov)  # shape: t x width_pixels x height_pixels
M = np.array(mov_frames).astype('float64')  # M for movie

fig,ax = plt.subplots(1,2)
fig.suptitle('Alternate Summary Image Approaches')
# Approach 1: Let's try mean-centering and finding the top quantile for each pixel
M1 = M.copy()
M1-=M1.mean(axis=0);
M_quant = np.quantile(M1,q=1,axis=0)  # compute quantile: 1.0
ax[0].imshow(M_quant,cmap='gray')
ax[0].set_title('Approach 1: Quantile')

# Approach 2: Let's try basic entropy
M2=M.copy()
M2[M2<=.5*M2.max()] = -1e-6  # make small values constant to prevent biasing by Gaussian noise
M2 /= M2.max(axis=0); M2 += abs(M2.min(axis=0))+1e-6  # scale, make nonzero so probability behaves
M_prob = M2/M2.sum(axis=0, keepdims=True)  # compute probability
M_entr = (-M_prob*np.log2(M_prob)).sum(axis=0)  # compute entropy
ax[1].imshow(M_entr, cmap='gray_r')
ax[1].set_title('Approach 2: Entropy')
plt.show()