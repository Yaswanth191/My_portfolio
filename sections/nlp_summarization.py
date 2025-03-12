
import streamlit as st

def show_nlp_project():
    # Project Heading with color change
    st.markdown("""
    <div style="padding: 20px; background: rgba(0, 0, 0, 0.7); 
                border-radius: 15px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);">
        <h1 style='text-align: center; color: #FFD700;'>📚 NLP Text Summarization Project</h1>
    </div>
    """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("""
    ### 📄 Project Overview
    This project is an end-to-end text summarization system built using the **PEGASUS** model fine-tuned on the **CNN/DailyMail** dataset.  
    It efficiently summarizes lengthy text data while retaining key information.
    """)

    # Architecture
    st.markdown("""
    ### 🏗️ Architecture
    The project follows a modular pipeline approach:
    1. **Data Ingestion:** Downloads and preprocesses the dataset.  
    2. **Data Validation:** Ensures the data meets required quality checks.  
    3. **Data Transformation:** Tokenizes and prepares data for training.  
    4. **Model Training:** Fine-tunes the **PEGASUS** model for summarization.  
    5. **Model Evaluation:** Evaluates performance using metrics like **ROUGE** and **BLEU**.  
    6. **Deployment:** Exposes an API via **FastAPI** for text summarization requests.  
    """)

    # Tech Stack
    st.markdown("""
    ### 🛠️ Tech Stack
    - **Model Used:** PEGASUS (from Hugging Face Transformers)  
    - **Dataset:** CNN/DailyMail (widely used for text summarization tasks)  
    - **Programming Language:** Python 3.8+  
    - **Machine Learning:** Hugging Face Transformers  
    - **Frameworks:** FastAPI, PyTorch  
    - **Cloud & Deployment:** AWS (EC2, ECR), Docker, GitHub Actions (CI/CD)  
    - **Tracking:** Weights & Biases (optional)  
    """)

    # Installation & Setup
    st.markdown("""
    ### ⚙️ Installation & Setup
    ```bash
    git clone https://github.com/Yaswanth191/Text-Summary-project.git
    cd Text-Summary-project
    conda create -n summary python=3.8 -y
    conda activate summary
    pip install -r requirements.txt
    ```
    """)

    # Training Instructions
    st.markdown("""
    ### 📈 Training the Model
    The **PEGASUS** model is fine-tuned on the **CNN/DailyMail** dataset to enhance summarization quality.  
    To train the model, run:
    ```bash
    python main.py
    ```

    This executes the following steps:  
    1. **Data Ingestion** (downloads dataset)  
    2. **Data Validation** (performs checks)  
    3. **Data Transformation** (prepares inputs)  
    4. **Model Training** (fine-tunes the PEGASUS model)  
    5. **Model Evaluation** (validates model performance)  
    """)

    # Running the API
    st.markdown("""
    ### 🌐 Running the API
    Start the FastAPI Server:
    ```bash
    python app.py
    ```

    Available Endpoints:  
    - **`GET /`** → Redirects to API documentation  
    - **`GET /train`** → Triggers model training  
    - **`POST /predict`** → Accepts text and returns a summary  
    """)

    # Deployment Guide
    st.markdown("""
    ### 🚀 Deployment Guide
    **Docker Setup:**  
    ```bash
    docker build -t text-summarizer .
    docker run -p 8080:8080 text-summarizer
    ```

    **AWS CI/CD Deployment:**  
    ```bash
    ecr_login=$(aws ecr get-login-password --region <your-region>)
    docker tag text-summarizer <aws-account-id>.dkr.ecr.<region>.amazonaws.com/text-summarizer
    docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/text-summarizer
    ```

    Then deploy the image on **AWS EC2** with:
    ```bash
    ssh -i "your-key.pem" ubuntu@your-ec2-instance
    sudo docker pull <aws-ecr-uri>
    sudo docker run -p 8080:8080 <aws-ecr-uri>
    ```
    """)

    # Future Enhancements
    st.markdown("""
    ### 🔮 Future Enhancements
    🚀 Improve summarization accuracy with larger datasets.  
    🚀 Optimize model inference for real-time performance.  
    🚀 Implement a UI frontend for user interaction.  
    """)

    # Contact Details
    st.markdown("""
    ---
    **Author:** Yaswanth Panchakarla  
    ✉️ Email: yaswanthpanchakarla1@gmail.com  
    🔗 GitHub: [Yaswanth191](https://github.com/Yaswanth191/Text-Summary-project)  
    """)

