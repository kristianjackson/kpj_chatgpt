import openai
import streamlit as st
import streamlit_chat as stc

openai.api_key = st.secrets["openai_api_key"]

MAX_TOKENS = 1024

def generate_initial_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = MAX_TOKENS,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    message = completions.choices[0].text
    return message

st.title("KPJ ChatGPT: powered by Streamlit and OpenAI")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input(
        "You: ",
        "Hello, how are you?",
        key = "input"
    )
    return input_text

user_input = None
while not user_input:
    user_input = get_text()

output = generate_initial_response(user_input)
st.session_state.past.append(user_input)
st.session_state.generated.append(output)

for i in range(len(st.session_state['generated'])):
    stc.message(
        st.session_state['generated'][i],
        key = str(i)
    )
    stc.message(
        st.session_state['past'][i],
        is_user = True,
        key = str(i) + '_user'
    )
