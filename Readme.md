

# Dataset Augmentation For Tensorflow Object Detection API
## Methodology
This repository is used for augmentation and randomization of both images and their labels (annotations from https://github.com/tzutalin/labelImg) and preparing them for training Tensorflow object detection API.
1. Create the following directory structure:

	```
	.
	└───annotations
	| 	└───xml
	└───data
	│	└───split
	└───images
	└───sample images
	└───sample labels
	│   AnnotationAugmentation.py
	│   Augmentation.py
	│   Labeling.py
	│   Randomize.py
	│   Readme.md
	│   Renaming.py
	│   TrainTestSplit.py
	│   XMLtoCSV.py
	
2. Copy raw images to **sample images** folder
3. Run label master for labeling sample images (https://github.com/tzutalin/labelImg) and save them in **sample labels** folder
4. To apply augmentations on images run **Augmentation.py**
5. To apply augmentations on labels run  **AnnotationAugmentation.py**
6. Copy contents of **sample images** to **images** and contents of **sample labels** to **labels**
7. To shuffle images and labels run **Randomize.py**
8. Update contents of xml files by running **Labelling.py**
9. Run **XMLtoCSV.py** to convert all xml files to a single CSV 
10. Create 2 folders in **images** directory named **train** and **test**
11. To split train and test images run **TrainTestSplit.py**
## Results
* **images** directory contains two sub directories containing images for train and test dataset.
* **data** directory contains a subdirectory **split** which contains two .csv files for labels for train and test images.
* All images and labels are named in sequence and their directories  updated.
