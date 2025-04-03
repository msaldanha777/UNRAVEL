# Image Registration
We used Advanced Normalization Tools (ANTs) in Python for volume registration. The registration was performed using an affine transformation, aligning the magnetization transfer (MT) on-image to the off-image. The following Python script demonstrates the process.

# MTR Data Visualization
To visualize the Magnetization Transfer Ratio (MTR) maps obtained from qMRLab fits, we developed a Python script that loads .mat files, extracts the MTR volume, and displays specific slices with optimized contrast adjustments. The script also saves the images for documentation and further analysis.
