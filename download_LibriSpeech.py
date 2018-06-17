import os
import sys
import subprocess

from utils import download_file

# url and path
urls = ['dev-clean.tar.gz',
        'dev-other.tar.gz',
        'test-clean.tar.gz',
        'test-other.tar.gz',
        'train-clean-100.tar.gz',
        'train-clean-360.tar.gz',
        'train-other-500.tar.gz',
        'intro-disclaimers.tar.gz',
        'original-books.tar.gz',
        'raw-metadata.tar.gz']

# directory
try:
    root = os.path.join(sys.argv[1], 'LibriSpeech/')
except:
    root = './LibriSpeech/'

if not os.path.exists(root):
    os.makedirs(root)

# download
for i, url in enumerate(urls):
    path = os.path.join(root, url)
    print('{}/{} downloading {}'.format(i + 1, len(urls), url))
    print(path)
    if not os.path.exists(path):
        download_file(os.path.join(
            'http://www.openslr.org/resources/12', url), path)
    else:
        print('exist')

# unzip
for i, url in enumerate(urls):
    print('{}/{} unzipping {}'.format(i + 1, len(urls), url))
    try:
        subprocess.call([
            'tar', 'zxvf', os.path.join(root, url), '-C',
            os.path.dirname(os.path.dirname(root))])
    except:
        print('can\'t unzip {}'.format(url))
