
from altair import param
from . OpenAIApi import OpenAIApi
class AssistantsApi(OpenAIApi):
    def __init__(self, api_key: str, organization: str = None) -> None:
        super().__init__(api_key, organization)
    
    def get_all_assistants(self):
        assistants = self.client.beta.assistants.list(
            order='desc',
            limit=20
        )

        return assistants
