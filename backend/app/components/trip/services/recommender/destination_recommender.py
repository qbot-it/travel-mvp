from gpt4all import GPT4All
from .parser import Parser
from ...dto.destination import Destination
from ....config import settings


class DestinationRecommender:
    __model: GPT4All
    __replace_token: str
    __prompt: str
    __parser: Parser

    def __init__(self):
        print('Load GPT model...')
        self.__model = GPT4All(settings.gpt_model, model_path='files/models')
        self.__replace_token = '<DESCRIPTION>'
        self.__prompt = (f"Find 3 places for vocation in the world with an airport nearby (include IATA airport code) "
                         f"that are similar to the description: '{self.__replace_token}'")
        print('GPT model ready')
        self.__parser = Parser()

    def run(self, descriptions: list) -> list[Destination]:
        destinations = []
        with self.__model.chat_session():
            for description in descriptions:
                prompt = self.__prompt.replace(self.__replace_token, description)
                response = self.__model.generate(prompt)
                destinations.extend(self.__parser.parse(response))

        return destinations

