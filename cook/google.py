import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()


def syntax_text(text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    tokens = client.analyze_syntax(document).tokens
    word_dict = dict()
    for token in tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        word_dict[token.text.content] = part_of_speech_tag.name
    return word_dict
