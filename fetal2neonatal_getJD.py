#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

- extract JD from fet2neo registration and save JD and flipped JD

"""

# IMPORT Libraries ------------------------------------------------
# %%

import os
import sys

# Global variables -----------------------------
from config import subjects, bash_cmd
# Functions ----------------------------------------------------

def create_JD(neo_image, registration, jac_path):
    cmd='CreateJacobianDeterminantImage 3 '+registration+' '+jac_path+' 1'
    bash_cmd(cmd)
   # jac = ants.create_jacobian_determinant_image(neo_image,,1) #  registration['fwdtransforms'][0]
   # ants.image_write(jac, jac_path)
   

def mask_JD(jac_path, mask_path, jac_masked_path):
    fsl_cmd=" ".join(("fslmaths", jac_path, "-mas", mask_path, jac_masked_path))
    bash_cmd(fsl_cmd)
    
def flip_JD(image_path, flippedpath):
    cmd='img='+str(image_path)+' ; flipped='+str(flippedpath)+'; 3dLRflip -LR -prefix $flipped $img'
    bash_cmd(cmd)
    

# main -----
for sub in subjects:
    imagepath = os.path.join("")
    mask_path= os.path.join("")
    jac_path = os.path.join("_jd.nii.gz")
    jac_masked_path = os.path.join("_jd_masked.nii.gz")
    flipped_JD= os.path.join("_jd_masked_flipped.nii.gz")
    registration=os.path.join("")
    jac = create_JD(imagepath,registration, jac_path)
    mask_JD(jac_path, mask_path, jac_masked_path)
    flip_JD(jac_masked_path, flipped_JD)

        
        
