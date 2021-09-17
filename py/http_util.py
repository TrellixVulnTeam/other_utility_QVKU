
import urllib.request
import shutil
import json
import yaml

def download_file_from_url(filename, url):
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)



def request_get_json(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        #result = data.decode('utf8')
        return json.loads(data)


def request_get_yaml(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        result = data.decode('utf8')
        return yaml.load(result, Loader=yaml.FullLoader)
        


def request_get_text(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return data.decode('utf8')


def request_get_exist(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return True
            else:
                print("warning ", response.status)
                return False
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print("error ", e.code)

        return False
