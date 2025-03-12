import streamlit as st

def show_introduction():
    st.markdown("""
    <div class="intro-container">
        <div class="intro-text">
            <h1>Hi, I'm Yaswanth 👋</h1>
            <p>
                💡I am an aspiring Generative AI Engineer with a passion for creating innovative solutions.<br>
                💡My expertise lies in leveraging cutting-edge technologies such as 
                <b>Artificial Intelligence</b>, <b>Natural Language Processing (NLP)</b>, 
                <b>Front End Web Development</b>, <b>Machine Learning</b>, 
                <b>Streamlit</b>, and <b>Hugging Face Transformers</b>.<br>
                💡I have worked on projects like developing AI-powered chatbots and optimizing cloud-based workflows, showcasing my ability to build impactful applications.<br>
                💡My goal is to contribute to the future of AI by solving real-world problems—explore my work to learn more!
            </p>
        </div>
        <div class="image-box">
    <img src="https://raw.githubusercontent.com/Yaswanth191/Project-Management-System/main/yaswanth_photo.jpg" 
         class="profile-image" alt="Yaswanth's Profile">
    <div class="name-text">Yaswanth Panchakarla</div>
</div>
    """, unsafe_allow_html=True)
