#!/bin/bash
#whitens / bleaches T2 weighted fetal or neonatal image for non-linear registration - replaces background with a bright color, removes black rim around the eCSF
#usage: please add afni to PATH and LD_LIBRARY_PATH e.g. /usr/local/afni/
#T2 image is $1 first position argument

image=$1
directory=$(dirname $1)
imagename=$(basename $image .nii.gz)

#removes data since AFNI by default cannot overwrite files
rm $directory/kmeans*

#does a quick kmeans for 2 classes, nicely finds background and foreground
3dkmeans -f $image -k 2 -remap COUNT -prefix $directory/kmeans.nii.gz 

#thresholds to background
fslmaths $directory/kmeans.nii.gz -thr 2 -bin $directory/kmeans.nii.gz

#gets the intensity value of the 99th percentile, used for the white overlay
thr=$(fslstats $image -P 99)

#does cluster detection. exports cluster size image. This is used to actually identify morphologically coherent cluster (background) against some wholes in the brain, which are small clusters that are closed
cluster -i $directory/kmeans.nii.gz -t 1 --osize=$directory/size.nii.gz

#thresholds the cluster that's larger than 10000 voxels (the brain itself was thresholded out in a previous step, so that won't count)
fslmaths $directory/size.nii.gz -thr 10000 -bin $directory/temp.nii.gz

#removes holes (closing), smoothes a bit, dilates the background label by 1 and creates overlay label
fslmaths $directory/temp.nii.gz -ero -ero -dilM -dilM -dilM -mul $thr $directory/overlay.nii.gz

#inverts overlay label, thresholds T2 image
fslmaths $directory/overlay.nii.gz -binv $directory/overlay_inverted.nii.gz
fslmaths $image -mas $directory/overlay_inverted.nii.gz $directory/temp.nii.gz

#adds the thresholded T2 and overlay together
fslmaths $directory/temp.nii.gz -add $directory/overlay.nii.gz $directory/"$imagename"_bleached.nii.gz

#removes temporary files
rm $directory/temp.nii.gz
rm $directory/overlay_inverted.nii.gz
rm $directory/overlay.nii.gz
rm $directory/size.nii.gz
rm $directory/kmeans.nii.gz
