# Bank Note Authentication and Deployment using Flask, Swagger and Docker

Determine whether a bank note is authentic or forged.

#### Data Set Information

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

source: https://archive.ics.uci.edu/ml/datasets/banknote+authentication

#### Attribute Information

1. variance of Wavelet Transformed image (continuous)
2. skewness of Wavelet Transformed image (continuous)
3. curtosis of Wavelet Transformed image (continuous)
4. entropy of image (continuous)
5. class (integer)

#### Classification Model Building
Built a classifcation model to predict whether a given curreny bill is fake(1) or real(0) based on the input values of variance, skewedness, kurtosis, entropy. Implemeted the model using Random Forests and achieved an accuracy rate of 99%. 

#### Deployment

##### using Flask
Created a pickle file (classifier.pkl) of the model to use it in a Flask App. Deployed the model using Flask where a user can run it on localhost using get and post requests. User can either give values to autheticate a bill or upload a file on PostMan consisting of records to be classified.

##### using Flasgger
In order to further improve the front-end user interface, used Swagger from Flasgger to create a proper front end api for model deployment

##### using Docker
Deployed the app by giving the requirements in the dockerfile to access the app through Docker



