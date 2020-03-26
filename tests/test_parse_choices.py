from JARS import COUNTRY, GENRE, YEAR
from JARS.clients.parse_choices import ChoicesClient

import os

import pytest
import yaml
import pdb

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_FILES_PATH = os.path.join(MODULE_PATH, 'test_files')
available_choices = [COUNTRY, GENRE, YEAR]



# META

def create_choice(**choices):
    for key in choices.keys():
        if key not in available_choices:
            raise RuntimeError(f'Choice was created with invalid key: {key}')
    return {choice_key: choices.get(choice_key) for choice_key in available_choices}


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
        cls.dummy_client = ChoicesClient({})

    def test_cleaned_choices(self):
        choices = create_choice(country='Germany')
        choices_cli = ChoicesClient(choices)

        cleaned_choices = choices_cli.cleaned_choices

        assert choices == cleaned_choices

    def test_load_config_valid(self):
        valid_config_filepath = os.path.join(TEST_FILES_PATH, 'valid_dummy_config.yml')
        expected = {'valid': {'list-of-vars': ['a', 'b', 'c', 'd']}}
        with open(valid_config_filepath, 'wt') as file_obj:
            yaml.dump(expected, file_obj)

        config = self.dummy_client.load_config(valid_config_filepath)
        assert config == expected
