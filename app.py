import streamlit as st

from gemini_service import ask_gemini


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="centered",
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Remove default top spacing */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }

    /* Header */
    .app-header {
        padding: 10px 0 24px 0;
        border-bottom: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 25px;
    }

    .app-title {
        font-size: 32px;
        font-weight: 700;
        color: var(--text-color);
        margin: 0;
    }

    .app-subtitle {
        font-size: 16px;
        color: var(--text-color);
        opacity: 0.65;
        margin-top: 6px;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        padding: 12px 16px;
        border-radius: 16px;
        margin-bottom: 12px;
    }

    /* User message */
    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarUser"]
    ) {
        background: var(--secondary-background-color);
    }

    /* Chat input container */
    [data-testid="stChatInput"] {
        border-radius: 24px !important;
    }

    [data-testid="stChatInput"] > div {
        border-radius: 24px !important;
        border: 1px solid rgba(128, 128, 128, 0.3) !important;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15) !important;
        background: var(--secondary-background-color) !important;
    }

    [data-testid="stChatInput"] textarea {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
        font-size: 16px !important;
        padding-left: 18px !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* Send button */
    [data-testid="stChatInput"] button {
        border-radius: 50% !important;
    }

    /* Hide Streamlit footer */
    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

header_col1, header_col2 = st.columns([5, 1])


with header_col1:

    st.markdown(
        '<div class="app-header">'
        '<div class="app-title">🤖 AI Learning Assistant</div>'
        '<div class="app-subtitle">'
        'Ask anything and get an answer from Gemini.'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


with header_col2:

    st.write("")

    if st.button(
        "Clear Chat",
        use_container_width=True,
    ):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

prompt = st.chat_input(
    "Ask anything"
)


# --------------------------------------------------
# HANDLE USER INPUT
# --------------------------------------------------

if prompt:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = ask_gemini(prompt)

                st.markdown(answer)

                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as e:

                st.error(
                    "Sorry, something went wrong."
                )

                st.error(str(e))





                #this is comment