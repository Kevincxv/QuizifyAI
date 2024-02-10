import streamlit as st
from streamlit.components.v1 import html
import time
import requests


st.set_page_config(
    page_title="Quizmify",
    page_icon="favicon.png",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        
    }
)

st.markdown("""
 <style>
    .stButton>button {
        border: 1px solid #4CAF50; /* Green border */
        background-color: #4CAF50; /* Green background */
        color: black; /* Black text */
        padding: 10px 24px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #8ef08e; /* Lighter green for hover */
        color: black; /* Black text on hover */
        outline: 2px solid black; /* Black outline on hover */
        outline-offset: -2px;
    }
    .stButton>button:active {
        background-color: rgba(0, 0, 0, 0.1); /* Lighter opacity black on click */
        border: 1px solid #4CAF50; /* Same green border */
        color: black; /* Black text */
        outline: 2px solid black; /* Same black outline */
    }
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
""", unsafe_allow_html=True)

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

st.header("Welcome to :green[Quizmify] your AI Learning Companion", help=None, divider=False)

url = st.text_input("Enter a URL you would like to know more about!", value="URL", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

uploaded_file = st.file_uploader("Upload Your PDF Document Here!", type=['pdf'])

def generate_questions_from_pdf(pdf_path, start_page=None, end_page=None):
    url = 'http://localhost:3000/generate'  # URL to your backend's /generate endpoint
    payload = {
        'pdfPath': pdf_path,
        'startPage': start_page,
        'endPage': end_page
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json().get('questions')
    else:
        st.error('Failed to get a response from the backend.')
        return None


st.selectbox("Select what type of questions you would like to be asked!", ("Multiple Choice Quesions", "Free Response Questions"), index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

num_questions = st.number_input("How man questions do you want?", min_value=1, max_value=20, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

st.selectbox("Select what level of difficultiy you want!", ("Easy", "Medium", "Hard"), index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

if st.button("Generate Quiz"):
    if uploaded_file and num_questions > 0:
        st.write("Processing your request...")

        # Save the uploaded file to a temporary path on your server
        with open("temp_uploaded_pdf.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Assuming the PDF is saved at 'temp_uploaded_pdf.pdf' on your server
        questions = generate_questions_from_pdf("temp_uploaded_pdf.pdf")

        if questions:
            st.write("Quiz is ready!")
            for question in questions:
                st.write(question)
        else:
            st.error("Failed to generate questions.")
    else:
        st.error("Please make sure all inputs are provided correctly.")