import streamlit as st

def show_ai_agent_project():
    # Project Heading with color change
    st.markdown("""
    <div style="padding: 20px; background: rgba(0, 0, 0, 0.7); 
                border-radius: 15px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);">
        <h1 style='text-align: center; color: #FFD700;'>🤖 YASH AI Agent WebUI</h1>
    </div>
    """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("""
    ### 📄 Project Overview
    The Browser Use WebUI is a user-friendly web interface built using **Gradio** that allows AI agents to automate
    browser tasks using the **Playwright** library. It leverages multiple **LLMs** to generate intelligent browser interactions.
    """ )

    # Key Features
    st.markdown("""
    ### 🔹 Key Features
    - ✅ **AI-Driven Browser Automation:** Uses **Playwright** to control web browsers with AI instructions.  
    - ✅ **Supports Multiple LLMs:** Compatible with **Google Gemini**, **OpenAI**, **MistralAI**, and more.  
    - ✅ **Persistent Sessions:** Maintains active browser states for continuous tasks.  
    - ✅ **Real-Time Streaming:** Provides live updates on agent actions directly in the interface.  
    - ✅ **Recording & Tracing:** Saves session recordings for debugging and review.  
    - ✅ **Dockerized Deployment:** Ensures scalability with **Supervisord** and multi-architecture support.  
    """)

    # Technologies Used
    st.markdown("""
    ### 🛠️ Technologies Used
    - **Python (3.11+)**  
    - **Gradio** (Web UI Framework)  
    - **Playwright** (Browser Automation)  
    - **LangChain** (LLM Integration)  
    - **Docker**, **Supervisord**, **noVNC**, **Xvfb**, **VNC**  
    """)

    # Installation & Setup
    st.markdown("""
    ### ⚙️ Installation & Setup
    **Option 1: Local Installation**  
    ```bash
    git clone https://github.com/Yaswanth191/browser-use-webui.git
    cd browser-use-webui
    uv venv --python 3.11
    source .venv/bin/activate      # For macOS/Linux
    .venv\Scripts\activate        # For Windows
    uv pip install -r requirements.txt
    playwright install --with-deps chromium
    ```

    **Option 2: Docker Installation**  
    ```bash
    git clone https://github.com/Yaswanth191/browser-use-webui.git
    cd browser-use-webui
    cp .env.example .env
    docker compose up --build
    ```
    """)

    # Usage Instructions
    st.markdown("""
    ### 🌐 Usage Instructions
    Start the WebUI locally:
    ```bash
    python webui.py --ip 127.0.0.1 --port 7788 --theme Ocean
    ```

    Access the WebUI at:  
    - **WebUI:** [http://localhost:7788](http://localhost:7788)  
    - **VNC Viewer:** [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html) (Password: **vncpassword**)  
    """)

    # Project Structure
    st.markdown("""
    ### 📂 Project Structure
    ```
    browser-use-webui/
    ├── app/               # Application code
    ├── assets/            # UI assets
    ├── requirements.txt   # Python dependencies
    ├── webui.py           # Main Gradio application
    ├── Dockerfile         # Container configuration
    ├── docker-compose.yml # Docker setup
    ├── supervisord.conf   # Process management
    ├── .env.example       # Environment variable template
    ├── data/              # Temporary data (ignored)
    └── tmp/               # Temporary files (ignored)
    ```
    """)

    # Challenges & Solutions
    st.markdown("""
    ### 🚧 Challenges & Solutions
    - **Persistent Sessions:** Added **CHROME_PERSISTENT_SESSION** for maintaining browser state.  
    - **Multi-LLM Integration:** Used `.env` with dynamic variable resolution for flexible API configurations.  
    - **Deployment Stability:** Integrated **health checks** and optimized the Dockerfile for improved reliability.  
    """)

    # Achievements
    st.markdown("""
    ### 🏆 Achievements
    - ✅ Integrated support for **8+ LLM providers** for versatile AI-driven interactions.  
    - ✅ Enabled **real-time browser automation** with live streaming outputs.  
    - ✅ Deployed via **Docker** with **99.9% uptime**, ensuring stability and scalability.  
    """)

    # Future Improvements
    st.markdown("""
    ### 🔮 Future Improvements
    - 🚀 Add support for **LLaMA** and other emerging models.  
    - 🚀 Develop **unit tests** for UI functionality and agent logic.  
    - 🚀 Optimize memory usage with dynamic `shm_size` adjustments in Docker.  
    """)

    # Contact Information
    st.markdown("""
    ---
    **Author:** Yaswanth Panchakarla  
    ✉️ Email: yaswanthpanchakarla1@gmail.com  
    🔗 GitHub: [Yaswanth191](https://github.com/Yaswanth191/Yash-AI-Chatbot)  
    """)
