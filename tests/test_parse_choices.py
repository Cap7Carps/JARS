from JARS import COUNTRY, GENRE, YEAR
from JARS.clients.parse_choices import ChoicesClient

import os
from unittest.mock import patch, MagicMock, PropertyMock
import pytest
import yaml
import pdb

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_FILES_PATH = os.path.join(MODULE_PATH, 'test_files')
AVAILABLE_CHOICES = [COUNTRY, GENRE, YEAR]


# META

def create_choice(**choices):
    for key in choices.keys():
        if key not in AVAILABLE_CHOICES:
            raise RuntimeError(f'Choice was created with invalid key: {key}')
    return {choice_key: choices.get(choice_key) for choice_key in AVAILABLE_CHOICES}


def test_create_choice_valid():
    created_choice = create_choice(country='England', genre='Rock')
    expected = {'genre': 'Rock', 'country': 'England', 'year': None}

    assert created_choice == expected


def test_create_choice_invalid_key():
    with pytest.raises(RuntimeError):
        create_choice(age=22, genre='Rock')


class TestChoicesClient:

    @classmethod
    def setup_class(cls):
        cls.dummy_client = ChoicesClient(os.path.join(TEST_FILES_PATH, 'test_config.yml'))

    def test_load_config_valid(self):
        valid_config_filepath = os.path.join(TEST_FILES_PATH, 'rewritable_file.yml')
        expected = {'valid': {'list-of-vars': ['a', 'b', 'c', 'd']}}
        with open(valid_config_filepath, 'wt') as file_obj:
            yaml.dump(expected, file_obj)

        config = ChoicesClient.load_config(valid_config_filepath)
        assert config == expected

    def test_parse_genres_styles(self):

        config = {'genres-styles': {'Rock': ['Grunge', 'Punk'], 'Electronic': ['Techno', 'Gabba']}}
        parsed_config = self.dummy_client.parse_genres_styles(config)
        expected = {'genres': ['Rock', 'Electronic'], 'styles': ['Grunge', 'Punk', 'Techno', 'Gabba']}

        assert parsed_config == expected

    def test_map_choice_genre_style_valid_choices_no_whitespace(self):

        self.dummy_client.valid_genres = ['Rock', 'Folk', 'Rap']
        self.dummy_client.valid_styles = ['Drone', 'Drill', 'K-pop']

        raw_choices = 'drone,rap,k-pop'
        expected_result = {'genre': ['Rap'], 'style': ['Drone', 'K-pop']}
        result = self.dummy_client.map_choice_genre_style(raw_choices)

        assert expected_result == result

    def test_map_choice_genre_style_valid_choices_WITH_whitespace(self):

        self.dummy_client.valid_genres = ['Rock', 'Folk', 'Rap']
        self.dummy_client.valid_styles = ['Drone', 'Drill', 'K-pop']

        raw_choices = 'drone,  rap,  k-pop'
        expected_result = {'genre': ['Rap'], 'style': ['Drone', 'K-pop']}
        result = self.dummy_client.map_choice_genre_style(raw_choices)

        assert expected_result == result

    def test_map_choice_genre_style_invalid_choices(self):

        self.dummy_client.valid_genres = ['Rock', 'Folk', 'Rap']
        self.dummy_client.valid_styles = ['Drone', 'Drill', 'K-pop']

        raw_choices = 'drone,  rap,  k-pop,discooo'
        expected_result = {'genre': ['Rap'], 'style': ['Drone', 'K-pop'], 'unmatched': ['Discooo']}
        result = self.dummy_client.map_choice_genre_style(raw_choices)

        assert expected_result == result
