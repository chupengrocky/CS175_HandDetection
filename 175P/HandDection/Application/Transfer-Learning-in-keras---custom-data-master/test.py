import os
PATH = os.getcwd()
# Define data path
data_path = PATH + '/data/hand2'
data_dir_list = [f for f in os.listdir(data_path) if not f.startswith('.')]
print (data_dir_list)
