import streamlit as st
import time
import requests

api_endpoint = "https://xum2r4r3zyuyllk4wx3vayakxq0pgeah.lambda-url.us-west-2.on.aws/"


# Method takes in user text, creates a prompt and invoke the foundation model

def get_response(text):
    payload = {
        "prompt": f"Please summarize the following text.\n {text}"
    }

    response = requests.post(api_endpoint, json = payload)
    print(f"response status:: {response.status_code}")
    response_text = response.text

    # For streaming like behavior
    for word in response_text.split():
        yield word + " "
        time.sleep(0.1)


def main():
    st.set_page_config("Text Summarization Demo")
    st.header("AWS Bedrock integration with Serverless Lambda  - Cohere model")

    text = st.text_area("Write text to summarize")

    if st.button("Summarize It"):
        with st.spinner("processing..."):
            ##call lambda function url
            st.write(get_response(text))


if __name__ == "__main__":
    main()