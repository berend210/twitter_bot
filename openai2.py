# ########################################################################### #
# ############################### DEPRECATED ################################ #
# ########################################################################### #
# from transformers import pipeline
#
# pipe = pipeline("text-generation", model="GroNLP/gpt2-small-dutch")
#
#
# # https://huggingface.co/GroNLP/gpt2-small-dutch?text=Test+hello+my+name+is+mark
# # https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextGenerationPipeline
#
# def output_filter(output):
#     """
#     Helper function, makes sure there are whole sentences
#     :param output: The generated text
#     :return: A smaller string in case the function detected a finished sentence
#     """
#     # Filters it to be a full sentence
#     pos = output[40:].find('.')
#     if output[40:].find('!') > pos:
#         pos = output[40:].find('!')
#     elif output[40:].find('?') > pos:
#         pos = output[40:].find('?')
#     if pos == -1:
#         return output
#     return output[0:pos + 41]
#
#
# def response2(input, length=100):
#     """
#     Uses the GroNLP GPT-2-small text generation model to generate gpt-2 responses
#     :param input: The text inp
#     :param length: The max length of the output
#     :return: A text-generated response
#     """
#     if input[-1] != '.':
#         input += '.'
#     length = len(input)
#     # Generate text
#     gen3 = pipe.__call__(text_inputs=input, max_length=length + len(input), temperature=0.50)[0]['generated_text'][
#            length:]
#     # Filter the generated text
#     output = output_filter(gen3)
#     print(output)
#     return output
