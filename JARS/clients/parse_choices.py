from .. import YEAR, COUNTRY, GENRE


class ChoicesClient:

    def __init__(self, choices):
        """
        :param choices: Dictionary of choices provided by user
        """
        self.cleaned_choices = choices

    def cleaned_choices(self):
        return self.cleaned_choices

    # Below will include the parsing of multiple genres/typos etc.
