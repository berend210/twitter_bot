import openai
import setup

# Load your API key from an environment variable or secret management service
openai.api_key = setup.get_openai()


def response(prompt=None, tokens=10, engine=3):
    """
    Function which gets a gpt-3 completion response by the OpenAI API
    :param prompt: The text which should be used for a response
    :param tokens: Max amount of tokens to be used
    :param engine: Which engine to use
    :return:
    """
    engine_type = ["text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"]
    # Temperature is always 1 as we want the api to take as much risk as possible
    resp = openai.Completion.create(engine=engine_type[engine], prompt=prompt, temperature=1, max_tokens=tokens)
    # Returns only the text produced by the API
    return resp["choices"][0]["text"]


def test_openai3():
    out = response(prompt="Motivational quote", tokens=30)
    print(out)
