from helpers.config import get_setting,settings

class BaseController:
    def __init__(self):
        self.app_setting = get_setting()
    