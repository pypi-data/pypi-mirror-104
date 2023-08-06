# NoisyDataCleaner
Python classes that identify and correct/remove noise in datasets

These models leverage on monte carlo simulation to approximate the correctness of a given label. The correction of the label builds on from the noise detection model. 

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-brightgreen?style=plastic&logo=appveyor"/></a>
  <a href="https://pypi.org/project/noisydatacleaner/"><img src="https://img.shields.io/pypi/v/noisydatacleaner?style=plastic"/></a>
  <a href="https://pypi.org/project/noisydatacleaner/"><img src="https://img.shields.io/pypi/pyversions/noisydatacleaner?style=plastic"/></a>
</p>

## Install:
```bash
pip install noisydatacleaner
```

## Models: 

1. NoiseRemover
Identifies and then removes the noise from the dataset. Random Forest is used for smaller datasets as it yields better results. Whereas for larger datasets, k-Nearest Neighbors is much more efficient.

2. LabelClassificationCorrector
Corrects the labels for classification datasets. Instead of only using 1 model like `NoiseRemover`, this model uses 5 different models:
```python
models = {
   'Random Forest': RandomForestClassifier(n_estimators=128),
   'Extra Trees': ExtraTreesClassifier(n_estimators=128),
   'Linear Discriminant': LinearDiscriminantAnalysis(),
   'Logistic Regression': LogisticRegression(max_iter=128),
   'Neural Network': MLPClassifier(hidden_layer_sizes=(128,64,32))
}
```
All of which comes from the sklearn library