import os
import sys
import subprocess

from utils import download_file

# url and path
urls = ['tsuchiya_normal.tar.gz',
        'tsuchiya_happy.tar.gz',
        'tsuchiya_angry.tar.gz',
        'uemura_normal.tar.gz',
        'uemura_happy.tar.gz',
        'uemura_angry.tar.gz',
        'fujitou_normal.tar.gz',
        'fujitou_happy.tar.gz',
        'fujitou_angry.tar.gz']

# directory
try:
    root = os.path.join(sys.argv[1], 'voice_statistics/')
except:
    root = './voice_statistics/'

if not os.path.exists(root):
    os.makedirs(root)

# download
for i, url in enumerate(urls):
    path = os.path.join(root, url)
    print('{}/{} downloading {}'.format(i + 1, len(urls), url))
    if not os.path.exists(path):
        download_file(os.path.join(
            'https://github.com/voice-statistics/'
            'voice-statistics.github.com/raw/master/assets/data/', url), path)

# unzip
for i, url in enumerate(urls):
    print('{}/{} unzipping {}'.format(i + 1, len(urls), url))
    try:
        print(os.path.join(root, url))
        subprocess.call([
            'tar', 'zxvf', os.path.join(root, url), '-C', root])
    except:
        print('can\'t unzip {}'.format(url))
