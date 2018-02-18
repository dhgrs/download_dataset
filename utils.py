import requests


def download_file(url, path):
    session = requests.Session()

    response = session.get(url, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': fileid, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, path)


def download_file_from_google_drive(fileid, path):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': fileid}, stream=True)
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
