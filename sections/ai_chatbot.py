import streamlit as st

def show_chatbot_project():
    # Project Heading with color change
    st.markdown("""
    <div style="padding: 20px; background: rgba(0, 0, 0, 0.7); 
                border-radius: 15px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);">
        <h1 style='text-align: center; color: #FFD700;'>🤖 YASH AI Chatbot</h1>
    </div>
    """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("""
    ### 📄 Project Overview
    This AI chatbot is designed to provide intelligent, real-time responses based on user queries. 
    Built using **Python**, **Streamlit**, and **MongoDB**, with integration of the 
    **Google Gemini API** for enhanced conversational capabilities.
    """)

    # Architecture
    st.markdown("""
    ### 🏗️ Architecture
    The project follows a modular architecture:
    1. **User Interface:** Developed with **Streamlit** for interactive UI.  
    2. **API Integration:** Integrated with **Google Gemini API** for NLP capabilities.  
    3. **Database Management:** Uses **MongoDB** and **SQLite** for chat history storage.  
    4. **Deployment:** Containerized with **Docker** and deployed on **AWS EC2**.  
    """)

    # Key Features
    st.markdown("""
    ### 🔹 Key Features
    - ✅ Integrated with **Google Gemini API** for advanced NLP responses.  
    - ✅ Stores chat history in **MongoDB** for session-based memory.  
    - ✅ Utilizes **SQLite** for fast and temporary chat history storage.  
    - ✅ Provides a **Show/Hide Chat History** toggle for improved readability.  
    - ✅ Deployed securely using **Docker** on **AWS EC2** for scalability and stability.  
    """)

    # Deployment Guide
    st.markdown("""
    ### 🚀 Deployment Guide
    **Docker Setup:**  
    ```bash
    docker build -t yash-chatbot .
    docker run -p 8501:8501 yash-chatbot
    ```

    **AWS CI/CD Deployment:**  
    ```bash
    ecr_login=$(aws ecr get-login-password --region <region>)
    docker tag yash-chatbot <aws-account-id>.dkr.ecr.<region>.amazonaws.com/yash-chatbot
    docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/yash-chatbot
    ```

    Then deploy the image on **AWS EC2** with:
    ```bash
    ssh -i "your-key.pem" ubuntu@your-ec2-instance
    sudo docker pull <aws-ecr-uri>
    sudo docker run -p 8501:8501 <aws-ecr-uri>
    ```
    """)

    # Future Enhancements
    st.markdown("""
    ### 🔮 Future Enhancements
    - 🚀 Improve AI responses with fine-tuned models.  
    - 🚀 Implement caching for faster database queries.  
    - 🚀 Deploy using **Kubernetes** for auto-scaling capabilities.  
    """)

    # Contact Information
    st.markdown("""
    ---
    **Author:** Yaswanth Panchakarla  
    ✉️ Email: yaswanthpanchakarla1@gmail.com  
    🔗 GitHub: [Yaswanth191](https://github.com/Yaswanth191/Chatbot-Streamlit)  
    """)
