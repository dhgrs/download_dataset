import os
import sys
import subprocess

from utils import download_file

# url and path
url = 'https://datashare.is.ed.ac.uk/bitstream/handle/10283/2651/' \
    'VCTK-Corpus.zip?sequence=2&isAllowed=y'

# directory
try:
    root = sys.argv[1]
except:
    root = './'

if not os.path.exists(root):
    os.makedirs(root)

# download
print('downloading')
path = os.path.join(root, 'VCTK-Corpus.zip')
if not os.path.exists(path):
    download_file(url, path)

# unzip
print('unzipping')
try:
    subprocess.call(['unzip', path, '-d', root])
except:
    print('can\'t unzip {}'.format(url))
