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
    urls = ['cmu_us_awb_arctic-0.95-release.tar.bz2',
            'cmu_us_bdl_arctic-0.95-release.tar.bz2',
            'cmu_us_clb_arctic-0.95-release.tar.bz2',
            'cmu_us_jmk_arctic-0.95-release.tar.bz2',
            'cmu_us_ksp_arctic-0.95-release.tar.bz2',
            'cmu_us_rms_arctic-0.95-release.tar.bz2',
            'cmu_us_slt_arctic-0.95-release.tar.bz2',]

    # directory
    try:
        root = os.path.join(sys.argv[1], 'CMU_ARCTIC/')
    except:
        root = './CMU_ARCTIC/'

    if not os.path.exists(root):
        os.makedirs(root)

    # download
    for i, url in enumerate(urls):
        path = os.path.join(root, url)
        print('{}/{} downloading {}'.format(i + 1, len(urls), url))
        if not os.path.exists(path):
            download_file(os.path.join('http://festvox.org/cmu_arctic/cmu_arctic/packed/', url), path)

    # unzip
    for i, url in enumerate(urls):
        print('{}/{} unzipping {}'.format(i + 1, len(urls), url))
        try:
            subprocess.call([
                'tar', 'jxvf', os.path.join(root, url), '-C', root])
        except:
            print('can\'t unzip {}'.format(url))
