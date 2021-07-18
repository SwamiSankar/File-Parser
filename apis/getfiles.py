from flask.json import jsonify
from flask import Blueprint
import glob
import os
from utils.util import FILE_DIR, FILE_DIR_REDUCED

getfiles = Blueprint('getfiles', __name__,
                     static_folder='static', template_folder='templates')

# API to fetch the files


@getfiles.route('/getFiles')
def getFiles():

    formated_files = []

    # Retrieve csv files present inside the Files folder
    try:
        files = (glob.glob(FILE_DIR))
        for file in files:
            formated_files.append(file.replace(
                FILE_DIR_REDUCED, ''))

    except:
        return 'NO Files Found', 400

    print(formated_files)

    # Returning list of files into JSON format
    return jsonify(formated_files)
