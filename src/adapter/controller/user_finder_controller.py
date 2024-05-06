from src.adapter.ports.user_finder_controller import IUserFinderController
from src.adapter.presenter.http_type.http_request import HttpRequest
from src.adapter.presenter.http_type.http_response import HttpResponse
from src.application.use_case.user_finder import UserFinder


class UserFinderController(IUserFinderController):
    def __init__(self, use_case: UserFinder):
        self.__use_case = use_case


    def handler(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]
        response = self.__use_case.find(first_name)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
