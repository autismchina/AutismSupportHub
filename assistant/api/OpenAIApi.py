import logging
from openai import OpenAI

class OpenAIApi:
    def __init__(self,api_key:str,organization:str=None) -> None:
        self.client = OpenAIApi.get_openai_client(api_key,organization)

    @staticmethod
    def get_openai_client(api_key:str,organization:str=None):
        """获取openai客户端连接"""
        try:
            client = OpenAI(api_key=api_key,
                            organization=organization)
            logging.info(f'openai认证成功{client.base_url}')
        except Exception as e:
            raise e('openai认证失败。')
        return client