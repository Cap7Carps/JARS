from JARS import COUNTRY, GENRE, YEAR
import pytest
import pdb

from JARS.clients.parse_choices import ChoicesClient

available_choices = [COUNTRY, GENRE, YEAR]


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


def test_cleaned_choices():
    choices = create_choice(country='Germany')
    choices_cli = ChoicesClient(choices)

    cleaned_choices = choices_cli.cleaned_choices

    assert choices == cleaned_choices


