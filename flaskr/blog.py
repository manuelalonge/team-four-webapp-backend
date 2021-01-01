from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flaskr.classes.image_recognized import ImageRecognized
from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.__init__ import create_app
import os


bp = Blueprint('blog', __name__)

app = create_app()
UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload_file():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return flash('No file part')
        files = request.files.getlist('files[]')
        photo_id = 0
        results = {}
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo = app.config['UPLOAD_FOLDER'] + "/" + filename
                photo_res = ImageRecognized.image_recognized(photo)
                os.remove(app.config['UPLOAD_FOLDER'] + "/" + filename)
                photo_id = photo_id +1
                photo_id_st = str(photo_id)
                results["Photo" + photo_id_st] = photo_res
            else:
                return flash("errore")
        return render_template('blog/upload.html', value=results)
    return render_template('blog/upload.html')
    
    
