from src.adapter.controller.user_finder_controller import UserFinderController
from src.adapter.presenter.http_type.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self):
        self.query_params = { "first_name": "foo"}


class TestUserFinderController:
    def test_user_finder_success(self, memory_user_finder):
        controller = UserFinderController(use_case=memory_user_finder)

        http_request = HttpRequestMock()
        response  = controller.handler(http_request)

        expected_response = {
            "data": {
                "attributes": [
                    {
                        "age": 15, 
                        "first_name": "foo", 
                        "last_name": "bar"
                    }
                ],
                "count": 1,
                "type": "Users"
            }
        }

        assert response.status_code == 200
        assert response.body == expected_response
        assert isinstance(response, HttpResponse)