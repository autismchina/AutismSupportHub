import streamlit as st
from . AppConfig import AppConfig
from . pages.chat import load_chat_assistant
from . api.AssistantsApi import AssistantsApi

@st.cache_data
def get_secrets(key:str='OPENAI_API_KEY'):
    try:
        secrets = st.secrets.get(key,None)
        if not secrets:
            raise Exception(f'{key}获取失败')
    except Exception as e:
        raise e
    return secrets

def start():
    """程序启动"""
    config = AppConfig()

    st.set_page_config(
        page_title=config.page_title,
        page_icon=config.page_icon,
        layout= config.layout,
        initial_sidebar_state=config.sidebar_state
    )
    api_key = get_secrets()
    load_chat_assistant(api_key,config)
    
