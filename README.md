# NeuraChat-AI-Advanced-AI-Chatbot
Advanced AI chatbot powered by Anthropic Claude API — built with Python &amp; Streamlit. Features real-time conversation, custom personality, model switching, and a premium dark UI. Deployable in one click on Streamlit Cloud.
# ⚡ NeuraChat AI — Advanced AI Chatbot

A **ChatGPT-level AI chatbot** built with Python and Streamlit, powered by the **Anthropic Claude API**. Features a premium dark UI, full conversation memory, customizable personality, and one-click Streamlit Cloud deployment.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude_API-7C3AED?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## ✨ Features

- 🧠 **Real AI Brain** — Powered by Anthropic Claude (same model as Claude.ai)
- 💬 **Conversation Memory** — Remembers full chat history across turns
- 🎛️ **Sidebar Controls** — Switch models, adjust creativity, set response length
- 🤖 **Custom Personality** — Edit the system prompt to change bot behavior
- ⚡ **Quick Suggestions** — 6 starter prompts shown on a blank chat
- ⬇️ **Export Chat** — Download full conversation as a `.txt` file
- 📊 **Session Stats** — Message count and session start time
- 🎨 **Premium Dark UI** — Glassmorphism design with animated typing indicator

---

## 🗂️ Project Structure

```
.
├── advanced_app.py       # Main Streamlit AI chatbot (Claude API powered)
├── chatbot.py            # Original rule-based chatbot (regex, no API needed)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files excluded from git
```

---

## ⚙️ Requirements

- Python 3.8+
- Anthropic API key → get one free at [console.anthropic.com](https://console.anthropic.com)

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run advanced_app.py
```

### 4. Add your API key
- Open the app in your browser (usually `http://localhost:8501`)
- Paste your **Anthropic API key** in the sidebar
- Start chatting!

---

## 🌐 Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New App** → select your repo
4. Set **Main file path** → `advanced_app.py`
5. Click **Deploy**

You'll get a public shareable link like:
```
https://your-app-name.streamlit.app
```

> 🔒 Users enter their own API key in the sidebar — your key is never stored or exposed.

---

## 🎛️ Configuration Options (Sidebar)

| Setting | Description |
|---|---|
| **API Key** | Your Anthropic API key (kept private, entered at runtime) |
| **Model** | `claude-sonnet-4-6` (smart) or `claude-haiku-4-5` (fast & cheap) |
| **System Prompt** | Define the bot's personality and behavior |
| **Temperature** | 0.0 = precise, 1.0 = creative |
| **Max Tokens** | Controls maximum response length (256–4096) |

---

## 💡 Example Prompts to Try

- `Explain quantum computing in simple terms`
- `Write a Python web scraper for a news site`
- `Help me debug this code: [paste your code]`
- `Write a professional email for a job application`
- `What is the difference between AI, ML, and Deep Learning?`
- `Write a short sci-fi story in 200 words`

---

## 🔄 Two Versions Included

| File | Type | Requires API? |
|---|---|---|
| `advanced_app.py` | Claude AI powered chatbot | ✅ Yes (free tier available) |
| `chatbot.py` | Rule-based chatbot (regex) | ❌ No |

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Anthropic](https://anthropic.com) for the Claude API
- [Streamlit](https://streamlit.io) for the web framework
