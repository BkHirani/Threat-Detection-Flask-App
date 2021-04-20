import os
import requests
from app import *
from functools import wraps
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (render_template, url_for, request, redirect,flash)
from werkzeug.utils import secure_filename
import pandas as pd
from datetime import datetime
import csv
from app.core_logic import *

ALLOWED_EXTENSIONS = ['jpg','xml','png']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_logs',methods=['GET', 'POST'])
def show_log():
    images = []
    if request.method == 'POST':
        sdt = datetime.fromisoformat(request.form['start_date']+' 00:00:00')
        edt = datetime.fromisoformat(request.form['end_date']+' 23:59:59')
        # images = Image.query.filter(Image.timestamp>=sdt).filter(Image.timestamp <=edt).all()
        images = Image.query.with_entities(Image.name,Object.name,Object.x_min,Object.y_min,Object.x_max,Object.y_max,Image.timestamp).join(Object, Image.id==Object.image_id).filter(Image.timestamp>=sdt).filter(Image.timestamp <=edt).all()
        return render_template('show_logs.html',data=images)    

    images = Image.query.with_entities(Image.name,Object.name,Object.x_min,Object.y_min,Object.x_max,Object.y_max,Image.timestamp).join(Object, Image.id==Object.image_id).all()
    return render_template('show_logs.html',data=images)    

@app.route('/upload_files',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img_file' not in request.files or 'xml_file' not in request.files:
            flash('No file part')
            return render_template('upload_files.html',success=0,msg='No File Found!')
        img_file = request.files['img_file']
        xml_file = request.files['xml_file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if img_file.filename == '' or xml_file.filename == '':
            flash('No selected file')
            return render_template('upload_files.html',success=0,msg='Please select file!',)
        if (img_file and allowed_file(img_file.filename)) and (xml_file and allowed_file(xml_file.filename)):
            img_filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img_file.filename))
            img_file.save(img_filepath)
            
            xml_filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(xml_file.filename))
            xml_file.save(xml_filepath)

            data = parseXML(xml_filepath)
            print(data)
            img = draw_rectangles(img_filepath, data)
            img_b64 = convert_to_base64(img)

            new_image = Image(name=secure_filename(img_file.filename), timestamp = datetime.now())
            db.session.add(new_image)
            db.session.commit()
            img_id = new_image.id

            for o in data['objects']:
                ovj = Object(name=o['name'], x_min=o['xmin'], y_min=o['ymin'], x_max=o['xmax'], y_max=o['ymax'],image_id = img_id)
                print(ovj)
                db.session.add(ovj)

            db.session.commit()
            return render_template('upload_files.html',success=1,msg='Objects Detected Successfully!',img_b64=img_b64)
    return render_template('upload_files.html')


    