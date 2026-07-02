import requests
import streamlit as st

# =====================================================
# CONFIG
# =====================================================

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Multimodal RAG",
    page_icon="📄",
    layout="wide",
)

# =====================================================
# CSS
# =====================================================

st.markdown(
    """
<style>

.block-container{
    padding-top:1rem;
}

div.stButton>button{
    width:100%;
    border-radius:8px;
}

div[data-testid="stSidebar"]{
    width:340px;
}

.source-box{
    background:#F7F7F7;
    border-radius:8px;
    padding:10px;
    margin-bottom:8px;
    border-left:5px solid #4CAF50;
}

</style>
""",
    unsafe_allow_html=True,
)

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# API HELPERS
# =====================================================

def backend_health():

    try:

        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=5,
        )

        return response.status_code == 200

    except:

        return False


def uploaded_files():

    response = requests.get(
        f"{BACKEND_URL}/upload/files"
    )

    if response.status_code == 200:
        return response.json()["files"]

    return []


def upload_pdf(file):

    response = requests.post(
        f"{BACKEND_URL}/upload/",
        files={
            "file": (
                file.name,
                file.getvalue(),
                "application/pdf",
            )
        },
    )

    return response


def index_documents():

    return requests.post(
        f"{BACKEND_URL}/index/"
    )


def delete_pdf(filename):

    return requests.delete(
        f"{BACKEND_URL}/admin/pdf/{filename}"
    )


def reset_chatbot():

    return requests.post(
        f"{BACKEND_URL}/admin/reset"
    )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("📄 Multimodal RAG")

    st.divider()

    st.subheader("Upload PDF")

    uploaded_pdf = st.file_uploader(
        "Choose PDF",
        type=["pdf"],
    )

    if st.button("Upload"):

        if uploaded_pdf is None:

            st.warning("Choose a PDF first.")

        else:

            with st.spinner("Uploading..."):

                response = upload_pdf(uploaded_pdf)

                if response.status_code == 200:

                    st.success("Uploaded successfully.")

                    st.rerun()

                else:

                    st.error(
                        response.json()["detail"]
                    )

    st.divider()

    st.subheader("Uploaded PDFs")

    pdfs = uploaded_files()

    if len(pdfs) == 0:

        st.info("No PDFs uploaded.")

    else:

        for pdf in pdfs:

            col1, col2 = st.columns([8,1])

            with col1:

                st.write(f"📄 {pdf}")

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{pdf}",
                ):

                    delete_pdf(pdf)

                    st.rerun()

    st.divider()

    if st.button(
        "📚 Index Knowledge Base"
    ):

        with st.spinner("Indexing..."):

            response = index_documents()

            if response.status_code == 200:

                st.success("Index completed.")

            else:

                st.error("Index failed.")

    st.divider()

    if st.button("🧹 Reset Chatbot"):

        with st.spinner("Resetting..."):

            reset_chatbot()

            st.session_state.messages = []

            st.success("Reset completed.")

            st.rerun()

    st.divider()

    st.subheader("Status")

    if backend_health():

        st.success("Backend Connected")

    else:

        st.error("Backend Offline")

# =====================================================
# CHAT UI
# =====================================================

st.title("💬 Multimodal RAG Chatbot")

st.caption(
    "Ask questions about your uploaded PDF documents."
)

st.divider()

# -----------------------------------------------------
# Display previous conversation
# -----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):

            with st.expander("📚 Sources"):

                for source in message["sources"]:

                    st.markdown(
                        f"""
<div class="source-box">

<b>📄 {source['document']}</b><br>

Page : {source['page']}<br>

Type : {source['type']}

</div>
""",
                        unsafe_allow_html=True,
                    )

# -----------------------------------------------------
# User Question
# -----------------------------------------------------

question = st.chat_input(
    "Ask a question..."
)

if question:

    # -----------------------------
    # Display User
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -----------------------------
    # Assistant
    # -----------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        complete_answer = ""

        try:

            response = requests.post(
                f"{BACKEND_URL}/chat/",
                json={
                    "question": question,
                },
                timeout=120,
            )

            if response.status_code == 200:

                result = response.json()

                answer = result["answer"]

                sources = result["sources"]

                # ---------------------------------
                # Fake typing animation
                # ---------------------------------

                for word in answer.split():

                    complete_answer += word + " "

                    placeholder.markdown(
                        complete_answer + "▌"
                    )

                placeholder.markdown(
                    complete_answer
                )

                # ---------------------------------
                # Sources
                # ---------------------------------

                if sources:

                    with st.expander("📚 Sources"):

                        for source in sources:

                            st.markdown(
                                f"""
<div class="source-box">

<b>📄 {source['document']}</b><br>

Page : {source['page']}<br>

Type : {source['type']}

</div>
""",
                                unsafe_allow_html=True,
                            )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            else:

                placeholder.error(
                    "Chat request failed."
                )

        except Exception as e:

            placeholder.error(str(e))