from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flaskr.classes.image_recognized import ImageRecognized
from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.__init__ import create_app
#from flask import current_app
from flask import jsonify
import os


bp = Blueprint('upload', __name__)

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
        print(1)
        if 'files[]' not in request.files:
            return flash('No file part')
        print(2)
        files = request.files.getlist('files[]')
        print(3)
        photo_id = 0
        results = {}

        for file in files:
            if file and allowed_file(file.filename):
                print(4)
                filename = secure_filename(file.filename)
                print(5)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(6)
                photo = app.config['UPLOAD_FOLDER'] + "/" + filename
                print(7)
                photo_res = ImageRecognized.image_recognized(photo)
                print(8)
                os.remove(app.config['UPLOAD_FOLDER'] + "/" + filename)
                print(9)
                photo_id = photo_id +1
                print(10)
                photo_id_st = str(photo_id)
                print(11)
                results["Photo" + photo_id_st] = photo_res
                print(12)
            else:
                results = "Error"
                return render_template("upload/landing_page.html", results= results)
        #pippo = jsonify(results)   
        #print(pippo)
        return render_template("upload/landing_page.html", results= results)

    return render_template('upload/landing_page.html')
    

    
