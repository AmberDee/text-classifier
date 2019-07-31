from .ulmfit import ulmfit
from .sk_models import *

def get_result(model, headline):
    
    prediction = -1

    if model == 'ulmfit':
        prediction = ulmfit.ulmfit_classify(headline)
    elif model == 'logistic_regression':
        prediction = logistic_classify(headline)
    elif model == 'xgboost':
        prediction = xgboost_classify(headline)

    return 'R' if int(prediction) == 1 else 'IR'