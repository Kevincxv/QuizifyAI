import streamlit as st

st.set_page_config(page_title="We Are Quizmify")

st.markdown(
    """
    <style>
    /* App background */
    .stApp { background-color: #2F3136; }
    
    /* Primary buttons (FRQ/MCQ) */
    .stButton>button {
        border: 2px solid transparent;
        color: white;
        background-color: #01DF67;
        border-radius: 5px;
        font-size: 16px;
        width: 100%;
        height: 50px;
        padding: 10px 0;
        transition: background-color 0.3s, border-color 0.3s, color 0.3s;
    }
    .stButton>button:hover {
        background-color: #808080;
        color: white;
    }

    /* Text and input fields */
    .st-cd, .st-cb, .st-ci, .st-ck, .st-cl, .st-cm, .st-cj, .st-bb { color: #FFFFFF; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { color: #000000; background-color: #DDDDDD; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('We Are Quizmify')

url = st.text_input('Enter the URL', key='url')

if 'question_type' not in st.session_state:
    st.session_state.question_type = ''
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = ''

def set_question_type(q_type):
    st.session_state.question_type = q_type

def set_difficulty(difficulty):
    st.session_state.difficulty = difficulty

question_types = ['FRQ', 'MCQ']
col1, col2 = st.columns(2)
for i, q_type in enumerate(question_types):
    selected = st.session_state.question_type == q_type
    button_key = f'button_{q_type}'
    with locals()[f'col{i+1}']:
        if st.button(q_type, key=button_key, on_click=set_question_type, args=(q_type,)):
            pass

        if selected:
            st.markdown(f"""<style>.{button_key} {{ border-color: #FFFFFF; }}</style>""", unsafe_allow_html=True)


num_questions = st.number_input('How many questions?', min_value=1, max_value=100, step=1, key='num_questions')


difficulty_levels = ['Easy', 'Medium', 'Hard']
colors = {'Easy': '#4CAF50', 'Medium': '#FFEB3B', 'Hard': '#F44336'}
hover_colors = {'Easy': '#808080', 'Medium': '#808080', 'Hard': '#808080'}
text_colors = {'Easy': 'white', 'Medium': 'black', 'Hard': 'white'}

st.markdown("### Difficulty Level")
col1, col2, col3 = st.columns(3)

for i, level in enumerate(difficulty_levels, start=1):
    with locals()[f'col{i}']:
        selected = st.session_state.difficulty == level
        if st.button(level, key=level, on_click=set_difficulty, args=(level,)):
            pass
        
        button_style = f"background-color: {colors[level]}; color: {text_colors[level]};"
        if selected:
            button_style += " border: 2px solid #FFFFFF;"  
        st.markdown(f'<style>.stButton>button:active {{ {button_style} }}</style>', unsafe_allow_html=True)


