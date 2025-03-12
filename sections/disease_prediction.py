import streamlit as st

def show_disease_project():
    # Project Heading with color change
    st.markdown("""
    <div style="padding: 20px; background: rgba(0, 0, 0, 0.7); 
                border-radius: 15px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);">
        <h1 style='text-align: center; color: #FFD700;'>🩺 AI-Driven Disease Prediction Model</h1>
    </div>
    """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("""
    ### 📄 Project Overview
    This model predicts the likelihood of various diseases based on patient data. 
    Developed using **Python**, **scikit-learn**, and **Pandas**, with insights visualized via **Matplotlib**. 
    The model is deployed using **Docker** and hosted on **AWS**.
    """)

    # Architecture
    st.markdown("""
    ### 🏗️ Architecture
    1. **Data Preprocessing:** Handled with **Pandas** for cleaning and transformation.  
    2. **Model Training:** Utilizes **Random Forest** classifier for accurate predictions.  
    3. **Evaluation:** Achieved high accuracy with feature importance analysis.  
    4. **Deployment:** Packaged using **Docker** and deployed on **AWS EC2**.  
    """)

    # Key Features
    st.markdown("""
    ### 🔹 Key Features
    - ✅ Utilizes **Random Forest** for robust disease prediction.  
    - ✅ Visualizes important features with insightful plots.  
    - ✅ Offers secure deployment via **Docker** on **AWS EC2**.  
    - ✅ Efficiently manages data using **Pandas** and **scikit-learn**.  
    """)

    # Deployment Guide
    st.markdown("""
    ### 🚀 Deployment Guide
    **Docker Setup:**  
    ```bash
    docker build -t disease-predictor .
    docker run -p 8501:8501 disease-predictor
    ```

    **AWS CI/CD Deployment:**  
    ```bash
    ecr_login=$(aws ecr get-login-password --region <region>)
    docker tag disease-predictor <aws-account-id>.dkr.ecr.<region>.amazonaws.com/disease-predictor
    docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/disease-predictor
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
    - 🚀 Incorporate deep learning models for improved accuracy.  
    - 🚀 Implement real-time data ingestion for dynamic insights.  
    - 🚀 Add REST API endpoints for better integration with frontend applications.  
    """)

    # Contact Information
    st.markdown("""
    ---
    **Author:** Yaswanth Panchakarla  
    ✉️ Email: yaswanthpanchakarla1@gmail.com  
    🔗 GitHub: [AI-Driven-Disease-Prediction-Model](https://github.com/Yaswanth191/AI-Driven-Disease-Prediction-Model)  
    """)
