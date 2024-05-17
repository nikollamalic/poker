import os
import logging
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

API_URL = os.getenv("API_URL")
METHOD = os.getenv("METHOD")


def send_get_request(url, method="GET"):
    try:
        logger.info(f"POST request to {url}")
        response = requests.request(method, url)
        logger.info(f"Success: {response.ok}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")


if __name__ == "__main__":
    send_get_request(API_URL, METHOD or "GET")
