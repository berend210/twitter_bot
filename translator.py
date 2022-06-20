import requests


def translate(input, first, to):
    url = "https://libretranslate.de/translate"

    payload = {
        "q": input,
        "source": first,
        "target": to,
        "format": "text"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    for target in response:
        string = str(target, 'utf-8')
        if "\\u00eb" in string:
            string = string.replace("\\u00eb", "ë")
        if "\\n" or "\\n\\n" in string[19:-3]:
            string = string[19:-3].partition("\\")[0]
            return string

    return string[19:-3]


def test_translate():
    t = translate("What are your bullies' reasons for trying to make you feel down? \n Some bullies may be because they", "en", "nl")
    print(t)
