import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="My Autobiography & Portfolio", layout="wide")

# Sidebar content
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Autobiography", "Portfolio"])

# Autobiography Section
if page == "Autobiography":
    st.title("My Autobiography")

    # Add a picture (adjusted size)
    image = Image.open("portfolio.jpg")  
    st.image(image, caption="This is me", use_column_width=False, width=300)

    st.header("About Me")
    st.write("""
        Hello! I'm James Ruther I. Ilustrisimo, a passionate developer with a love for creating innovative solutions. 
        My journey in technology started from a young age, and over the years, I have honed my skills 
        in full-stack development. I enjoy working on both mobile and web applications, always aiming 
        to learn and grow in this ever-evolving field.

        Beyond technology, I love working out at the gym, and I'm passionate about playing basketball, 
        volleyball, and online games. These activities help me stay active and balanced, both physically 
        and mentally.
    """)

    st.subheader("Education")
    st.write("""
        - **Bachelor's Degree in Information Technology**  
          Cebu Institute of Technology University  
          2021 - 2024
    """)

    st.subheader("Skills")
    st.write("""
        - **Programming Languages**: C, C++, Python, Java, JavaScript
        - **Frameworks**: React, Flutter
        - **Databases**: MySQL, Firestore
    """)

# Portfolio Section
elif page == "Portfolio":
    st.title("My Portfolio")

    st.subheader("Projects")
    
    st.write("### Project 1: AttendEase Capstone Project || Cebu Institute Of Technology")
    st.write("""
        AttendEase is a location-aware attendance tracking application. It allows institutions to monitor attendance 
        with ease, ensuring that the right people are present at the right times. The project involved Android development 
        using Kotlin and integration with Firestore for real-time data storage.
        
        I was the leader of the project and served as the full-stack developer, overseeing both front-end and back-end 
        development to ensure seamless functionality and user experience.
    """)
    st.progress(80)

    st.write("### Project 2: Personal Website")
    st.write("""
        A responsive portfolio website created using React and Node.js. This website showcases my projects, 
        skills, and experiences, providing a professional online presence.
    """)
    st.progress(75)

# Contact Section

    st.subheader("Connect with me on social media:")
    st.write("[Instagram](https://www.instagram.com/be_like_james/)")
    st.write("[Facebook](https://www.facebook.com/ilmo45/)")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 by James Ruther I. Ilustrisimo. All rights reserved.")
