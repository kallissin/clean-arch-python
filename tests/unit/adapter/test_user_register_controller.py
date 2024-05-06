from src.adapter.controller.user_register_controller import UserRegisterController
from src.adapter.presenter.http_type.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self):
        self.body = { 
            "first_name": "foo",
            "last_name": "bar",
            "age": 25
        }


class TestUserRegisterController:
    def test_user_register_success(self, memory_user_register):
        controller = UserRegisterController(use_case=memory_user_register)

        http_request = HttpRequestMock()
        response  = controller.handler(http_request)

        expected_response = {
            "data": {
                "attributes": [
                    {
                        "age": 25, 
                        "first_name": "foo", 
                        "last_name": "bar"
                    }
                ],
                "count": 1,
                "type": "Users"
            }
        }

        assert response.body == expected_response
        assert response.status_code == 201
        assert isinstance(response, HttpResponse)
