from src.helpers.config import get_setting,settings
import os


class BaseController:
    def __init__(self):
        self.app_setting = get_setting()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
    