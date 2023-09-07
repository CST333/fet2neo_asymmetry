# %%
import ants
import os
import shutil

def load_data(subj, session):
    # original file path
    orig_session=os.path.join()
    # load original file
    original_image=ants.image_read()
    
    # flipped file path
    flipped_session=os.path.join()
    # load flipped image 
    flipped_image=ants.image_read() 
    
    # template
    template_image=ants.image_read()
    
    # template mask
    template_mask=ants.image_read()
    
    return original_image, flipped_image, template_image, template_mask

def define_transform_paths(subj, session):
    linear_transform_path = os.path.join()
    linear_imageoutput_path = os.path.join()
    nonlinear_transform_path = os.path.join()
    nonlinear_imageoutput_path = os.path.join()
    jac_output_path= os.path.join()
    ants_prefix = os.path.join()

    return linear_imageoutput_path,linear_transform_path, nonlinear_imageoutput_path, nonlinear_transform_path, jac_output_path

def subj2temp_applyreg2JD(JD, fixed, transformlist):
    mywarpedimage = ants.apply_transforms(fixed = fixed, moving = JD, transformlist = transformlist, interpolator = "multiLabel", verbose=True)
    
    return mywarpedimage
# %%
for subj in subjects:
    print("subject : " + str(subj))
    # %%
    # original
    print("subject : " + str(subj))
    original_image, flipped_image, template_image, template_mask = load_data(subj, "neonatal")
    linear_imageoutput_path,linear_transform_path, nonlinear_imageoutput_path, nonlinear_transform_path, jac_normal_output_path = define_transform_paths(subj, "non_flipped")
    transformlist=[nonlinear_transform_path, linear_transform_path]
    print(transformlist)
    mywarpedimage = subj2temp_applyreg2JD(ants.image_read(os.path.join()), template_image, transformlist)
    ants.image_write(mywarpedimage, jac_normal_output_path)
    
    
    # flipped images
    linear_imageoutput_path,linear_transform_path, nonlinear_imageoutput_path, nonlinear_transform_path, jac_flipped_output_path = define_transform_paths(subj, "flipped")
   
    transformlist=[nonlinear_transform_path, linear_transform_path]
    print(transformlist)
    mywarpedimage = subj2temp_applyreg2JD(ants.image_read(os.path.join(), template_image, transformlist) 
    ants.image_write(mywarpedimage, jac_flipped_output_path)
# %%
