import os
import sys
import subprocess

from utils import download_file

# url and path
urls = ['https://www.westernsydney.edu.au/__data/assets/text_file/0019/'
        '1204408/EMNIST_Readme.txt',
        'https://cloudstor.aarnet.edu.au/plus/index.php/s/54h3OuGJhFLwAlQ/'
        'download']

paths = ['Readme.txt', 'gzip.zip']

# directory
try:
    root = os.path.join(sys.argv[1], 'EMNIST/')
except:
    root = './EMNIST/'

if not os.path.exists(root):
    os.makedirs(root)

# download
for i, (url, path) in enumerate(zip(urls, paths)):
    print('{}/{} downloading {}'.format(i + 1, len(urls), path))
    path = os.path.join(root, path)
    if not os.path.exists(path):
        download_file(url, path)

# unzip
try:
    subprocess.call([
        'unzip', os.path.join(root, 'gzip.zip'), '-d', root])
except:
    print('can\'t unzip gzip.zip')
