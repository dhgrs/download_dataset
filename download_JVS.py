import os
import sys
import subprocess

from utils import download_file_from_google_drive


# url and path
google_drive_id = "19oAw8wWn3Y7z6CKChRdAyGOB9yupL_Xt"

# directory
try:
    root = os.path.join(sys.argv[1], 'jsv_ver1/')
except:
    root = './vsj_ver1/'

if not os.path.exists(root):
    os.makedirs(root)

# download
download_file_from_google_drive(google_drive_id, os.path.join(root, "jvs_ver1.zip"))

# unzip
try:
    subprocess.call([
        'unzip', os.path.join(root, 'jvs_ver1.zip'), '-d', root])
except:
    print('can\'t unzip jvs_ver1.zip')
