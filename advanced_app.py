"""
Advanced AI Chatbot — Powered by Claude API
============================================
A Streamlit web app that uses the Anthropic Claude API to provide
ChatGPT-level conversational AI with a premium chat UI.

Setup:
    pip install streamlit anthropic
    streamlit run advanced_app.py
"""

import streamlit as st
import anthropic
from datetime import datetime

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="NeuraChat AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS — Dark glassmorphism with teal/violet accent
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* App background */
.stApp {
    background: #080b14;
    min-height: 100vh;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color: #c9d1d9 !important; }

/* Header */
.app-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 1.4rem 0 0.6rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    margin-bottom: 1.2rem;
}
.header-icon {
    width: 42px; height: 42px;
    background: linear-gradient(135deg, #00d4aa, #7c3aed);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}
.header-text h1 {
    font-size: 1.25rem; font-weight: 700;
    color: #ffffff; letter-spacing: -0.4px;
    line-height: 1;
}
.header-text p {
    font-size: 0.72rem; color: #00d4aa;
    font-weight: 500; margin-top: 3px;
    letter-spacing: 0.04em; text-transform: uppercase;
}

/* Status badge */
.status-badge {
    margin-left: auto;
    display: flex; align-items: center; gap: 6px;
    background: rgba(0,212,170,0.1);
    border: 1px solid rgba(0,212,170,0.25);
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.72rem; color: #00d4aa; font-weight: 500;
}
.status-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: #00d4aa;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { opacity: 1; } 50% { opacity: 0.3; }
}

/* Chat container */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 0.5rem 0 1.5rem;
    min-height: 300px;
}

/* Message rows */
.msg-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
}
.msg-row.user-row { flex-direction: row-reverse; }

/* Avatars */
.av {
    width: 34px; height: 34px; border-radius: 10px;
    display: flex; align-items: center;
    justify-content: center; font-size: 0.85rem;
    flex-shrink: 0; margin-top: 2px;
}
.av-bot { background: linear-gradient(135deg,#00d4aa,#7c3aed); }
.av-user { background: linear-gradient(135deg,#3b82f6,#8b5cf6); }

/* Bubbles */
.bubble {
    max-width: 78%;
    padding: 0.75rem 1.05rem;
    border-radius: 16px;
    font-size: 0.875rem;
    line-height: 1.65;
    word-wrap: break-word;
    white-space: pre-wrap;
}
.bubble-bot {
    background: #161b27;
    border: 1px solid rgba(255,255,255,0.08);
    color: #cdd6f4;
    border-top-left-radius: 4px;
}
.bubble-user {
    background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(139,92,246,0.2));
    border: 1px solid rgba(139,92,246,0.3);
    color: #dde1ff;
    border-top-right-radius: 4px;
}
.msg-time {
    font-size: 0.65rem;
    color: rgba(255,255,255,0.22);
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
}
.user-row .msg-time { text-align: right; }

/* Typing indicator */
.typing {
    display: flex; align-items: center; gap: 5px;
    padding: 0.6rem 0.9rem;
    background: #161b27;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; border-top-left-radius: 4px;
    width: fit-content;
}
.dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: #00d4aa;
    animation: bounce 1.2s infinite;
}
.dot:nth-child(2) { animation-delay: 0.2s; }
.dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce {
    0%,60%,100% { transform: translateY(0); }
    30% { transform: translateY(-6px); }
}

/* Divider */
.divider {
    text-align: center; font-size: 0.68rem;
    color: rgba(255,255,255,0.18);
    letter-spacing: 0.08em; text-transform: uppercase;
    margin: 0.4rem 0;
}

/* Suggestion chips */
.chips { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.8rem; }
.chip-label {
    font-size: 0.68rem; color: rgba(255,255,255,0.35);
    text-transform: uppercase; letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}

/* Input */
.stTextInput > div > div > input {
    background: #0d1117 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 14px !important;
    color: #cdd6f4 !important;
    padding: 0.75rem 1rem !important;
    font-size: 0.88rem !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(0,212,170,0.5) !important;
    box-shadow: 0 0 0 3px rgba(0,212,170,0.08) !important;
}
.stTextInput > div > div > input::placeholder { color: rgba(255,255,255,0.25) !important; }

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #00d4aa, #7c3aed) !important;
    color: #ffffff !important; border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important; font-size: 0.85rem !important;
    padding: 0.65rem 1.2rem !important;
    transition: opacity 0.2s, transform 0.1s !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }
.stButton > button:active { transform: translateY(0) !important; }

/* Sidebar metrics */
.metric-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px; padding: 0.75rem 1rem;
    margin-bottom: 0.6rem;
}
.metric-label { font-size: 0.68rem; color: rgba(255,255,255,0.35); text-transform: uppercase; letter-spacing: 0.08em; }
.metric-value { font-size: 1.1rem; font-weight: 700; color: #00d4aa; margin-top: 2px; }

/* Model selector */
.stSelectbox > div > div {
    background: #0d1117 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: #cdd6f4 !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.03) !important;
    border-radius: 10px !important;
    color: #cdd6f4 !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.12); border-radius: 4px; }

/* Warning / info */
.stAlert { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────
defaults = {
    "messages": [],
    "total_tokens": 0,
    "total_messages": 0,
    "session_start": datetime.now().strftime("%H:%M"),
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Configuration")

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-...",
        help="Get your key at console.anthropic.com",
    )

    st.markdown("---")
    st.markdown("### 🧠 Model")
    model = st.selectbox(
        "Select model",
        ["claude-sonnet-4-6", "claude-haiku-4-5-20251001"],
        label_visibility="collapsed",
    )

    st.markdown("### 🎛️ Personality")
    system_prompt = st.text_area(
        "System Prompt",
        value="You are NeuraChat, a highly intelligent, friendly, and helpful AI assistant. "
              "You give clear, accurate, and thoughtful responses. You can help with coding, "
              "writing, analysis, math, general knowledge, and creative tasks.",
        height=130,
        label_visibility="collapsed",
    )

    temperature = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.7, 0.05)
    max_tokens = st.slider("Max Response Length", 256, 4096, 1024, 128)

    st.markdown("---")
    st.markdown("### 📊 Session Stats")
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Messages Sent</div>
        <div class="metric-value">{st.session_state.total_messages}</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Session Started</div>
        <div class="metric-value">{st.session_state.session_start}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_messages = 0
        st.session_state.total_tokens = 0
        st.rerun()

    if st.session_state.messages:
        log_lines = []
        for m in st.session_state.messages:
            log_lines.append(f"[{m['time']}] {m['role'].upper()}: {m['content']}")
        st.download_button(
            "⬇️ Export Chat",
            "\n\n".join(log_lines),
            file_name=f"neurachat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.7rem;color:rgba(255,255,255,0.25);text-align:center'>"
        "Powered by Anthropic Claude API<br>Built with Streamlit</div>",
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="header-icon">⚡</div>
    <div class="header-text">
        <h1>NeuraChat AI</h1>
        <p>Advanced AI Assistant</p>
    </div>
    <div class="status-badge">
        <div class="status-dot"></div>
        Online
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# API Key Check
# ─────────────────────────────────────────────
if not api_key:
    st.markdown("""
    <div style="
        background: rgba(0,212,170,0.07);
        border: 1px solid rgba(0,212,170,0.2);
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
        margin: 2rem 0;
    ">
        <div style="font-size:2rem;margin-bottom:0.75rem">🔑</div>
        <div style="color:#cdd6f4;font-weight:600;font-size:1rem;margin-bottom:0.4rem">
            Enter your Anthropic API Key to start
        </div>
        <div style="color:rgba(255,255,255,0.4);font-size:0.82rem">
            Get a free key at <b>console.anthropic.com</b> → paste it in the sidebar
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ─────────────────────────────────────────────
# Suggestions (shown when chat is empty)
# ─────────────────────────────────────────────
SUGGESTIONS = [
    "Explain quantum computing simply",
    "Write a Python web scraper",
    "Debug my code",
    "Help me write an email",
    "What is machine learning?",
    "Write a short story",
]

if not st.session_state.messages:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 0 0.5rem">
        <div style="font-size:2.2rem;margin-bottom:0.5rem">⚡</div>
        <div style="color:#ffffff;font-weight:700;font-size:1.15rem;margin-bottom:0.3rem">
            What can I help you with?
        </div>
        <div style="color:rgba(255,255,255,0.35);font-size:0.82rem;margin-bottom:1.5rem">
            Ask me anything — coding, writing, math, analysis, or just chat
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, s in enumerate(SUGGESTIONS):
        if cols[i % 3].button(s, key=f"sug_{i}", use_container_width=True):
            st.session_state.messages.append({
                "role": "user", "content": s,
                "time": datetime.now().strftime("%H:%M")
            })
            st.rerun()


# ─────────────────────────────────────────────
# Chat History Display
# ─────────────────────────────────────────────
chat_html = '<div class="chat-container">'
for i, msg in enumerate(st.session_state.messages):
    role = msg["role"]
    content = msg["content"].replace("<", "&lt;").replace(">", "&gt;")
    time = msg.get("time", "")

    if role == "user":
        chat_html += f"""
        <div class="msg-row user-row">
            <div class="av av-user">🧑</div>
            <div>
                <div class="bubble bubble-user">{content}</div>
                <div class="msg-time">{time}</div>
            </div>
        </div>"""
    else:
        chat_html += f"""
        <div class="msg-row">
            <div class="av av-bot">⚡</div>
            <div>
                <div class="bubble bubble-bot">{content}</div>
                <div class="msg-time">{time}</div>
            </div>
        </div>"""

chat_html += "</div>"
st.markdown(chat_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Input Area
# ─────────────────────────────────────────────
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        "", placeholder="Message NeuraChat...",
        key="user_input", label_visibility="collapsed"
    )
with col2:
    send_btn = st.button("Send ⚡", use_container_width=True)


# ─────────────────────────────────────────────
# API Call + Response
# ─────────────────────────────────────────────
def call_claude(messages_history, system, mdl, temp, max_tok, key):
    client = anthropic.Anthropic(api_key=key)
    api_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in messages_history
    ]
    response = client.messages.create(
        model=mdl,
        max_tokens=max_tok,
        temperature=temp,
        system=system,
        messages=api_messages,
    )
    return response.content[0].text, response.usage.input_tokens + response.usage.output_tokens


if (send_btn or user_input) and user_input.strip():
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip(),
        "time": datetime.now().strftime("%H:%M:%S"),
    })
    st.session_state.total_messages += 1

    # Show typing indicator + call API
    with st.spinner(""):
        st.markdown("""
        <div class="msg-row" style="margin-top:0.5rem">
            <div class="av av-bot">⚡</div>
            <div class="typing">
                <div class="dot"></div><div class="dot"></div><div class="dot"></div>
            </div>
        </div>""", unsafe_allow_html=True)

        try:
            reply, tokens = call_claude(
                st.session_state.messages,
                system_prompt, model, temperature, max_tokens, api_key
            )
            st.session_state.messages.append({
                "role": "assistant",
                "content": reply,
                "time": datetime.now().strftime("%H:%M:%S"),
            })
            st.session_state.total_tokens += tokens

        except anthropic.AuthenticationError:
            st.error("❌ Invalid API key. Please check your key in the sidebar.")
            st.session_state.messages.pop()
        except anthropic.RateLimitError:
            st.error("⚠️ Rate limit hit. Please wait a moment and try again.")
            st.session_state.messages.pop()
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
            st.session_state.messages.pop()

    st.rerun()
