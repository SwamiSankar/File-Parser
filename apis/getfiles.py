from flask.json import jsonify
from flask import Blueprint
import glob
import os


getfiles = Blueprint('getfiles', __name__,
                     static_folder='static', template_folder='templates')

# API to fetch the files


@getfiles.route('/getFiles')
def getFiles():

    formated_files = []

    # Retrieve csv files present inside the Files folder
    try:
        files = (glob.glob(os.getenv('FILE_PATH')))
        for file in files:
            formated_files.append(file.replace(
                os.getenv('FILE_PATH_REDUCED'), ''))

    except:
        return 'NO Files Found', 400

    # Returning list of files into JSON format
    return jsonify(formated_files)
