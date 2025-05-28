import os

import yaml

# Load config.yaml from /config directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(base_dir, "config", "config.yaml")
with open(config_path, "r") as file:
    CONFIG = yaml.safe_load(file)


def get_user_by_role(role):
    for user in CONFIG["users"]:
        if user["role"] == role:
            return user
    raise ValueError(f"No user found with role: {role}")


def get_ui_url(endpoint):
    try:
        return CONFIG["base_url"]["ui"] + CONFIG["endpoints"]["ui"][endpoint]
    except KeyError:
        raise Exception(f"Invalid UI endpoint: {endpoint}")


def get_browser_name():
    return CONFIG.get("browser", {}).get("name", "chrome")


def get_headless_mode_status():
    return CONFIG.get("browser", {}).get("headless", False)


def get_api_url(endpoint):
    try:
        return CONFIG["base_url"]["api"] + CONFIG["endpoints"]["api"][endpoint]
    except KeyError:
        raise Exception(f"Invalid API endpoint: {endpoint}")


def get_api_details():
    api_details = CONFIG["api_details"]
    api_details["username"] = os.getenv("API_USERNAME", api_details["username"])
    api_details["encrypt_password"] = os.getenv(
        "API_ENCRYPT_PASSWORD", api_details["encrypt_password"]
    )
    api_details["consumer_key"] = os.getenv("CONSUMER_KEY", api_details["consumer_key"])
    api_details["consumer_secret"] = os.getenv(
        "CONSUMER_SECRET", api_details["consumer_secret"]
    )

    return api_details


# def get_api_ignore_https_errors_status():
#     return CONFIG["api_details"].get("ignore_https_errors", True)


# def get_api_header_auth():
#     api_config = CONFIG["api_details"]
#     raw_token = f"{api_config['consumer_key']}:{api_config['consumer_secret']}"
#     encoded_token = base64.b64encode(raw_token.encode()).decode()

#     return {
#         "Authorization": f"{api_config['app_authorization']}{encoded_token}",
#         "Referer": api_config["referer"],
#         "Content-Type": api_config["content_type"],
#     }

# @pytest.fixture(autouse=True)
# def get_api_header_after_login(generate_api_token):
#     token = generate_api_token
#     api_config = CONFIG["api_details"]
#     return {
#         "Authorization": f"{api_config['resource_authorization']} {token}",
#         "Referer": api_config["referer"],
#         "Accept": api_config["accept"],
#     }
# def get_api_request_data():
#     api_config = CONFIG["api_details"]
#     data = {
#         "grant_type": api_config["grant_type"],
#         "username": api_config["username"],
#         "password": api_config["encrypt_password"],
#     }
#     return urlencode(data)


# def get_api_accept_header_value():
#     return CONFIG["api_details"].get("accept", "application/json")


# def get_api_resource_authorization():
#     return CONFIG["api_details"].get("resource_authorization", "Bearer ")


# def get_api_referer_header_value():
#     return CONFIG["api_details"]["referer"]
