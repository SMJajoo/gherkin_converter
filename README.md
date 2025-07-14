---

# 🚗 Vehicle Gherkin Scenario Generator

This Streamlit app converts free-form vehicle testing scenarios into structured **Gherkin syntax** using a combination of **Google's Gemini 1.5 model** and a set of predefined templates.

---

## ✨ Features

* 🔍 **Template-Based Generation**: Uses Gherkin templates to ensure consistent structure.
* 🤖 **LLM-Powered**: Leverages Gemini 1.5 for intelligent language understanding.
* 🧠 **RAG Architecture**: Combines retrieval and generation for context-aware outputs.
* 🖥️ **Simple Web Interface**: Built with Streamlit for easy usage.

---

<img width="932" height="877" alt="image" src="https://github.com/user-attachments/assets/9c1297b2-d060-4afc-94b4-4d2347724110" />


## 📁 File Structure

```
├── app.py         # Main application code
├── gherkin_templates.txt          # Contains Gherkin syntax templates
├── requirements.txt (optional)   # Python dependencies
```

---

## 🚀 Getting Started

### 1. **Install Dependencies**

```bash
pip install streamlit langchain faiss-cpu google-generativeai langchain-google-genai
```

### 2. **Set Your API Key**

Set your Google API key as an environment variable:

```bash
export GOOGLE_API_KEY=your_api_key_here  # macOS/Linux
# OR
set GOOGLE_API_KEY=your_api_key_here     # Windows
```

### 3. **Run the App**

```bash
streamlit run app.py
```

---

## 📝 Example Usage

**Input:**

```
The vehicle is moving at 80 km/h and the lane-keeping assist is enabled.
```

**Output (Gherkin):**

```gherkin
Feature: Lane Keeping Assist
Scenario: Lane keeping while vehicle is in motion
Given the vehicle speed is > 80 km/h
And the lane-keeping assist feature is enabled
Then the vehicle shall maintain a distance of 1.5 meters
```

---

## 📌 License

This project is for educational and prototyping purposes.

---
