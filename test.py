import requests
import fire
import os


def main(
    url="http://deso-scb.graygrass-fb2be12d.westus2.azurecontainerapps.io",
    data={"deso": "0114A0010"},
):
    url = os.path.join(url, "send-data/")
    print("URL:", url)
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


if __name__ == "__main__":
    fire.Fire(main)
