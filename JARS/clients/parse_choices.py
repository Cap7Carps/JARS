from .. import YEAR, COUNTRY, GENRE

import os
import yaml

class ChoicesClient:

    def __init__(self, raw_choices):
        """
        :param raw_choices: Dictionary of raw-text choices provided by user
        """

        MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
        CONF_FILE_NAME = os.path.join(MODULE_PATH, os.pardir, 'conf', 'discogs.yml')

        self.raw_choices = raw_choices
        self.config = self.load_config(CONF_FILE_NAME)
        self.valid_genres = self.load_valid_genres()
        self.valid_styles = self.load_valid_styles()


    # Below will include the parsing of multiple genres/typos etc.

    @property
    def cleaned_choices(self):
        return self.raw_choices

    @property
    def valid_genres(self):
        return self.valid_genres

    @property
    def valid_styles(self):
        return self.valid_styles

    @staticmethod
    def load_valid_genres(conf):
        pass

    @staticmethod
    def load_config(full_conf_filepath):
        with open(full_conf_filepath, 'rt') as file_obj:
            conf = yaml.safe_load(file_obj.read())

        return conf

