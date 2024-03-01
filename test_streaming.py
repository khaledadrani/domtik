import time

import requests

from source.schema.api_schema import SimpleLLMRequest
from source.schema.common_schema import SupportedLLModelsEnum

request_body = SimpleLLMRequest(
    prompt="What is Python?",
    llm_type=SupportedLLModelsEnum.GPT_4ALL,
    params=None  # Optional parameters if needed
)


def stream_response(url):
    with requests.post(url, json=request_body.model_dump(), stream=True) as response:
        try:
            for chunk in response.iter_content(chunk_size=64):
                print(f"|{chunk.decode('utf-8')}|")
                # print(chunk.decode('utf-8'), end="")
                time.sleep(0.15)# Assuming UTF-8 encoding
        except requests.exceptions.RequestException as e:
            print("Error:", e)


if __name__ == "__main__":
    stream_url = "http://localhost:8000/llm/stream"  # Replace with your streaming endpoint
    stream_response(stream_url)