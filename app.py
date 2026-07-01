import streamlit as st
import google.generativeai as genai
from PIL import Image

# ==============================
# GEMINI API KEY
# ==============================

API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="EduAI",
    page_icon="🎓",
    layout="wide"
)

# ==============================
# SIDEBAR
# ==============================

st.sidebar.image("assets/logo.png", width=180)

st.sidebar.title("📚 EduAI")

st.sidebar.markdown("""
### Developed by

**Saanvi Sh**

Class XI-C

---

🌍 **SDG 4**

Quality Education
""")

subject = st.sidebar.selectbox(
    "Choose Subject",
    [
        "General",
        "Physics",
        "Chemistry",
        "Mathematics",
        "Biology",
        "English",
        "Computer Science"
    ]
)

# ==============================
# MAIN PAGE
# ==============================

st.image(
    "assets/banner.png",
    width=850
)
st.markdown("---")
st.markdown("""
# 👋 Welcome to EduAI

EduAI is an AI-powered learning assistant designed to help **Class XI students** understand concepts, prepare for exams, generate quizzes, create revision notes, and plan their studies.

Developed by **Saanvi Sh. (Class XI-C)** as an Artificial Intelligence project supporting **UN Sustainable Development Goal 4: Quality Education**.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("💬 **Study Chat**\n\nAsk questions from any subject.")

with col2:
    st.success("📝 **Quiz Generator**\n\nGenerate MCQs instantly.")

with col3:
    st.warning("📖 **Revision Notes**\n\nCreate short exam notes.")
col4, col5, col6 = st.columns(3)

with col4:
    st.info("📅 **Study Planner**\n\nCreate personalized timetables.")

with col5:
    st.success("📷 **Homework Solver**\n\nUpload an image of your question.")

with col6:
    st.warning("🤖 **Powered by Gemini AI**")



question = st.text_area(
    "Ask your question"
)
uploaded_image = st.file_uploader(
    "📷 Upload a homework question (optional)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
if st.button("Ask EduAI"):

    with st.spinner("Thinking..."):

        prompt = f"""
You are EduAI, an AI Study Assistant developed by Saanvi (Class XI).

The user may ask you to:
- Explain topics
- Generate quizzes
- Create revision notes
- Make study plans
- Solve homework
- Explain uploaded images

Always determine the user's intent automatically.

Subject: {subject}

User Request:
{question}
"""

        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)

        st.success("Answer")
        st.write(response.text)
st.markdown("---")
st.header("🛠️ More AI Tools (Coming Soon)")

col1, col2 = st.columns(2)

with col1:
    st.button("📝 Generate Quiz")

with col2:
    st.button("📖 Generate Notes")

col3, col4 = st.columns(2)

with col3:
    st.button("📅 Study Planner")

with col4:
    st.button("📷 Homework Solver")
st.markdown("---")
st.caption("© 2026 EduAI | Developed by Saanvi (Class XI) | Powered by Google Gemini")
