import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Load MTR Data from .mat file
mat_file_path = "fitted_file_location"
mat_data = scipy.io.loadmat(mat_file_path)
mtr_image = mat_data['MTR']

# Select and transform a slice
slice_idx = 21  # Change index to view different slices
mtr_image = np.transpose(mtr_image, (0, 1, 2))  # Adjust slice orientation

# Display range adjustment for visualization
vmin, vmax = np.percentile(mtr_image[slice_idx, :, :], [2, 98])

# Display raw qMRLab Fit Slice for validation
plt.figure(figsize=(3, 3))
plt.title(f'MTR - Slice {slice_idx}')
plt.imshow(mtr_image[slice_idx, :, :], cmap='viridis', vmin=0, vmax=4)  
plt.colorbar(label='MTR (%)')
plt.show()

# Display MTR Slice with 'jet' colormap
fig, ax = plt.subplots(figsize=(3, 3))
img = ax.imshow(mtr_image[slice_idx, :, :], cmap='jet', vmin=0, vmax=4)  
ax.set_xticks([])
ax.set_yticks([])
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
cax = inset_axes(ax, width="4%", height="100%", bbox_to_anchor=(0.03, -0.03, 1, 1), bbox_transform=ax.transAxes, loc='lower right')
plt.colorbar(img, cax=cax, orientation='vertical', label='MTR (%)')
plt.show()
