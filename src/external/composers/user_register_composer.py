from src.external.repository.user_repository import UserRepository
from src.application.use_case.user_register import UserRegister
from src.adapter.controller.user_register_controller import UserRegisterController



def user_register_composer():
    repository = UserRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return controller.handler
