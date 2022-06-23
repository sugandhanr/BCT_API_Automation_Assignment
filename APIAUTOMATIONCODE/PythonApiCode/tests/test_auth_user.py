from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.asserts import Asserts


class TestCreateUser(BaseCase):
    def test_wrong_data(self):
        data = {
            'email': 'sugusugan0@example.com',
            'password': 'JobSugan@2022'
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Invalid username/password supplied")
        Asserts.assert_response_not_has_cookie(response, '/movie/top_rated')
        Asserts.assert_response_not_has_headers(response, "/movie/top_rated")

    def test_auth_successfully(self):
        data = {
            'email': 'sugusugan0@example.com',
            'password': 'JobSugan@2022'
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_has_cookie(response, '/movie/top_rated')
        Asserts.assert_response_has_headers(response, "/movie/top_rated")

    def test_get_user_with_id(self):
        data = {
            'email': 'sugusugan0@example.com',
            'password': 'JobSugan@2022'
        }

        response = Request.post('user/login', data)

        Asserts.assert_json_has_key(response, 'user_id')

        auth_cookie = self.get_cookie(response, '/movie/top_rated')
        auth_header = self.get_header(response, '/movie/top_rated')
        user_id = response.json()['user_id']

        response = Request.get(f'user/{user_id}', headers=auth_header, cookies=auth_cookie)

        Asserts.assert_code_status(response, 200)
        Asserts.assert_json_has_key(response, 'firstName')
        Asserts.assert_json_has_key(response, 'lastName')
        Asserts.assert_json_has_key(response, 'email')

    def test_change_created_user_data(self):
        email = self.create_unique_email('sugan')
        password = 'JobSugan@2022'
        username = 'sugusugan0@gmail.com'

        data = {
            'email': email,
            'password': password,
            'username': username,
            'firstName': 'sugan',
            'lastName': 'sugu',
        }

        response = Request.post('user', data)
        user_id_after_registration = response.json()['id']
