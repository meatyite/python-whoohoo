"""
A Module that allows you to use www.whoohoo.co.uk to translate texts into different dialects.
Works using BeautifulSoup4 and requests.

LICENSED UNDER THE WTFPL (DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE), SEE LICENSE.txt
NO COPYRIGHT WHATSOEVER
"""

import requests
from bs4 import BeautifulSoup as bs
from enum import Enum


class WhooHooTranslatorType(Enum):

    alig = "alig"
    cockney = "cockney"
    upnorf = "upnorf"
    irish = "irish"
    brummie = "brummie"
    geordie = "geordie"
    posh = "posh"
    scottie = "scottie"
    scouse = "scouse"


class WhooHooTranslator:

    def __init__(self, translator_type):
        self.translateType = translator_type.value

    # whoohoo.co.uk only accepts newlines as CRLF
    def __replace_all_newlines_with_CRLF(self, text):
        return text.replace('\r', '\r\n').replace('\r\n', '\n').replace('\n', '\r\n')

    def translate(self, text: str) -> str:
        text = self.__replace_all_newlines_with_CRLF(text)
        html = requests.post(
            url="http://www.whoohoo.co.uk/main.asp",
            data={
                'string': text,
                'x': '26',
                'y': '6',
                'pageid': self.translateType,
                'topic': 'translator'
            }
        ).text
        soup = bs(html, 'html.parser')
        translated_text = soup.find_all('form', recursive=True)[1].find('b').string
        # Sometimes it starts an empty space for some reason
        if translated_text[0] is ' ':
            translated_text = translated_text[1:]
        return translated_text

    def translate_to_file(self, text: str, file_path: str) -> None:
        translated_text = self.translate(text)
        open(file_path, 'wb').write(translated_text.encode())

