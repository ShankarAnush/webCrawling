import os
from distutils.file_util import write_file


# create_project_dir ----> function call to create a project directory
def create_project_dir(directory):  # Each website crawled is put into a separate folder
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# create queue and crawled files (if doesn't exist already)
def create_data_files(folder_name):
    file = os.path.join(folder_name + '/' + folder_name + '.csv')
    print(file)
    if not os.path.isfile(file):
        write_file(file, '')
    # crawled = os.path.join(project_name + '/crawled.csv')
