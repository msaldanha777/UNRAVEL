import ants

base = "file_location"
input_off = base + "\\MToff.nii"
input_on = base + "\\MTon.nii"
output_reg_on = base + "\\registered-MTon.nii"

# Load images
fixed_image = ants.image_read(input_off)
moving_image = ants.image_read(input_on)

# Perform affine registration
registration = ants.registration(fixed=fixed_image, moving=moving_image, type_of_transform='Affine')
registered_image = ants.apply_transforms(fixed=fixed_image, moving=moving_image, transformlist=registration['fwdtransforms'])
