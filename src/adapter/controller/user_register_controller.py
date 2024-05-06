from src.adapter.ports.user_register_controller import IUserRegisterController
from src.adapter.presenter.http_type.http_request import HttpRequest
from src.adapter.presenter.http_type.http_response import HttpResponse
from src.application.use_case.user_register import UserRegister


class UserRegisterController(IUserRegisterController):
    def __init__(self, use_case: UserRegister):
        self.__use_case = use_case


    def handler(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]
    
        response = self.__use_case.register(first_name, last_name, age)

        return HttpResponse(
            status_code=201,
            body={ "data": response }
        )
