# Dataset Augmentation Workflow for Tensorflow Object Detection API

## Introduction
This repository provides a comprehensive workflow for augmenting and randomizing both images and their corresponding labels (annotations generated using [labelImg](https://github.com/tzutalin/labelImg)). The aim is to prepare a well-structured dataset for training with the Tensorflow Object Detection API.

## Directory Structure
Create the following organized directory structure:

```
.
└───annotations
|   └───xml
└───data
│   └───split
└───images
|   └───train
|   └───test
└───sample_images
└───sample_labels
│   AnnotationAugmentation.py
│   Augmentation.py
│   Labeling.py
│   Randomize.py
│   Readme.md
│   Renaming.py
│   TrainTestSplit.py
│   XMLtoCSV.py
```

## Steps

1. **Prepare Sample Images and Labels**:
   - Place raw images in the `sample_images` folder.
   - Utilize [labelImg](https://github.com/tzutalin/labelImg) to label the sample images and save annotations in the `sample_labels` folder.

2. **Image Augmentation**:
   - Apply image augmentations using the script `Augmentation.py`.

3. **Label Augmentation**:
   - Apply label augmentations using the script `AnnotationAugmentation.py`.

4. **Consolidation**:
   - Copy the contents of the `sample_images` folder to the `images` folder.
   - Copy the contents of the `sample_labels` folder to the `annotations/xml` folder.

5. **Randomization**:
   - Shuffle the images and labels within the `images` and `annotations/xml` folders using `Randomize.py`.

6. **Update Annotations**:
   - Update XML files' contents with updated image and label directories by running `Labeling.py`.

7. **XML to CSV Conversion**:
   - Convert all XML files to a single CSV using `XMLtoCSV.py`.

8. **Train-Test Split**:
   - Create `train` and `test` subfolders within the `images` directory.
   - Split the dataset into train and test images using `TrainTestSplit.py`.

## Results
- The `images` directory is organized into `train` and `test` subdirectories, each containing their respective images for training and testing.
- The `data` directory holds a `split` subdirectory with two CSV files for labels corresponding to train and test images.
- All images and labels are sequentially named and their directories are updated as part of the workflow.

By following this structured workflow, you can efficiently augment, randomize, and prepare your dataset for optimal utilization with the Tensorflow Object Detection API.
