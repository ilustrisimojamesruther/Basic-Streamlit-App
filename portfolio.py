import streamlit as st
from PIL import Image

# Set up the page with a custom theme
st.set_page_config(page_title="My Autobiography & Portfolio", layout="centered")

# Define custom CSS to apply the maroon and gold theme with a grey background
st.markdown("""
    <style>
        /* Main page background color */
        .stApp {
            background-color: #D3D3D3; /* Light grey */
        }

        /* Header styling */
        h1 {
            color: #800000; /* Maroon */
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
            font-weight: bold;
        }

        /* Subheader styling */
        h2 {
            color: #FFD700; /* Gold */
            font-family: 'Verdana', sans-serif;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 5px;
        }

        /* Text block styling */
        p, ul {
            color: #4b3832;
            font-family: 'Verdana', sans-serif;
            font-size: 1.1em;
        }

        /* Footer styling */
        footer {
            font-family: 'Verdana', sans-serif;
            color: #800000;
            text-align: center;
            margin-top: 50px;
        }

        /* Custom button style */
        .stButton>button {
            color: white;
            background-color: #800000; /* Maroon */
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Verdana', sans-serif;
        }
        .stButton>button:hover {
            background-color: #A52A2A; /* Darker Maroon */
        }

        /* Aligning images */
        .stImage img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 10px;
            border: 3px solid #FFD700; /* Gold Border */
        }
    </style>
""", unsafe_allow_html=True)

# Create separate pages for Autobiography, Portfolio, and Contact
def autobiography_page():
    st.title("My Autobiography")

    # Add a picture (adjusted size)
    image = Image.open("portfolio.jpg")
    st.image(image, caption="This is me", use_column_width=False, width=250)

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

def portfolio_page():
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

def contact_page():
    st.title("Get in Touch")

    st.write("I'd love to hear from you! Feel free to reach out using the form below.")
    st.subheader("Connect with me on social media:")
    st.write("[Instagram](https://www.instagram.com/be_like_james/)")
    st.write("[Facebook](https://www.facebook.com/ilmo45/)")

# Display a main menu for page selection
st.title("Welcome to My Personal Site")
page = st.selectbox("Choose a page", ["Autobiography", "Portfolio", "Contact"])

if page == "Autobiography":
    autobiography_page()
elif page == "Portfolio":
    portfolio_page()
elif page == "Contact":
    contact_page()

# Footer
st.markdown("---")
st.markdown("© 2024 by James Ruther I. Ilustrisimo. All rights reserved.")
