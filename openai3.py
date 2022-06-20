import openai
import setup
import translator

# Load your API key from an environment variable or secret management service
openai.api_key = setup.get_openai()


def prompt_builder(text):
    prompt = "Tweet: " + text + "\n" + "You: "
    return prompt


def response(prompt=None, tokens=20, engine=3, translate_nl=True, build_prompt=False):
    """
    Function which gets a gpt-3 completion response by the OpenAI API
    :param prompt: The text which should be used for a response
    :param tokens: Max amount of tokens to be used
    :param engine: Which engine to use
    :return:
    """
    tran = 0
    gentex = 0
    engine_type = ["text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"]

    if prompt is None:
        return "Try again please"

    if translate_nl:
        tran = translator.translate(prompt, "nl", "en")
    else:
        tran = prompt

    if build_prompt:
        gentex = prompt_builder(tran)
    else:
        gentex = tran

    try:
        resp = openai.Completion.create(engine=engine_type[engine], prompt=gentex, temperature=1, max_tokens=tokens)
    except:
        return None

    # Returns only the text produced by the API
    text = resp["choices"][0]["text"]
    print("EN: " + text)

    if translate_nl:
        end = translator.translate(text.strip(), "en", "nl")
        print("NL: " + end + "\n\n")

    return end


def test_openai3():
    out = response(prompt="Motiverende tekst", tokens=22, build_prompt=True)
    print(out)


# test_openai3()
