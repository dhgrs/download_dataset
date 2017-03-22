import requests
import os
import sys
import subprocess


def download_file(url, path):
    session = requests.Session()

    response = session.get(url, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': fileid, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, path)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, path):
    CHUNK_SIZE = 32768

    with open(path, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
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
