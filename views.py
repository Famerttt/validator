from app_flask import app
from flask import jsonify, request, abort
from modelValidation import ModelValidation
import logging
from werkzeug.utils import secure_filename
import os
from DataValidation import Data_validation

logging.basicConfig(filename="sample.log", level=logging.DEBUG)


@app.route('/validation', methods=['POST'])
def new_validator():
    file = request.files['file']
    if not file:
        abort(400)
    home_path = os.getcwd()

    try:
        if file:
            filename = secure_filename(file.filename)
            file.save(home_path + '/' + filename)
    except:
        abort(500)

    try:
        target_name = request.form['targetName']
    except:
        target_name = None

    try:
        error_code = request.form['errorCode']

    except:
        error_code = None

    obj = ModelValidation(home_path + '/' + filename, target_name, error_code)
    validator = Data_validation(obj)
    validation_status, message = validator.full_validation()
    result = {'validationStatus': validation_status, "error_message": message}
    os.remove(home_path + '/' + filename)

    return jsonify(result), 200
