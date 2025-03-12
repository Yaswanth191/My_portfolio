import streamlit as st
import time

def show_resume():
    st.markdown("## 📄 My Resume")

    # Improved download button with attractive styling
    resume_url = f"https://github.com/Yaswanth191/Yaswanth_Resume/blob/main/Your_new_CV__1_%20(2).pdf?nocache={int(time.time())}"
    
    st.markdown(f"""
        <div style="
            display: flex; 
            justify-content: center; 
            margin-top: 20px;">
            <a href="{resume_url}" download target="_blank" 
               style="
                background-color: #FFD700; 
                color: #0F0F0F; 
                font-weight: bold; 
                padding: 12px 30px; 
                border-radius: 25px; 
                text-decoration: none; 
                box-shadow: 0 4px 10px rgba(255, 215, 0, 0.8); 
                transition: background-color 0.3s ease, transform 0.3s ease;">
                📥 Download Resume (PDF)
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Additional Skills Section
    st.markdown("""
    ### Skills
    - 💻 **Programming Languages:** Python, Java
    - 🤖 **AI/ML Tools:** Hugging Face, FastAPI, Streamlit
    - ☁️ **Cloud Platforms:** AWS, Docker
    - 🗂️ **Databases:** MongoDB, MySQL
    """)

