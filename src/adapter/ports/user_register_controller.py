from abc import ABC, abstractmethod
from src.adapter.presenter.http_type.http_request import HttpRequest
from src.adapter.presenter.http_type.http_response import HttpResponse


class IUserRegisterController(ABC):
    
    @abstractmethod
    def handler(self, http_request: HttpRequest) -> HttpResponse:
        pass
