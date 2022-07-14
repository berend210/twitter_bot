import openai
import setup
import translator
import random
import twitter
from difflib import SequenceMatcher

# Load your API key from an environment variable or secret management service
openai.api_key = setup.get_openai()


def prompt_builder(text):
    """
    Prompt builder for the openai API. The prompt text is in the setup.py.
    :param text: string used for the prompt.
    :return: Prompt with the wanted text.
    """
    prompt_list = setup.get_prompts()
    chance = random.randint(0, len(prompt_list) - 1)
    prompt = prompt_list[chance][0].replace("#text#", text)
    print(prompt_list[chance][1])
    return prompt


def response(prompt=None, tokens=25, engine=3, translate_nl=True, build_prompt=True):
    """
    Function which gets a gpt-3 completion response by the OpenAI API.
    :param prompt: The text which should be used for a response.
    :param tokens: Max amount of tokens to be used.
    :param engine: Which engine to use.
    :param translate_nl: Whether it should to translated to Dutch or not.
    :param build_prompt: Whether the prompt builder should be used or not.
    :return:
    """

    engine_type = ["text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"]
    inp = prompt

    if prompt is None:
        return "Try again please"

    if translate_nl:
        prompt = translator.translate(prompt, "auto", "en")

    if build_prompt:
        prompt = prompt_builder(prompt)

    try:
        resp = openai.Completion.create(engine=engine_type[engine], prompt=prompt, temperature=1, max_tokens=tokens)
    except:
        return None

    # Returns only the text produced by the API
    text = resp["choices"][0]["text"]
    print("OPENAI: " + text)

    if translate_nl:
        text = translator.translate(text.strip(), "en", "nl")

    # Makes the output weird when the inp is too similar.
    if SequenceMatcher(None, inp, text).ratio() > 0.7:
        text = twitter.ret_speech(text)

    print("Final resp: " + text)
    return text


def test_openai3():
    """
    OpenAI test function.
    :return: None.
    """
    out = response(prompt="Beren", tokens=22, build_prompt=True)
    print("Test openAI API: " + out)
