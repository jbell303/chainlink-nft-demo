from brownie import config
import requests, os
from pathlib import Path

PINATA_BASE_URL = 'https://api.pinata.cloud'
endpoint = '/pinning/pinFileToIPFS'
base_dir = "./img/"
# filepath = "./img/pug.png"
# filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": config["pinata"]["api-key"],
    "pinata_secret_api_key": config["pinata"]["api-secret"]
}

def upload_to_pinata():

    for filename in os.listdir(base_dir):
        filepath = base_dir + filename
        with Path(filepath).open("rb") as fp:
            image_binary = fp.read()
            # upload to pinata
            response = requests.post(
                PINATA_BASE_URL + endpoint, 
                files={"file": (filename, image_binary)}, 
                headers=headers,
            )
            print(response.json())

def main():
    upload_to_pinata()