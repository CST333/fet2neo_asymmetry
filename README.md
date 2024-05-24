# Characterization of dynamic patterns of human fetal to neonatal brain asymmetry with deformation-based morphometry (DBM)
*Steger C, Moatti C, Payette K, De Silvestro A, Nguyen TD, Coraj S, Yakoub N, Natalucci G, Kottke R, Tuura R, Knirsch W and Jakab A (2023) Characterization of dynamic patterns of human fetal to neonatal brain asymmetry with deformation-based morphometry. Front. Neurosci. 17:1252850. doi: 10.3389/fnins.2023.1252850*
## Overview of the scripts

### scripts for data preparation
* shavel.sh : to create image with bright background
* flipping.sh : to flip brain images along their axis
* blurring.sh : script to blur JD maps

### scripts for image registration
* linear and nonlinear registration in antspy: registration calls for linear and nonlinear registration

### scripts for metric calculation and metric extraction

### scripts for JD extraction
* asymmetry_generate_JD.py : bashcommand to extract JD map of a registration### script to run asymmetry analysis
* stacking.sh : stacking JD into 4D image
* run_randomise.sh + run_randomise_report.txt : randomise call
* cluster.sh : call to report clusters

