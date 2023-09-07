cd /asymmetry_dataset/fet2neo/JD_in_neonatal_space

for subj in #
do
 3dBlurInMask -prefix ${subj}_jd_masked_blurred.nii.gz -FWHM 6 -mask /brain_asymmetry_analyis/dataset/${subj}/neonatal/orig/${subj}_neonatal_mask.nii.gz -input ${subj}_jd_masked.nii.gz
done