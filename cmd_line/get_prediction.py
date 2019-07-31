import argparse
from class_models.predict import *
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Get Relevance Prediction for a headline')
parser.add_argument('--model', type=str, help='ulmfit, logistic, or xgboost')
parser.add_argument('--headline', type=str, help='headline to classify in "double quotes"')

args = parser.parse_args()

if args.model == "ulmfit" or args.model == "xgboost":
    print(get_result(args.model, args.headline))
elif args.model == "logistic":
    print(get_result("logistic_regression", args.headline))
else:
    print("Please choose an acceptable model name: ulmfit, logistic, or xgboost")