# UNRAVEL
The UNRAVEL study (Utility of the Non-Invasive MRI Assessment of Tenosynovial Amyloidosis for the Early Detection of Cardiac Amyloidosis) is a research initiative aimed at evaluating the potential of MRI-based imaging to detect amyloid deposition in the carpal tunnel as an early marker of systemic amyloidosis, particularly before significant cardiac involvement. By utilizing advanced MRI techniques, including Magnetization Transfer Ratio (MTR) imaging, the study seeks to quantify amyloid burden in tendons and assess its correlation with cardiac amyloidosis progression.

# Image Registration
We used Advanced Normalization Tools (ANTs) in Python for volume registration. The registration was performed using an affine transformation, aligning the magnetization transfer (MT) on-image to the off-image. The following Python script demonstrates the process.

# MTR Visualization
To visualize the Magnetization Transfer Ratio (MTR) maps obtained from qMRLab fits, we developed a Python script that loads .mat files, extracts the MTR volume, and displays specific slices with optimized contrast adjustments. The script also saves the images for documentation and further analysis.
