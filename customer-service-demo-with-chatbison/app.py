import streamlit as st
import os
import time

from vertexai.language_models import ChatModel
from langchain_core.messages import HumanMessage, AIMessage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/root/key/key.json'
model_id = "chat-bison@002"

context = '''
You are a helpful order return assistant.
Customers will use you to return their items. Items can only be returned if they were purchased within the last 15 days and are unused.
Make sure to confirm that item is BOTH unused and was purchased within the last 15 days. Please ask customer for both the rules.
If BOTH the above conditions are met, then show a message with the return address [1st main street, new york, NY 10001], otherwise reject the return with a friendly message.
Do not worry about Order Numbers or Product Details.
'''

chat_model = ChatModel.from_pretrained(model_id)
chat = chat_model.start_chat(context=context)

parameters = {
    "temperature": 0.0,
    "max_output_tokens": 256,
    "top_p": 0.95,
    "top_k": 40
}

def response_generator(prompt, parameters, messages):
    history = ''
    for message in messages:
        if isinstance(message, HumanMessage):
            history = f"{history}\nUser: {message.content}"

        if isinstance(message, AIMessage):
            history = f"{history}\nAssistant: {message.content}"



    response = chat.send_message(f"{history}\n{prompt}", **parameters)
    response_text = response.text

    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)

def reset_chat():
    st.session_state.messages = []

def main():
    st.title("Customer Service Agent Demo")
    st.write("Hello, Wecome to the return center. I am here to help you.")

    if "messages" not in st.session_state:
        st.session_state.messages = []


    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)


    if prompt:= st.chat_input("Hello, how can I help you?"):
        st.session_state.messages.append(HumanMessage(prompt))
        with st.chat_message("Human"):
            st.markdown(prompt)

        with st.chat_message("AI"):
            response = st.write_stream(response_generator(prompt, parameters, st.session_state.messages))

        st.session_state.messages.append(AIMessage(response))

    st.button("Reset Chat", on_click=reset_chat)

if __name__ == "__main__":
    main()







