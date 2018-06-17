import os
import sys
import subprocess

from utils import download_file

# url and path
url = 'http://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2'

# directory
try:
    root = sys.argv[1]
except:
    root = './'

if not os.path.exists(root):
    os.makedirs(root)

# download
print('downloading')
path = os.path.join(root, 'LJSpeech-1.1.tar.bz2')
if not os.path.exists(path):
    download_file(url, path)

# unzip
print('unzipping')
try:
    subprocess.call(['tar', 'xvf', path, '-C', root])
except:
    print('can\'t unzip {}'.format(url))
