# Model Card
Jesse Kukuk developed this model for the WGU/Udacity Machine Learning DevOps course. It employs the scikit-learn RandomForestClassifier model with its default hyperparameters.

## Model Details


## Intended Use
This model aims to predict an individual's salary range using attributes from their census data.
## Training Data
#### The course provided the data file "census.csv," comprising 32,561 rows of census data organized into 15 columns:
* Sex
* Capital-gain
* Capital-loss
* Salary
* Age
* Workclass
* Fnlgt
* Education
* Education-num
* Marital-status
* Occupation
* Relationship
* Race
* Hours-per-week
* Native-country

#### Afterwards, the data underwent cleaning, which involved:

* Normalizing the education column
* Removing records with missing workclass or occupation information
* Eliminating records with an unknown native-country.
    
## Evaluation Data
20% of the dataset was set aside for the purpose of testing and evaluating the trained model.

## Metrics
Precision, Recall, and F1 scores were utilized to evaluate the model. The obtained results were:
* F1: 0.6830
* Precision: 0.7297
* Recall: 0.6420

## Ethical Considerations
Further investigation is required to uncover potential biases within the dataset and to verify that all incorporated features effectively represent the broader population. It's important to note that the training data, while valuable, might not comprehensively mirror every demographic segment within the population. This indicates the necessity for additional measures to enhance the dataset's representativeness and address any underlying biases.

## Caveats and Recommendations
