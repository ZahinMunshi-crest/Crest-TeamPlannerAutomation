# def test_api_login(generate_api_token):
#     print(generate_api_token)


from utils import assertions as ast
from utils.api_client import ApiClient

client = ApiClient()


def test_get_login_status_code(generate_api_token):
    token = generate_api_token
    response = client.get(endpoint="get_login_user", token=token)
    ast.assert_status_code(response, 200)
