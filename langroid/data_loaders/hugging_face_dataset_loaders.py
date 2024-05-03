import time

import requests


def download_from_hugging_face(offset=0, dataset_name="nvidia/HelpSteer"):
    url = "https://datasets-server.huggingface.co/rows"

    params = {  # parametrized
        "dataset": dataset_name,
        "config": "default",
        "split": "train",
        "offset": str(offset),
        "length": "100"
    }

    response = requests.get(url, params=params)

    time.sleep(0.3)
    if response.status_code == 200:
        return response.json()
        # print(help_steer_data)
    else:
        print(response.content)
        print("Error:", response.status_code)
        raise ValueError(response.status_code)


def post_process_hugging_face(result):
    """
    Not generic enough, perhaps you need to provide the schema coming from response object
    :param result:
    :return:
    """
    dataset = []

    for l in result:
        dataset.extend([row['row']['prompt'] + "<sep>" + row['row']['response'] for row in l['rows']])

    return dataset
