import base64
from urllib.parse import urlencode

import pytest
from playwright.sync_api import sync_playwright

from utils import config_reader as cr
from utils.loggers import get_loggers

logger = get_loggers(__name__)
api_details = cr.get_api_details()


@pytest.fixture(scope="session")
def generate_api_token():
    try:
        with sync_playwright() as p:
            api_request_context = p.request.new_context(
                ignore_https_errors=api_details["ignore_https_errors"]
            )

            headers = {
                "Referer": api_details["referer"],
                "Content-Type": api_details["content_type"],
            }

            raw_token = (
                f"{api_details['consumer_key']}:{api_details['consumer_secret']}"
            )
            encoded_token = base64.b64encode(raw_token.encode()).decode()
            headers["Authorization"] = f"Basic {encoded_token}"

            data = {
                "grant_type": api_details["grant_type"],
                "username": api_details["username"],
                "password": api_details["encrypt_password"],
            }
            encode_data = urlencode(data)
            response = api_request_context.post(
                cr.get_api_url("post_login"),
                headers=headers,
                data=encode_data,
            )

            if not response.ok:
                raise Exception(
                    f"API token request failed with status {response.status}: {response.text()}"
                )

            json_data = response.json()
            access_token = json_data.get("access_token")

            if not access_token:
                raise KeyError("Access token not found in response")

            logger.info("Access token generated successfully")
            return access_token

    except Exception as e:
        logger.error(f"Token generation failed: {str(e)}")
        pytest.fail(f"Fixture 'generate_api_token' failed: {str(e)}")
