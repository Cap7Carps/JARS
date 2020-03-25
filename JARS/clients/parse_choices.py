from .. import YEAR, COUNTRY, GENRE


class ChoicesClient:

    def __init__(self, raw_choices):
        """
        :param raw_choices: Dictionary of choices provided by user
        """
        self.choices = raw_choices

    @property
    def cleaned_choices(self):
        return self.choices

    # Below will include the parsing of multiple genres/typos etc.
