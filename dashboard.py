import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐")

# 💕 Background
st.markdown("""
<style>
.stApp {
    background-color: #ffe6f0;
}
</style>
""", unsafe_allow_html=True)

# ⭐ Title
st.markdown("""
<h1 style='text-align: center;'>⭐ Welcome to My Portfolio</h1>
<p style='text-align: center; font-size:20px; color:#cc0066; font-weight:600;'>
Code Learner Today | Software Developer Tomorrow 💻
</p>
""", unsafe_allow_html=True)

# 👤 Image
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("image.jpg", width=200)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# 🔘 CLICKABLE MENU
menu = st.radio(
    "📌 Navigate",
    ["Home", "About Me", "Skills", "Projects", "Contact"],
    horizontal=True
)

st.markdown("---")

# 🏠 HOME
if menu == "Home":
    st.write("Welcome to my portfolio! Explore my sections above 👆")

# 👤 ABOUT
elif menu == "About Me":
    st.title("👤 About Me")
    st.write("""
    I’m an enthusiastic 3rd year Computer Science student who enjoys designing and developing applications. 
    I take pride in solving challenges and building interfaces that are both functional and easy to use.
    """)

    st.subheader("🎓 Education")
    st.write("- BS Computer Science")
    st.write("- DEBESMSCAT")

    st.subheader("🎯 Goals")
    st.write("- Continuously improve my skills as a Full Stack Developer")
    st.write("- Create practical solutions that enhance student learning and productivity")

# 💻 SKILLS
elif menu == "Skills":
    st.title("💻 Skills")

    st.subheader("Programming")
    st.write("Python")
    st.progress(75)

    st.write("JavaScript")
    st.progress(70)

    st.write("PHP")
    st.progress(20)

    st.subheader("Design")
    st.write("Canva / UI Design")
    st.progress(85)

    st.subheader("Tools")
    st.write("- GitHub")
    st.write("- VS Code")
    st.write("- Streamlit")
    st.write("- Canva")

# 📁 PROJECTS
elif menu == "Projects":
    st.title("📁 My Projects")

    projects = {
        "MIS Database System": "A system designed to manage and organize information efficiently.",
        "Environmental Puzzle Games": "An interactive game promoting environmental awareness.",
        "Student Grade Database System (SPNHS)": "A system for managing student grades and records.",
        "OS File System": "A project focused on file organization and management in operating systems.",
        "My Barista Portfolio (Personal Site)": "A personal website showcasing barista skills and experience.",
    }

    certifications = {
        "Cisco CSS Essentials Certificate": "Certification in CSS Fundamentals.",
        "Cisco HTML Essentials Certificate": "Certification in HTML basics.",
        "CSE (SimpliLearn) Certification": "Course Certification in Computer Science Engineering basics.",
    }

    for name, desc in projects.items():
        with st.expander(name):
            st.write(desc)

    st.subheader("📜 Certifications")
    for cert, desc in certifications.items():
        with st.expander(cert):
            st.write(desc)

# 📞 CONTACT
elif menu == "Contact":
    st.title("📞 Contact Me")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.error("Please fill all fields.")

    st.markdown("### 🌐 Social Links")
    st.write("- GitHub: https://github.com/")
    st.write("- Facebook: https://facebook.com/")