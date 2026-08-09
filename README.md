# 🤖 AI Debugging Assistant
An AI-powered debugging assistant that analyzes source code and error messages to identify potential bugs, explain their root causes, and suggest possible fixes.
## 🚀 Features
- 🔍 Analyze source code and error messages
- 🐛 Identify potential bugs
- 💡 Explain the root cause of errors
- 🛠️ Suggest possible fixes
- 🤖 Powered by Google Gemini
- ⚙️ Configurable AI model parameters
## 🏗️ How It Works
1. The user provides source code and an error message.
2. The application processes the input.
3. A debugging prompt is created for the AI model.
4. Google Gemini analyzes the code and error.
5. The assistant returns an explanation and suggested fix.

## 🛠️ Tech Stack
- **Python** — Core programming language
- **Google Gemini API** — AI-powered code analysis
- **Pydantic** — Configuration and data validation
- **YAML** — Application configuration
- **Git & GitHub** — Version control and project hosting

## 📂 Project Structure
```text
ai-debugging-assistant/
│
├── apps/
├── config/
├── utils/
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── __init__.py

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Atiq40-cyber/ai-debugging-assistant.git
cd ai-debugging-assistant
```
### 2. Create a virtual environment
bash
python -m venv venv

### 3. Activate the virtual environment
**Windows:**
```bash
venv\Scripts\activate

### 4. Install dependencies

bash
pip install -r requirements.txt
## 🔑 API Key Configuration

This project uses the Google Gemini API for AI-powered debugging.

Before running the application, configure your Gemini API key.

### Set the API Key

Create a `.env` file in the project root:

env
GEMINI_API_KEY=your_api_key_here

## ▶️ Running the Application

Run the following command:
bash
python main.py

## 💻 Example
### Input
```python
numbers = [1, 2, 3]
print(numbers[5])
``text


### Error
```text
IndexError: list index out of range
### AI Analysis
The assistant analyzes the code and error, identifies the cause of the problem, explains why it occurred, and suggests a possible fix.
## 📸 Demo

### 1. User Input

![AI Debugging Assistant](https://raw.githubusercontent.com/Atiq40-cyber/ai-debugging-assistant/main/demo.png)






## 🚧 Future Improvements
- [ ] Support more programming languages
- [ ] Generate automated test cases
- [ ] Add code quality scoring
- [ ] Add debugging history
- [ ] Add security vulnerability detection
- [ ] Deploy the application online
