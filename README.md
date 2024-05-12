<br />
<div align="center">


  <h3 align="center">Gora ML Liquidity Analytics and Preduction</h3>

  <p align="center">
    <!--Gora ML Liquidity Analytics and Preduction-->
    <!--<br />-->
    <a href="https://github.com/Hrishikesh332/Liquidity-Analytics-and-Prediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Hrishikesh332/Liquidity-Analytics-and-Prediction">View Demo</a>
    ·
    <a href="https://github.com/Hrishikesh332/Liquidity-Analytics-and-Prediction/issues">Report Bug</a>
    ·
    <a href="https://github.com/Hrishikesh332/Liquidity-Analytics-and-Prediction/issues">Request Feature</a>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About">About</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Tech-Stack">Tech Stack</a></li>
    <li><a href="#Languages-and-Tools">Languages and Tools</a></li>
    <li><a href="#Workflow">Workflow</a></li>
    <li><a href="#Instructions-on-running-project-locally">Instructions on running project locally</a></li>
    <li><a href="#Feedback">Feedback</a></li>
  </ol>
</details>

------

## Overview
The GoraxGiz ML Competition aims to build models that predict the likelihood and ratio of individual liquidations in comparison to the amount borrowed (`total_liquidation_to_total_borrow`). This competition utilizes DeFi transaction history and behavior data from various lending protocols and chains.

## Structure of the Repository

```

Liquidity-Analytics-and-Prediction/
├── notebook/
│   ├── Analytics_EDA/
│   └── Prediction/
│   
├── models/
│   ├── liquidity_prediction.pkl
│   
├── test/
│   ├── test_script.py
│   └── liquidity_prediction.csv
│  
├── src/
│   ├── UML_prediction.png
│ 


```
## Data Collection
The dataset includes wallet transaction history (borrow, lend, etc.) from the following lending protocols and chains -

### Lending Protocols
- Aave
- Compound
- Cream
- RociFi
- Venus
- MakerDAO
- GMX
- Radiant

### Chains
- Ethereum (full transaction history)
- Arbitrum (protocol-specific history)
- Fantom (protocol-specific history)
- Polygon (protocol-specific history)
- Optimism (protocol-specific history)
- BSC (protocol-specific history)
- Avalanche (protocol-specific history)

The Historical token prices for conversion to USDT at the transaction time are included.

## Loading the Dataset
To load the dataset, follow these steps -

1. Install the `giza-datasets` package (version 0.2.2).
2. In your Python environment, instantiate a `DatasetsLoader` object and load the "gora-competition-training" dataset:

```python
import certifi
import os
os.environ['SSL-CERT_FILE'] = certifi.where()
from giza_datasets import DatasetsLoader

loader = DatasetsLoader
df = loader.load("gora-competition-training")

```
3. It supports the python version higher than or equal to 3.11, so it would be difficult to run in Google Colab or GCP Colab Enterprise.
4. Installation of the giza-datasets module is necessary

```bash
pip install giza-datasets

```
5. The provided notebook is made as per downloading the data from the giza and then making use of it by mounting it with the google drive for the ease of connection with google colab.


## Pipeline Workflow

The following diagram illustrates the workflow of the pipeline -

![Pipeline Workflow](https://github.com/Hrishikesh332/Liquidity-Analytics-and-Prediction/blob/main/src/UML_Approach.png)

The pipeline consists of the following steps:

1. Loading and Analysis of the Dataset Provided
2. To convert the categorical columns into numericals one to prepare it for training.
3. Train multiple regression models using different algorithms and techniques - Decision Tree Regression, Random Forest Regression, Gradient Boosting Regression, Support Vector Regression, XGBoost Regression, LightGBM Regression, CatBoost Regression
4. Perform hyperparameter tuning on each model using techniques like GridSearchCV.
5. Combine the tuned models using a Stacking Regressor approach which provides the robust result.
6. Evaluate the performance of the Stacking Regressor on the test data with the mean square error.

## Test Data and the Evaluation

The Test Data is taken from the `gora-competition-evaluation` which contains all the feature column except the target column, the prediction prepared is attached in the repository as `liquidity_prediction.csv`. 

The test script is also prepared to utilize the model developed and can be tested on the featured present and relevant as per the training dataset.

## Feedback

If you have any feedback, please reach out to us at **hriskikesh.yadav332@gmail.com**



## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

