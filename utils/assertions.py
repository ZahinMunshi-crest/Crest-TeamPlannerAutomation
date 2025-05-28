def assert_status_code(response, expected_code):
    assert (
        response.status == expected_code
    ), f"Expected: {expected_code}, but received {response.status}"
