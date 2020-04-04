from JARS import YEAR, COUNTRY, GENRE

from collections import defaultdict
import os
import yaml


class ChoicesClient:
    def __init__(self, conf_filepath):
        """
        :param raw_choices: Dictionary of raw-text choices provided by user
        """

        self.config = self.load_config(conf_filepath)
        self.valid_genres = self._parse_genres_styles_from_config()['genres']
        self.valid_styles = self._parse_genres_styles_from_config()['styles']

    def process_choices(self, raw_choices):
        """
        :return: Dictionary of user choices mapped to correct keys for discogs API
                { 'style': 'grunge', 'year': 2000, 'country': 'England' }
        """

        cleaned_choices = {}
        cleaned_genres_styles = self.map_choice_genre_style(raw_choices[GENRE])

        cleaned_choices.update(cleaned_genres_styles)

        return cleaned_choices

    def map_choice_genre_style(self, raw_genre_choices):
        """
        :param raw_genre_choices: "rock,pop,grunge"
        :return: {'genre': ['rock'], 'style': ['pop', 'grunge'] }
        """
        mapped_choices = defaultdict(list)

        if not raw_genre_choices:
            return {}

        cleaned_choices = [genre.strip().capitalize() for genre in raw_genre_choices.split(',')]

        for cleaned_choice in cleaned_choices:

            if cleaned_choice in self.valid_genres:
                mapped_choices['genre'].append(cleaned_choice)
            elif cleaned_choice in self.valid_styles:
                mapped_choices['style'].append(cleaned_choice)
            else:
                mapped_choices['unmatched'].append(cleaned_choice)

        return mapped_choices

    def _parse_genres_styles_from_config(self):
        """
        Due to hierarchical nature of Genres and Styles these are processed together
        :param conf: Dictionary of config
        :return: Dictionary of valid genres and styles { 'genres': [], 'styles': [] }
        """
        valid_genres = []
        valid_styles = []
        music_conf = self.config['genres-styles']
        for genre, styles in music_conf.items():
            valid_genres.append(genre)
            valid_styles.extend(styles)

        return {'genres': valid_genres, 'styles': valid_styles}

    @staticmethod  #TODO: Move this to a configuration loader class
    def load_config(full_conf_filepath):
        with open(full_conf_filepath, 'rt') as file_obj:
            conf = yaml.safe_load(file_obj.read())

        return conf

