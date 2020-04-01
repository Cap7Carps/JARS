from JARS import GENRE, YEAR, COUNTRY
from JARS.clients.parse_choices import ChoicesClient
from JARS.clients.orchestrator import Orchestrator


import PySimpleGUI as sg


def main():
    raw_choices = get_user_choices()
    Orchestrator(raw_choices).run()


def get_user_choices():
    """
    :return: Dictionary of user's input choices {'country': 'England', 'genre': 'techno', ...}
    """

    CANCEL = 'cancel'

    sg.theme('DarkAmber')

    layout = [
                [sg.Text('What should your Playlist compromise of?')],
                [sg.Text('Genre/Style'), sg.InputText(key=GENRE)],
                [sg.Text('Year'), sg.InputText(key=YEAR)],
                [sg.Text('Country'), sg.InputText(key=COUNTRY)],
                [sg.Button('Ok'), sg.Button(CANCEL)]
    ]

    window = sg.Window('JARS', layout)

    event, choices = window.read()

    if event in (None, CANCEL):   # if user closes window or clicks cancel
        exit(1)

    window.close()

    return choices


if __name__ == '__main__':
    main()
