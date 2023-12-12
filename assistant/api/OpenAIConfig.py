
from dataclasses import dataclass


class OpenAIConfig:
    # gpt-3.5-turbo
    def __init__(self,messages:list[dict],model='gpt-4-1106-preview',stream=True):
        self.model = model
        self.messages = messages
        self.stream = stream