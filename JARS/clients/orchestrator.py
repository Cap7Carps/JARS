from parse_choices import ChoicesClient

import os


class Orchestrator:

    def __init__(self, raw_choices):

        MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
        DISCOGS_CONF_FILE_NAME = os.path.join(MODULE_PATH, os.pardir, 'conf', 'discogs.yml')

        self.raw_choices = raw_choices
        self.clean_choices = ChoicesClient(DISCOGS_CONF_FILE_NAME).process_choices(raw_choices)

    def run(self):
        pass

    def prepare_query(self):
        pass

    def retrieve_releases(self, query):
        # Used NamedTuple to create something which you can easily access artist/release from
        pass

