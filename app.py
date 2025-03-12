import streamlit as st
from PIL import Image
from sections.introduction import show_introduction
from sections.projects import show_projects
from sections.education import show_education
from sections.contact import show_contact
from sections.resume import show_resume

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Yaswanth's Portfolio", page_icon="🤖", layout="wide")

# --- CUSTOM CSS ---
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- INTRODUCTION SECTION ---
show_introduction()

# --- SESSION STATE INITIALIZATION ---
if "selected_section" not in st.session_state:
    st.session_state.selected_section = None

# --- NAVIGATION BUTTONS ---
st.markdown("---")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📂 Projects", key="projects"):
        st.session_state.selected_section = "Projects"
        st.rerun()

with col2:
    if st.button("🎓 Education", key="education"):
        st.session_state.selected_section = "Education"
        st.rerun()

with col3:
    if st.button("📞 Contact", key="contact"):
        st.session_state.selected_section = "Contact"
        st.rerun()

with col4:
    if st.button("🌐 Live Demo"):
        st.markdown("[🚀 Deployed Project](http://3.83.87.37:8501/)")

with col5:
    if st.button("📄 Resume", key="resume"):
        st.session_state.selected_section = "Resume"
        st.rerun()

# --- DISPLAY SELECTED SECTION CONTENT ---
st.markdown("---")

if st.session_state.selected_section == "Projects":
    show_projects()

elif st.session_state.selected_section == "Education":
    show_education()

elif st.session_state.selected_section == "Contact":
    show_contact()

elif st.session_state.selected_section == "Resume":
    st.markdown('<div class="section-headline">📄 Resume</div>', unsafe_allow_html=True)
    show_resume()

# --- FOOTER ---
st.markdown("""
<div class='footer'>
    © 2025 Yaswanth. All rights reserved.<br>
    <i>'Building AI that empowers the future!'</i>
</div>
""", unsafe_allow_html=True)
