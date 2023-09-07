#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


stack all JD for fslrandomise, neonatal space symmetrical


"""

# IMPORT Libraries ------------------------------------------------
# %%
import os
import shutil
import sys

# %%
# Global variables -----------------------------
from config_fet2neo import subjects, bash_cmd
# %%
# Functions ----------------------------------------------------
def get_image_list_string(subjects):
    string=''
    subject_list='' 
    
    for subj in subjects:
        string=" ".join([string, 'path'])
        subject_list+=subj+' 1 \n'
    for subj in subjects:
        string=" ".join([string, 'path'])
        subject_list+=str(subj)+' 0 \n'
    return string,  subject_list

def get_image_list_string_flipped_only(subjects):
    string=''
    subject_list='' 
  
    for subj in subjects:
        string=" ".join([string, 'path'])
        subject_list+=str(subj)+' 1 \n'
    return string,  subject_list

def stack_images(image_list_string, JD_merged_path):
    
    bash_cmd('fslmerge -a '+JD_merged_path+' '+image_list_string )
    #fslmerge -a JD_merged ${final_group}
    
# %%

image_string, subject_list = get_image_list_string(subjects)#
print(subject_list)

stack_images(image_string, 'outputpath.nii.gz')

image_string, subject_list = get_image_list_string_flipped_only(subjects)

stack_images(image_string, 'outputpath.nii.gz')