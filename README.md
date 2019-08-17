# python-whoohoo
Allows you to translate english texts into different UK dialects via whoohoo.co.uk in python.
## Examples
The following is Fairly self-explaintory:
```
from whoohoo import *


translator = WhooHooTranslator(WhooHooTranslatorType.scottie)
original_text = "did you know that Water boils at 100 degrees Celsius?"
translated_text = translator.translate(original_text)
print(translated_text)
```
The following retrieves text from pastebin then translates to scottish english and saves into a file. <br/>
In this example we are going to use the bee movie script:
```
from urllib.request import urlopen
from whoohoo import *


translator = WhooHooTranslator(WhooHooTranslatorType.scottie)
bee_movie_script = urlopen("https://pastebin.com/raw/UfFEq7ei").read().decode()
translator.translate_to_file(bee_movie_script, "The bee movie script in Scottish English.txt")
```
