from deep_translator import GoogleTranslator


def translate(input, first='auto', to="nl"):
    """
    Translator function which can be used to translate given inputs. Automatically set to detect and then translate to
    Dutch.
    :param input: string which has to be translated.
    :param first: current language.
    :param to: target language.
    :return: translated prompt.
    """
    translated = GoogleTranslator(source=first, target=to).translate(input)
    return translated


def test_translate():
    """
    Test function for translating
    :return: None
    """
    t = translate("What are you doing here Putin? You're not supposed to cross these borders!", "en", "nl")
    print(t)
