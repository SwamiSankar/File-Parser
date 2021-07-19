import os
current_working_directory = os.getcwd()
os.environ['FILE_PATH'] = '{}/Files/*csv'.format(current_working_directory)
os.environ['FILE_PATH_REDUCED'] = "{}/Files/".format(current_working_directory)
