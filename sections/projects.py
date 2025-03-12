import streamlit as st
from sections.nlp_summarization import show_nlp_project
from sections.ai_chatbot import show_chatbot_project
from sections.disease_prediction import show_disease_project
from sections.ai_agent import show_ai_agent_project

def show_projects():
    st.header("📂 Projects")
    st.markdown("Click a project below to view its details:")

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None

    # --- PROJECT BUTTONS ---
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧠 NLP Text Summarization", key="NLP"):
            st.session_state.selected_project = "NLP"

        if st.button("💉 Disease Prediction Model", key="Disease"):
            st.session_state.selected_project = "Disease"

    with col2:
        if st.button("🤖 AI-Powered Chatbot", key="Chatbot"):
            st.session_state.selected_project = "Chatbot"

        if st.button("🧠 AI-Agent", key="Agent"):
            st.session_state.selected_project = "Agent"

    st.markdown("---")

    # --- DISPLAY FULL-WIDTH PROJECT DETAILS ---
    if st.session_state.selected_project == "NLP":
        show_nlp_project()

    elif st.session_state.selected_project == "Chatbot":
        show_chatbot_project()

    elif st.session_state.selected_project == "Disease":
        show_disease_project()

    elif st.session_state.selected_project == "Agent":
        show_ai_agent_project()
