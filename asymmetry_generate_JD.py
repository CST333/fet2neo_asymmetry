''' 
title: asymmetry analysis JD map generation
project: Asymmetry project
version: 1.0 - Feb 2023

This is script extracts JD files. The project has two analysis approaches:

    - fetal to neonatal
    - fetal and neonatal to mid-template
    
'''
#%%
import ants

domain_image_path='neonatal_image.nii.gz'
transformation_path='fetal2neonatal_image_1Warp.nii.gz'


def extract_JD_image(domain_image_path, transformation_path, do_log=False, geom= False):
    ''' creates JD files based on nonlinear registration
            input:
            domain_image (ANTsImage) – image that defines transformation domain (fixed image)
            tx (string) – deformation transformation file name
            do_log (boolean) – return the log jacobian
            geom (bolean) – use the geometric jacobian calculation (boolean)
            
            output: written JD file
    '''
    #jac = ants.create_jacobian_determinant_image(fi,mytx['fwdtransforms'][0],1)
    domain_image=ants.image_read(domain_image_path)
   # tx = ants.image_read(transformation_path) #ants.read_transform(transformation_path)
    jac= ants.create_jacobian_determinant_image(domain_image, transformation_path, do_log=True, geom=False)
    ants.image_write(jac, '.nii.gz')
    return jac


#jac=extract_JD_image(domain_image_path, transformation_path, do_log=False, geom= False)
