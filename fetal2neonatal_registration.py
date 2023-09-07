#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

linearly and nonlinearly registers fetal to neonatal

registrations:
- flirt
- Rigid + Affine antsAI
- antspy: "Affine", "TRSAA", "Similarity"
settings:
- using a mask/erroded mask, no mask

output: ".mat" file ready to use in the subject folder, "T2" images in the metrics folder

"""

# IMPORT Libraries ------------------------------------------------
import os
import shutil
import sys
import ants

# Global variables -----------------------------
from config_fet2neo import masking, session, subjects, where, nonlin_regtest_list_antspy

# Functions ----------------------------------------------------

    
# MAIN ---------------------------------------------------------

if __name__ == "__main__":
    
    print("linear registrations ...")
    
    print("these subjects will be registered: ")
    print(subjects) # loaded from config
    
    for subj in subjects:
    
            ## Location of original images
            # fetal
            orig_session0=os.path.join()
            # neonatal 
            orig_session1=os.path.join()

            ## antspy part -----------------------------------------------------
            
            # load template
            fixed=ants.image_read(orig_session1)
            fixedImageseg1 = os.path.join() # segmenation file
            # load original images 
            moving0=ants.image_read(orig_session0) #fetal  
            movingImageseg0 = os.path.join()  #segmenationfile
            
            for mask in masking:
                if mask == "masked":
                    mask_temp=ants.image_read()
                elif mask == "erroded_masked":
                    mask_temp=ants.image_read()
                elif mask == "nomask":
                    mask_temp= "NA"
 
                
                for transform in ["TRSAA"]:  
                    print("computing registration to:" +where + "mask: " + mask + " transfrom: " + transform)
                
                    # fetal 
                    if mask=="nomask":
                        registration0 = ants.registration(fixed = fixed, moving = moving0, type_of_transform= transform )
                    else: 
                        registration0 = ants.registration(fixed = fixed, moving = moving0, mask=mask_temp, type_of_transform= transform )

                    # save moved T2 image
                    warped_moving0 = registration0["warpedmovout"]
                    warped_moving0.to_filename(os.path.join()
                    
                    # save matrix
                    linearreg_session0=os.path.join()
                    shutil.copy(registration0['fwdtransforms'][0], linearreg_session0)


            ## nonlinear registration ---------
            # fetal
            orig_session0=os.path.join()
            orig_session0_labels=os.path.join()
            
            # neonatal 
            orig_session1=os.path.join()
            orig_session1_labels=os.path.join()
            
            
            # load original images 
            moving0=ants.image_read(orig_session0) # fetal  
            fixed=ants.image_read(orig_session1) # neonatal
            
            # the path to the segmentation of the neonates
            #orig_session1_labels 
            
            for mask in non_linear_masking:
                # load masks
                if mask == "masked":
                    mask_temp=ants.image_read()
                    
                elif mask == "eroded_masked":
                    mask_temp=ants.image_read()
                elif mask == "nomask":
                    mask_temp= None
 
                
               
                # read in initial linear transform for fetal to neonatal
                linearreg0=(os.path.join())
                
            
                # We will now call:     ants.registration(fixed, moving, type_of_transform='SyN', initial_transform=None, outprefix='', mask=None, 
                #                              grad_step=0.2, flow_sigma=3, total_sigma=0, aff_metric='mattes', aff_sampling=32, syn_metric='mattes', 
                #                              syn_sampling=32, reg_iterations=(40, 20, 0), verbose=False, **kwargs)
                
                
                for transform in nonlin_regtest_list_antspy: # ['SyNOnly']
                        print("computing registration to: " +where + " mask: " + mask + " transfrom: " + transform)
                        
                        if transform == 'SyNOnly':  
                            
                            for syn_metric in antspy_syn_metric: # ["CC"]
            
                                if syn_metric== 'CC':
                                      for syn_sampling in antspy_syn_sampling_cc:   # [2]
                                          
                                          for count, reg_iterations in enumerate([ (100, 70, 50, 20)]): #(40, 20, 0),
                                            # session 0 (fetal) 
                                            registration0 = ants.registration(fixed = fixed, moving = moving0, mask=mask_temp, type_of_transform= transform, 
                                                                            syn_metric = syn_metric, syn_sampling=syn_sampling, reg_iterations=reg_iterations, initial_transform= linearreg0)
                                            
                                            # save moved T2 image
                                            warped_moving0 = registration0["warpedmovout"]
                                            warped_moving0.to_filename(os.path.join())
                                            
                                            # save matrix
                                            linearreg_session0=os.path.join()
                                            shutil.copy(registration0['fwdtransforms'][0], linearreg_session0)
                                            linearreg_session0_inv=os.path.join()
                                            shutil.copy(registration0['invtransforms'][1], linearreg_session0_inv)
                            

                        
                                        