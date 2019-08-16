from whoohoo import *
from requests import get as GET


translator = WhooHooTranslator(WhooHooTranslatorType.scottie)
bee_movie_script = GET("https://pastebin.com/raw/UfFEq7ei").content.decode()
bee_movie_script = bee_movie_script.replace('\r\n  \r\n', '')
translator.translate_to_file(bee_movie_script, 'bee movie script but it\'s in a scottish dialect.txt')