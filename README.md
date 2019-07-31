# Clone the repository from github
`git clone https://github.com/AmberDee/text-classifier.git`  

# Install the needed packages in order to create the classifier

`cd text-classifier`

`pip install .`

# Create a virtual enviroment to start the flask app
#### For reference https://flask.palletsprojects.com/en/1.1.x/installation/#install-create-env
## For Mac:
`$ mkdir myproject`

$ cd myproject
## For Windows
`$ python3 -m venv venv`

# Activate env:
## For Mac
`$. venv/bin/activate`

## For Windows
`> py -3 -m venv venv`
`> venv\Scripts\activate`

# Setup the enviroment

`$ pip3 install -r requirements.txt`

# Start the flask app
#### For reference https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

## For Mac
`$ export FLASK_APP=near-relevance`  

`$ export FLASK_ENV=development`  

`$ flask run`

## For Windows
`> $env:FLASK_APP = "near-relevance"`  

`> $env:FLASK_ENV = "development"`  

`> flask run`

##For the command line application

`cd cmd_line`

##to run, model values are ulmfit, logistic or xgboost
# pass in headline in double quotes


`python get_prediction.py --model=[model] --headline=["headline text"]`

#example

`python get_prediction.py --model=ulmfit --headline="stock market is down"`
