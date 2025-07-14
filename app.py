# vehicle_gherkin_app.py

import os
import streamlit as st
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings



# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to get response from Gemini
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text


@st.cache_resource
def load_template_index():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current file's directory
    template_path = os.path.join(current_dir, "gherkin_templates.txt")

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    documents = [Document(page_content=content)]

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", 
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    db = FAISS.from_documents(texts, embeddings)
    return db.as_retriever(), content


# Generate Gherkin scenario using Gemini + RAG
def generate_gherkin_scenario(user_input, template_context):
    prompt = f"""
        You are a vehicle testing assistant. Convert the following scenario into Gherkin steps using the templates provided below.

        ### Templates:
        {template_context}

        ### Scenario:
        {user_input}

        ### Output Format:
        Feature: <Feature Name>
        Scenario: <Scenario Description>
        Given ...
        When ...
        Then ...
        """
    return get_gemini_response(prompt)


# Streamlit UI
def main():
    st.set_page_config(page_title="Vehicle Gherkin Scenario Generator", layout="centered")
    st.title("🚗 Vehicle Scenario → Gherkin Converter")

    st.markdown("Enter a vehicle testing scenario below. The app will convert it into Gherkin steps using predefined templates.")

    user_input = st.text_area("Vehicle Testing Scenario", height=200)

    if st.button("Generate Gherkin Steps"):
        with st.spinner("Generating..."):
            retriever, template_context = load_template_index()
            result = generate_gherkin_scenario(user_input, template_context)
            st.markdown("### 🧾 Generated Gherkin Scenario")
            st.code(result, language="gherkin")


if __name__ == "__main__":
    main()
