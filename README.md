Mental Health LLM Chatbot – Fullstack App
This project is a simple full-stack chatbot interface that allows users to interact with a fine-tuned LLM model (like TinyLlama) through a React frontend and a FastAPI backend.

Project Structure
```
Mental Health LLM/
├── backend/
│   ├── server.py
│   └── [your fine-tuned model folder, e.g. final_model/]
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.js
│   └── package.json
```

Setup Instructions

1. Clone or Create Your Project Directory
Make sure your directory contains both frontend and backend folders.

2. Backend Setup (FastAPI)
Requirements:
Python 3.10+
torch, transformers, peft, fastapi, uvicorn

Install dependencies:
```
cd backend
pip install torch transformers peft fastapi uvicorn
```
Model Folder:
Place your fine-tuned model (e.g., TinyLlama with LoRA adapters) inside backend/final_model.

Run the backend:
```
uvicorn server:app --reload --port 5100
```

3. Frontend Setup (React)

 Install frontend dependencies:
 ```
 cd frontend
npm install
```

4. Chat Usage
The frontend has a simple form where you can type a mental health-related question and click “Ask”.

The React app sends a POST request to:
```
http://127.0.0.1:5100/chat
```

Request JSON format:
```
{
  "question": "Why do I feel anxious all the time?"
}
```

Expected response:
```
{
  "answer": "It's okay to feel anxious. You're not alone. Let's talk about it..."
}
```


5. Common Issues & Fixes
 CORS Error in Console

Make sure CORS is allowed in server.py:
```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

404 Not Found
Double-check that your frontend is calling /chat, and your backend endpoint is also /chat:
```
fetch("http://127.0.0.1:5100/chat", { ... })
@app.post("/chat")
async def ask_question(...):
```

422 Unprocessable Entity
Make sure you're sending the correct request body:
```
{ "question": "..." }
```

Backend not responding
Ensure you restarted the backend after changing code using:
```
uvicorn server:app --reload --port 5100
```

6. Example Folder Tree (Filled)
 ```
Mental Health LLM/
├── backend/
│   ├── server.py
│   └── final_model/
│       ├── adapter_model.bin
│       └── adapter_config.json
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
```

8. Example Conversation
```
You: I’ve been feeling sad for no reason lately.
Bot: It's completely normal to feel this way. You're not alone — do you want to talk about it?
```
10. Optional Improvements
    Add user authentication (optional)
    Save chat history
    Use a more powerful model with quantization
    Dockerize the backend for deployment
    Deploy frontend to Vercel / Netlify and backend to Render / Railway


9.License
This is a demo project for educational purposes. Not intended to replace real medical advice or mental health therapy.
