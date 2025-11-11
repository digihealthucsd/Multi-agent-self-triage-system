# TriageMD – Local Setup Notes

A small triage assistant that combines a FastAPI backend, a React frontend, and a set of AMA flowcharts.

---

## What’s inside
- `backend/` – FastAPI app that wraps the multi-agent triage logic (retrieval, decision, and chat agents).
- `frontend/` – Vite + React (with React Flow) for the web UI.
- `Flowcharts/` – Flowchart metadata and the Python definitions for each graph.
- `System/` and `Utils/` – Original multi-agent implementation that the API calls under the hood.

---

## Requirements
the stack is minimal:

- Python 3.10+ (using a virtualenv in `backend/venv`)
- Node.js 18+
- An OpenAI API key (the code looks for `OPENAI_API_KEY` in a `.env` file at repo root)

also keys for Anthropic, Gemini, or DeepSeek if you want to swap models.

---

## Backend – run FastAPI locally

```bash
cd backend
python -m venv venv          # only the first time
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

By default the API listens on `http://localhost:8000`. 

---

## Frontend – run the React dev server

```bash
cd frontend
npm install
npm run dev
```

Vite serves the UI on `http://localhost:5173`. It expects the backend API at `http://localhost:8000` (configured in `frontend/.env.development`).

---

## Environment variables

1. Create a `.env` file at the repo root:
   ```
   OPENAI_API_KEY=sk-xxxx
   ```
   (Add other provider keys if you plan to use them.)

2. The backend loads this file before starting FastAPI, so you don’t have to edit code to switch keys.

---

## End-to-end test

1. Start the backend (port 8000).
2. Start the frontend (port 5173).
3. Visit `http://localhost:5173` and follow the flow:
   - Choose “Myself”.
   - Fill in name / sex / age.
   - Start the chat and type something like “I feel generally ill and tired”.
   - The UI should show one primary flowchart plus two alternates, the graph should render on the left, and chatting “Yes/No” should highlight the path.

---

## Notes
- The retrieval endpoint now returns the LLM-selected flowchart and two (or three) alternates so the UI can show multiple options.
- All third-party dependencies are pinned in the backend requirements file and the frontend `package.json`.
