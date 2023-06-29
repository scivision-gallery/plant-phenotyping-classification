<div align="center">
    <h1>Classification of plant images using Computer Vision</h1>
</div>

<p align="center">
    <a href="https://github.com/scivision-gallery/plant-phenotyping-classification/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <a href="https://mybinder.org/v2/gh/scivision-gallery/plant-phenotyping-classification/HEAD?labpath=mapreader_plant_scivision_v2.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://github.com/scivision-gallery/plant-phenotyping-classification/workflows/Continuous%20integration/badge.svg">
        <img alt="Continuous integration badge" src="https://github.com/scivision-gallery/plant-phenotyping-classification/workflows/Continuous%20integration/badge.svg">
    </a>
    <br/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/1899856/159468646-8bb13932-d593-4dc9-affe-927b023d9c55.png" 
        alt="Classification of plant images using MapReader" width="60%" align="center">
</p>

<p align="center">
    <em>
    Classification of a plant image using MapReader (https://github.com/Living-with-machines/MapReader). This multiclass classification had three labels: None; Flower (red patches); Non-flower plant-related (yellow patches).  
    </em>
</p>

## Abstract

Understanding how the genetics of plants interact with their environment to produce certain chateristics or 'phenotypes' is critical to understand how they might grow under different conditions. In relation to agriculture, extracting accurate data on pehnotype may help us to better manage plants to produce higher-yield, more resilient crops, and plan for future food security by predicting how crops may grow under various climate change scenarios.

State-of-the-art plant phenotyping platforms have recently been established in the UK, such as the National Plant Phenomics Centre that collect high spatiotemporal resolution imagery of plants, as well as data on plant genetics and environmental conditions. However, extracting phenomic data from these images is expensive and time consuming to carry out manually.

We are working with the NPPC to automate extraction of plant phenotype data from various datasets, one of which is comprised of time-series images of individual brassica napus plants. We want to track the change and emergence of different plant structures (such as leaves, flowers, branches and seed pods) over time.

Here, we use the scivision Python API to load example plant data (at individual and satellite scale) and perform inference with MapReader model trained on NPPC images of individual brassica plants. [MapReader](https://github.com/Living-with-machines/MapReader) is an end-to-end computer vision (CV) pipeline developed to analyse historical maps as scale, using a patch classification approach to to identify landscape features i.e. railways and buldings and examine change in these classes over time. The aim of the mapreader-plant model is to classify different parts of plants and track how they change over time in a similar fashion.

## How to run

1. Create a conda environment:

```bash
conda create -n plant_py38 python=3.8
conda activate plant_py38
```

2. Make sure you have [git-lfs](https://git-lfs.com/) installed

3. Clone the `plant-phenotyping-classification` repository:

```bash
git clone https://github.com/scivision-gallery/plant-phenotyping-classification.git
```

4. Install dependencies:

```bash
cd plant-phenotyping-classification
pip install -r requirements.txt
```

5. Open Jupyter Notebook:

```bash
pip install jupyter
jupyter notebook
```

Open one of the notebooks on the repository. Currently, we have:
- mapreader_plant_scivision_v2.ipynb

A full conda environment can be found in environment_full.yml which may be useful if you are having issues creating an environment in which to run the notebook. This contains details of all the packages and their versions which are required to run these notebooks, including secondary and tertiary dependencies.

## Where are the MapReader models stored?

Refer to: https://github.com/alan-turing-institute/mapreader-plant-scivision
