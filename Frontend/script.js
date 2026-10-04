// --- Configuration ---
const BACKEND_URL = "http://127.0.0.1:8000"; // Assuming default FastAPI local port
//const BACKEND_URL = "http://127.0.0.1:8000/api/nasm-rag-pipeline-llm";
// --- DOM Elements ---
const apiKeyInput = document.getElementById('api-key');
const baseUrlInput = document.getElementById('base-url');
const modelSelect = document.getElementById('model-select');
const saveSettingsBtn = document.getElementById('save-settings-btn');
const settingsStatus = document.getElementById('settings-status');

const chatBox = document.getElementById('chat-box');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');

// --- Functions ---

// 1. Handle Model/API Setting Update
saveSettingsBtn.addEventListener('click', async () => {
    const payload = {
        key: apiKeyInput.value.trim(),
        url: baseUrlInput.value.trim(),
        model: modelSelect.value.trim()
    };

    if (!payload.key) {
        showStatus("API Key is required!", "#f38ba8");
        return;
    }

    try {
        saveSettingsBtn.disabled = true;
        saveSettingsBtn.innerText = "Applying...";

        const response = await fetch(`${BACKEND_URL}/model_selection`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            showStatus("Settings applied successfully!", "#a6e3a1");
        } else {
            const errData = await response.json();
            showStatus("Failed to apply settings.", "#f38ba8");
            console.error(errData);
        }
    } catch (error) {
        showStatus("Backend unreachable. Is FastAPI running?", "#f38ba8");
        console.error(error);
    } finally {
        saveSettingsBtn.disabled = false;
        saveSettingsBtn.innerText = "Apply Settings";
    }
});

function showStatus(message, color) {
    settingsStatus.textContent = message;
    settingsStatus.style.color = color;
    setTimeout(() => { settingsStatus.textContent = ""; }, 4000);
}

// 2. Handle Chat Interface
function addMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender);
    
    if (sender === 'bot') {
        // 1. Strip raw citation tags like 【ccfbdaab-c4f3-498a-8e2b-c8c72d8bb18d】
        const cleanedText = text.replace(/【[^】]+】/g, '');
        
        // 2. Render Markdown into HTML
        msgDiv.innerHTML = marked.parse(cleanedText);
    } else {
        msgDiv.textContent = text;
    }
    
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function handleSendMessage() {
    const question = chatInput.value.trim();
    if (!question) return;

    // Add user message to UI
    addMessage(question, 'user');
    chatInput.value = '';
    
    // Add loading placeholder
    const loadingId = "msg-" + Date.now();
    const loadingDiv = document.createElement('div');
    loadingDiv.classList.add('message', 'bot');
    loadingDiv.id = loadingId;
    loadingDiv.textContent = "Retrieving documentation and generating answer...";
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch(`${BACKEND_URL}/query`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Query: question }) // Matching your backend dict key
        });

        const data = await response.json();
        
        // Remove loading state & display real answer
        document.getElementById(loadingId).remove();
        
        if (response.ok) {
            addMessage(data.Answer, 'bot');
        } else {
            addMessage(`Error: ${JSON.stringify(data.detail || data)}`, 'bot');
        }
    } catch (error) {
        document.getElementById(loadingId).remove();
        addMessage("Connection error. Ensure your FastAPI server is running on http://127.0.0.1:8000.", 'bot');
        console.error(error);
    }
}

// Allow sending with button or Enter key (but Shift+Enter for new line)
sendBtn.addEventListener('click', handleSendMessage);
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSendMessage();
    }
});