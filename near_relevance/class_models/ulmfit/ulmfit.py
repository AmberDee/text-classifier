import fastai
from fastai import *
from fastai.text import *

def ulmfit_classify(text):
    learn = load_learner('models')
    return learn.predict(text)[0]
