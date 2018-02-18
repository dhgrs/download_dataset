import os
import sys
import subprocess

from utils import download_file_from_google_drive

# id and path
readme_ids = [
    '0B7EVK8r0v71pOXBhSUdJWU1MYUk']
readme_paths = [
    'README.txt']

annotation_ids = [
    '0B7EVK8r0v71pbThiMVRxWXZ4dU0',
    '0B7EVK8r0v71pblRyaVFSWGxPY0U',
    '0B7EVK8r0v71pd0FJY3Blby1HUTQ',
    '0B7EVK8r0v71pTzJIdlJWdHczRlU']
annotation_paths = [
    'Anno/list_bbox_celeba.txt',
    'Anno/list_attr_celeba.txt',
    'Anno/list_landmarks_align_celeba.txt',
    'Anno/list_landmarks_celeba.txt']

eval_ids = [
    '0B7EVK8r0v71pY0NSMzRuSXJEVkk']
eval_paths = [
    'Eval/list_eval_partition.txt']

img_celeba_ids = [
    '0B7EVK8r0v71pQy1YUGtHeUM2dUE',
    '0B7EVK8r0v71peFphOHpxODd5SjQ',
    '0B7EVK8r0v71pMk5FeXRlOXcxVVU',
    '0B7EVK8r0v71peXc4WldxZGFUbk0',
    '0B7EVK8r0v71pMktaV1hjZUJhLWM',
    '0B7EVK8r0v71pbWFfbGRDOVZxOUU',
    '0B7EVK8r0v71pQlZrOENSOUhkQ3c',
    '0B7EVK8r0v71pLVltX2F6dzVwT0E',
    '0B7EVK8r0v71pVlg5SmtLa1ZiU0k',
    '0B7EVK8r0v71pa09rcFF4THRmSFU',
    '0B7EVK8r0v71pNU9BZVBEMF9KN28',
    '0B7EVK8r0v71pTVd3R2NpQ0FHaGM',
    '0B7EVK8r0v71paXBad2lfSzlzSlk',
    '0B7EVK8r0v71pcTFwT1VFZzkzZk0']
img_celeba_paths = [
    'Img/img_celeba/img_celeba.7z.001',
    'Img/img_celeba/img_celeba.7z.002',
    'Img/img_celeba/img_celeba.7z.003',
    'Img/img_celeba/img_celeba.7z.004',
    'Img/img_celeba/img_celeba.7z.005',
    'Img/img_celeba/img_celeba.7z.006',
    'Img/img_celeba/img_celeba.7z.007',
    'Img/img_celeba/img_celeba.7z.008',
    'Img/img_celeba/img_celeba.7z.009',
    'Img/img_celeba/img_celeba.7z.010',
    'Img/img_celeba/img_celeba.7z.011',
    'Img/img_celeba/img_celeba.7z.012',
    'Img/img_celeba/img_celeba.7z.013',
    'Img/img_celeba/img_celeba.7z.014']

img_align_celeba_png_ids = [
    '0B7EVK8r0v71pSVd0ZjQ3Sks2dzg',
    '0B7EVK8r0v71pR2NwRnU2cVZ2RTg',
    '0B7EVK8r0v71peUlHSDVhd0JTamM',
    '0B7EVK8r0v71pVmYwbmRtV2hZcDA',
    '0B7EVK8r0v71pVjRlNVB3cDVjaDQ',
    '0B7EVK8r0v71pa3NIcEgtTXZrM0U',
    '0B7EVK8r0v71pNE5aQmY5c2ZLOXc',
    '0B7EVK8r0v71pejhuem9QV2h0MDQ',
    '0B7EVK8r0v71pZk5QcUlObVltaEE',
    '0B7EVK8r0v71pLThPNzFETUNMUVE',
    '0B7EVK8r0v71pZWZ4UGdBbk9UVWs',
    '0B7EVK8r0v71pSk1zVWN2aHhMZ3c',
    '0B7EVK8r0v71pNjFfTGYzTWJDdUU',
    '0B7EVK8r0v71pbFlZaURkY3dhWWM',
    '0B7EVK8r0v71pczZ0NFNFdFRXSUU',
    '0B7EVK8r0v71pckZsdFFIYlJoN1k']
img_align_celeba_png_paths = [
    'Img/img_align_celeba_png/img_align_celeba_png.7z.001',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.002',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.003',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.004',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.005',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.006',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.007',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.008',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.009',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.010',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.011',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.012',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.013',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.014',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.015',
    'Img/img_align_celeba_png/img_align_celeba_png.7z.016']

ids = readme_ids + annotation_ids + eval_ids +\
    img_celeba_ids + img_align_celeba_png_ids

paths = readme_paths + annotation_paths + eval_paths +\
    img_celeba_paths + img_align_celeba_png_paths

# directory
try:
    root = os.path.join(sys.argv[1], 'CelebA/')
except:
    root = './CelebA/'
Img_img_celeba = os.path.join(root, 'Img/img_celeba')
Img_img_align_celeba_png = os.path.join(root, 'Img/img_align_celeba_png')
Anno = os.path.join(root, 'Anno')
Eval = os.path.join(root, 'Eval')

if not os.path.exists(Img_img_celeba):
    os.makedirs(Img_img_celeba)

if not os.path.exists(Img_img_align_celeba_png):
    os.makedirs(Img_img_align_celeba_png)

if not os.path.exists(Anno):
    os.makedirs(Anno)

if not os.path.exists(Eval):
    os.makedirs(Eval)

# download
for i, (fileid, path) in enumerate(zip(ids, paths)):
    print('{}/{} downloading {}'.format(i + 1, len(ids), path))
    path = os.path.join(root, path)
    if not os.path.exists(path):
        download_file_from_google_drive(fileid, path)

# unzip
try:
    subprocess.call([
        '7z', 'x', '-o' + os.path.relpath(os.path.join(root, 'Img')),
        os.path.join(Img_img_celeba, 'img_celeba.7z.*')])
except:
    print('can\'t unzip img_celeba')

try:
    subprocess.call([
        '7z', 'x', '-o' + os.path.relpath(os.path.join(root, 'Img')),
        os.path.join(Img_img_align_celeba_png,
                     'img_align_celeba_png.7z.*')])
except:
    print('can\'t unzip img_align_celeba_png')
