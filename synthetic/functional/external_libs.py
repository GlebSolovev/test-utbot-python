from typing import List

import numpy as np
import requests
from requests import Response, HTTPError


def avg_without_annotations(arr):
    return np.sum(arr) / len(arr)


def avg(arr: np.ndarray) -> float:
    return np.sum(arr) / len(arr)


def add_ones(arr: np.ndarray) -> np.ndarray:
    return arr + np.ones(arr.shape)


def request_ok_github() -> int:
    return requests.get('https://api.github.com').status_code


def request_different_github() -> List[Response]:
    responses = []
    for url in ['https://api.github.com/invalid', 'https://api.github.com']:
        try:
            response = requests.get(url)
            response.raise_for_status()
            responses.append(response)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
    return responses
