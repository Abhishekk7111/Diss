import streamlit as st
import openai
import os

st.set_page_config(page_title="ChatGPT Duel", layout="wide")
st.title("🤖 ChatGPT-1 vs ChatGPT-2 Debate")

openai.api_key = os.environ.get("OPENAI_API_KEY")

question = st.text_input("Ask any question:")

rounds = st.slider("Number of debate rounds:", min_value=1, max_value=5, value=3)

if st.button("Start Debate") and question.strip() != "":
    chat1 = [{"role": "user", "content": question}]
    chat2 = [{"role": "user", "content": question}]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ChatGPT-1")
    with col2:
        st.subheader("ChatGPT-2")

    for i in range(rounds):
        resp1 = openai.ChatCompletion.create(model="gpt-5", messages=chat1, temperature=0.7)
        reply1 = resp1.choices[0].message.content.strip()
        chat1.append({"role": "assistant", "content": reply1})
        chat2.append({"role": "user", "content": reply1})

        resp2 = openai.ChatCompletion.create(model="gpt-5", messages=chat2, temperature=0.7)
        reply2 = resp2.choices[0].message.content.strip()
        chat2.append({"role": "assistant", "content": reply2})
        chat1.append({"role": "user", "content": reply2})

        with col1:
            st.markdown(f"**Round {i+1}:** {reply1}")
        with col2:
            st.markdown(f"**Round {i+1}:** {reply2}")
