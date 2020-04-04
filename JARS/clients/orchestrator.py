from JARS.clients.parse_choices import ChoicesClient
from JARS.clients.discogs import JARSDiscogsClient

import os


class Orchestrator:

    def __init__(self, raw_choices):

        MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
        DISCOGS_CONF_FILE_NAME = os.path.join(MODULE_PATH, os.pardir, 'conf', 'discogs.yml')

        self.clean_choices = ChoicesClient(DISCOGS_CONF_FILE_NAME).process_choices(raw_choices)

    def run(self):
        discogs_client = JARSDiscogsClient(self.clean_choices)
        discogs_results = discogs_client.query_database()
        iterator_results = iter(discogs_results)

        desired_size = 10
        playlist = []

        while len(playlist) <= desired_size:
            release = next(iterator_results)
            print(release)
            playlist.append(release)


