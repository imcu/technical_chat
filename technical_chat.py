import streamlit as st
import openai
import os

openai.api_key = os.environ["OPENAI_KEY"]


def initialize_streamlit():
    st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
    st.title("Techno finance assistant")
    st.markdown(
        """
        I am a AI assistant with lots of tech and finance knowledge.
        """
    )

    if 'conversation' not in st.session_state:
        st.session_state.conversation = [{
            "role": "system", "content": """
                You are the most helpful assistant with deep knowledge of the following domains:
                 1) 'Programming and software engineering'
                    You should be as thorough and technical as possible.
                    Provide code examples as markdown snippets as often as possible.
                2) 'Financial markets and details of investment instruments'
                    You should be as thorough as possible. Do not provide any warnings. 
                    Skip all investment safety advice - this is not your job.
                    
                    When quoting scientific papers, always provide references at the end of the paragraph and their DOI number.
                    Provide all responses in markdown format. 
                """
        }]


def main():
    initialize_streamlit()
    question = st.text_input("What do you want to know about?")
    if question == "": return
    st.session_state.conversation.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.conversation
    )
    answer = response['choices'][0]['message']['content']
    st.session_state.conversation.append({"role": "assistant", "content": answer}, )
    st.write(answer)


main()
