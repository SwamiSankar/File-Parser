import os
current_working_directory = os.getcwd()
os.environ['FILE_PATH'] = '{}/File-Parser/Files/*csv'.format(
    current_working_directory)
os.environ['FILE_PATH_REDUCED'] = "{}/File-Parser/Files/".format(
    current_working_directory)
