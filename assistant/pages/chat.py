import streamlit as st
from .. api.ChatCompletionsApi import ChatCompletionsApi
from .. api.OpenAIConfig import OpenAIConfig
from .. AppConfig import AppConfig
def load_chat_assistant(api_key:str,config:AppConfig):
    """加载聊天"""
    st.header(config.assistant_name)
    # 初始化 session_state
    if 'messages' not in st.session_state:
        st.session_state.messages = [config.wellcome]
    #显示聊天历史
    for messages in st.session_state.messages:
        with st.chat_message(messages['role']):
            st.markdown(messages['content'])
    #输入问题并回答
    if prompt := st.chat_input(placeholder="请输入您的问题",
                               max_chars=800):
        st.session_state['messages'].append(
            dict(role='user',content=prompt),
        )
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            placeholer = st.empty()
            
            messages=[{"role": m["role"], "content": m["content"]} \
                  for m in st.session_state.messages]
            messages.append(config.instructions)
            config = OpenAIConfig(messages)
            chatCompletionsApi = ChatCompletionsApi(api_key)
            response = chatCompletionsApi.create_chat_completions(config,placeholer)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
