import streamlit as st

st.set_page_config(page_title="Quiz Generator")

st.markdown(
    """
    <style>
    /* App background */
    .stApp { background-color: #2F3136; }

    /* Header color */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF; /* White color for headers */
    }

    /* Adjustments for radio labels (Question Type and Difficulty) to white */
    .stRadio > label {
        color: white !important;
    }

    /* Primary buttons styling (FRQ, MCQ, Easy, Medium, Hard) */
    .stButton>button {
        border: 2px solid transparent;
        color: white;
        background-color: #01DF67; /* Green background */
        border-radius: 5px;
        font-size: 16px;
        padding: 10px 20px; /* Adjust padding for better appearance */
        transition: background-color 0.3s, border-color 0.3s;
    }

    /* Hover effect for all buttons */
    .stButton>button:hover {
        background-color: #808080; /* Grey background on hover */
    }

    /* Difficulty buttons specific colors */
    /* Note: It's tricky to target specific Streamlit buttons with CSS alone due to dynamic class names.
       You'll need to add custom classes via JavaScript or use button labels for conditional styling in Python. */

    /* Text and input fields styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stNumberInput>div>div>input {
        color: #000000; /* Black text for input */
        background-color: #DDDDDD;
    }

    /* Label color adjustment */
    .stTextInput>label, .stNumberInput>label, .stRadio>div>label {
        color: #FFFFFF; /* White color for input labels */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("We Are Quizmify")


textbook_url = st.text_input("Enter the textbook URL", key="textbook_url")
page_range = st.text_input("Page Range", key="page_range")
question_type = st.radio("Question Type", ['FRQ', 'MCQ'], key="question_type", horizontal=True)
num_questions = st.number_input("Number of Questions", min_value=1, max_value=100, step=1, key="num_questions")
difficulty = st.radio("Difficulty", ['Easy', 'Medium', 'Hard'], key="difficulty", horizontal=True)


quiz_placeholder = st.empty()
answers_placeholder = st.empty()


if st.button("Generate Quiz"):
    if not textbook_url or not page_range:
        st.error("Please fill in all fields.")
    else:
        
        quiz = {
            "questions": ["What is X?", "How does Y work?"],
            "answers": ["X is...", "Y works by..."]
        }
        quiz_placeholder.write("Quiz Questions:")
        for i, question in enumerate(quiz["questions"], start=1):
            quiz_placeholder.write(f"{i}. {question}")
            
        if st.button("Show Answers"):
            answers_placeholder.write("Quiz Answers:")
            for i, answer in enumerate(quiz["answers"], start=1):
                answers_placeholder.write(f"{i}. {answer}")
