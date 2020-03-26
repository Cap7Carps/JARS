from parse_choices import ChoicesClient


class Orchestrator:

    def __init__(self, raw_choices):
        self.raw_choices = raw_choices
        self.clean_choices = ChoicesClient(raw_choices).cleaned_choices

    def run(self):
        pass

    def prepare_query(self):
        pass

    def retrieve_releases(self, query):
        # Used NamedTuple to create something which you can easily access artist/release from
        pass

