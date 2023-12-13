import requests
import fire
import os


def main(
    url="https://deso-scb.gentlesky-8e5d1207.westus2.azurecontainerapps.io/",
    data={"deso": "0114A0010"},
):
    url = os.path.join(url, "get-deso-data")
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


if __name__ == "__main__":
    fire.Fire(main)
