from src.external.repository.user_repository import UserRepository
from src.application.use_case.user_finder import UserFinder
from src.adapter.controller.user_finder_controller import UserFinderController



def user_finder_composer():
    repository = UserRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)

    return controller.handler
