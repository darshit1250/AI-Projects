# Predict Frog Family Through Croaks
  This machine learning project predicts family of a frog by its calls. 
  
# Problem Definition
  Acoustic classification of anurans (frogs) has received increasing attention for its promising application in biological and environment studies. In this study, a novel feature extraction method for frog call classification is presented based on the analysis of spectrograms. The frog calls are first automatically segmented into syllables. Then, spectral peak tracks are extracted to separate desired signal (frog calls) from background noise. The spectral peak tracks are used to extract various syllable features, including: syllable duration, dominant frequency, oscillation rate, frequency modulation, and energy modulation.
  
  This dataset was used in several classification tasks related to the challenge of anuran species recognition through their calls. It is a multilabel dataset with three columns of labels. This dataset was created segmenting 60 audio records belonging to 4 different families, 8 genus, and 10 species. Each audio corresponds to one specimen (an individual frog), the record ID is also included as an extra column. We used the spectral entropy and a binary cluster method to detect audio frames belonging to each syllable. After the segmentation we got 7195 syllables, which became instances for train and test the classifier. These records were collected in situ under real noise conditions (the background sound). Some species are from the campus of Federal University of Amazonas, Manaus, others from Mata Atlantic, Brazil, and one of them from Córdoba, Argentina. The recordings were stored in wav format with 44.1kHz of sampling frequency and 32bit of resolution, which allows us to analyses signals up to 22kHz. 

# Dataset
  * From every extracted syllable 22 MFCCs were calculated by using 44 triangular filters. These coefficients were normalized between -1 ≤ mfcc ≤ 1. Below is the dataset structure.
  * ![image](https://user-images.githubusercontent.com/67219027/119276134-21922f00-bbe7-11eb-9c4a-b987e5b04f3d.png)
  * Families: 
     * Bufonidae        :       68
     * Dendrobatidae    :       542
     * Hylidae          :       2165
     * Leptodactylidae  :       4420
  * Datasource: [UCI Machine Learning Repository: Anuran Calls (MFCCs) Data Set](https://archive.ics.uci.edu/ml/datasets/Anuran+Calls+%28MFCCs%29)

# Algorithms Used in this project
  * logistic regression
  * Gaussian Naive Bayes
  * K-Nearest Neighbour (KNN)
  * MLP classifier (NN)
  * Random Forest classifier

# Liberaries used in the project
  * ScikitLearn (https://github.com/scikit-learn/scikit-learn)
  * MatplotLib (https://github.com/matplotlib/matplotlib)
  * NumPy (https://github.com/numpy/numpy)
  * Seaborn (https://github.com/mwaskom/seaborn)
  * Pandas (https://github.com/pandas-dev/pandas)
