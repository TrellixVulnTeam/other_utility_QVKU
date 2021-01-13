
import urllib.request
import shutil

def download_file_from_url(filename, url):
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)