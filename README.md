<div align="center">
    <h1>Plant phenotyping classification</h1>
</div>

<p align="center">
    <a href="https://github.com/scivision-gallery/plant-phenotyping-classification/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <a href="https://mybinder.org/v2/gh/scivision-gallery/plant-phenotyping-classification/HEAD?labpath=mapreader_plant_scivision.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://github.com/scivision-gallery/plant-phenotyping-classification/workflows/Continuous%20integration/badge.svg">
        <img alt="Continuous integration badge" src="https://github.com/scivision-gallery/plant-phenotyping-classification/workflows/Continuous%20integration/badge.svg">
    </a>
    <br/>
</p>


Understanding how the genetics of plants interact with their environment to produce certain chateristics or 'phenotypes' is critical to understand how they might grow under different conditions. In relation to agriculture, extracting accurate data on pehnotype may help us to better manage plants to produce higher-yield, more resilient crops, and plan for future food security by predicting how crops may grow under various climate change scenarios.
State-of-the-art plant phenotyping platforms have recently been established in the UK, such as the National Plant Phenomics Centre that collect high spatiotemporal resolution imagery of plants, as well as data on plant genetics and environmental conditions. However, extraction phenomic data from these images is expensive and time consuming to carry out manually.
We are working with the NPPC to automated extraction of plant phenotype data from various datasets, one of which is comprised of time-series images of individual brassica napus plants. We want to track the change and emergence of different plant structures (such as leaves, flowers, branches and seed pods) over time.
In this notebook we use the scivision Python API to load example plant data (at individual and satellite scale) and perform inference with MapReader model trained on NPPC images of individual brassica plants. MapReader (https://github.com/Living-with-machines/MapReader) is an end-to-end computer vision (CV) pipeline developed to analyse historical maps as scale, using a patch classification approach to to identify landscape features i.e. railways and buldings and examine change in these classes over time. The aim of the mapreader-plant model is to classify different parts of plants and track how they change over time in a similar fashion.

Link: https://github.com/alan-turing-institute/mapreader-plant-scivision
