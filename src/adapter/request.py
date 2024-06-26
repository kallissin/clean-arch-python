from typing import Callable
from flask import request as FlaskRequest
from src.adapter.presenter.http_type.http_request import HttpRequest
from src.adapter.presenter.http_type.http_response import HttpResponse



def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:
    http_request = HttpRequest(
        headers=request.headers,
        body=request.json or {},
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    http_response = controller(http_request)
    return http_response
