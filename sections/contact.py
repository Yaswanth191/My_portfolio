import streamlit as st

def show_contact():
    st.markdown("""
    <div style="padding: 20px; background: rgba(0, 0, 0, 0.7); 
                border-radius: 15px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);">
        <h2 style='text-align: center; color: #FFD700;'>📞 Contact Me</h2>
        <p style='text-align: center; color: #FFFFFF;'>
            📧 <b>Email:</b> <a href="mailto:yaswanthpanchakarla1@gmail.com" style="color: #FFD700;">
            yaswanthpanchakarla1@gmail.com</a><br>
            📱 <b>Mobile:</b> <a href="tel:+917671829194" style="color: #FFD700;">
            +91 7671829194</a><br>
            🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/yaswanth-panchakarla-510530291/" 
            style="color: #FFD700;">linkedin.com/in/yaswanth</a><br>
            🖥️ <b>GitHub:</b> <a href="https://github.com/Yaswanth191" 
            style="color: #FFD700;">github.com/Yaswanth191</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style='text-align: center;'>
        🚀 <b>Let's collaborate and build impactful AI solutions together!</b>
    </div>
    """, unsafe_allow_html=True)