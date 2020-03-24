from . import GENRE, YEAR, COUNTRY
from clients.parse_choices import ChoicesClient

import PySimpleGUI as sg


def main():
    raw_choices = get_user_choices()
    clean_choices = ChoicesClient(raw_choices).cleaned_choices()
    # JARSClient(**clean_choices)


def get_user_choices():


    sg.theme('DarkAmber')   # Add a touch of color

    layout = [
                [sg.Text('What should your Playlist compromise of?')],
                [sg.Text('Genre/Style'), sg.InputText(key=GENRE)],
                [sg.Text('Year'), sg.InputText(key=YEAR)],
                [sg.Text('Country'), sg.InputText(key=COUNTRY)],
                [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('JARS', layout)

    event, choices = window.read()

    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        exit(1)

    window.close()

    return choices


if __name__ == '__main__':
    main()
