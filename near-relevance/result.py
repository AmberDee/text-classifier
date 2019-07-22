from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .class_models import predict as mdl

from .class_models.predictors import *

from .db import get_db

bp = Blueprint('result', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, u.model_name, generated, input_text, result'
        ' FROM model_result p JOIN model u ON p.model_id = u.id'
        ' ORDER BY generated DESC'
    ).fetchall()

#@bp.route('/create', methods=('GET', 'POST'))
#def create():
    db = get_db()
    models = db.execute(
        'SELECT id, model_name'
        ' FROM model'
        ' ORDER BY id ASC'
        ).fetchall()
    
    if request.method == 'POST': 
        model = request.form['model']
        headline = request.form['headline']
        error = None

        if not model:   
            error = 'Model is required.'
        
        result = mdl.get_result(model, headline)  

        modelid = db.execute(
            'SELECT id'
            ' FROM model '
            'WHERE model_name = ?',
            (model,)
            ).fetchone()      

        if not headline:
            error = 'Headline is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO model_result (model_id, input_text, result)'
                ' VALUES (?, ?, ?)',
                (int(modelid['id']), headline, str(result))
            )
            db.commit()
            return redirect(url_for('result.index'))
    return render_template('result/index.html', models=models, posts=posts)

@bp.route('/clear_results', methods=('POST',))
def clear_results():
    db = get_db()
    db.execute('DELETE FROM model_result')
    db.commit()
    return redirect(url_for('result.index'))
