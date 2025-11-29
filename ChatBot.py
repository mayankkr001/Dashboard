import streamlit as st
import google.generativeai as genai

API_KEY = ""
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

menu = st.sidebar.selectbox(
    "Menu",
    ["Chatbot", "About", "Help"]
)

st.write("<h1 style='text-align:center;'>CHATBOT</h1>", unsafe_allow_html=True)
st.write("<h2 style='text-align:center;'>Ask Your Queries Below.</h2>", unsafe_allow_html=True)

if menu == "Chatbot":

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

# User input
    
    user_input = st.chat_input("Type Your Query")

    if user_input:
        st.session_state.messages.append(("user", user_input))
        st.chat_message("user").write(user_input)

        try:
            response = st.session_state.chat.send_message(user_input)
            bot_reply = response.text
        except Exception as e:
            bot_reply = f"Error: {e}"

        st.session_state.messages.append(("bot", bot_reply))
        st.chat_message("assistant").write(bot_reply)



elif menu == "About":
    st.subheader("About This Chatbot")
    st.write("""This chatbot uses **Google Gemini 2.5 Flash** model  and is built using **Streamlit**.""")

elif menu == "Help":
    st.subheader("Help & Instructions")
    st.write("""
    - Go to **Chatbot** from the sidebar to start chatting.
    - Type your question and press Enter.
    - The bot will respond instantly.""")