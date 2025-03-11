import streamlit as st

st.set_page_config(page_title="LangGraph agent", layout="centered")
st.title("AI Chatbot")
st.write("This is a simple chatbot that uses the LangGraph AI agent to generate responses.")

system_prompt = st.text_area("Define you agent:", height = 100, placeholder="Define your agent here..")

MODEL_NAMES_GROQ = [ "mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]    

provider=st.radio("select the provider u want to use", ("Groq", "OpenAI"))
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", height = 100, placeholder="Ask away..")
API_URL="https://ai-chatbot-5l1e.onrender.com/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")