# Prompt API (FastAPI + Groq) — Minimal, Clear, Ready to Run

This repo exposes a single POST API that:

accepts a user prompt,

sends it to the Groq API using an API key, and

returns the generated text as JSON.

It’s intentionally simple and beginner-friendly.

Prerequisites:-

Python 3.10+ (3.11/3.12/3.13 are fine)

An Groq API key (create one in your Groq account → API Keys)

Git (for repo and branching)

Internet access (the API calls Groq)

Create a folder structure:-
fastapi/
│
├── api/
│   └── routes.py
│
├── groq_client/
│   └── client.py
│
├── main.py
├── requirements.txt
├── .env                # you create this (or use OS env instead)
├── .gitignore
└── README.md

1.Create and Activate a Virtual Environment
    From the fastapi/ folder:-
    python -m venv .venv
    # Windows:
    #   .venv\Scripts\activate
    # macOS/Linux:
    #   source .venv/bin/activate

2.Install Dependencies:-
    pip install -r requirements.txt

3.Run the Server:-
    uvicorn main:app --reload

4.Open the interactive docs:
    http://127.0.0.1:8000/docs

    API: Generate Text

    Endpoint: POST /api/generate
    Request body:
    {
        "prompt": "Explain Delta Lake in one sentence"
    }
    Response body:
    {
        "response": "Delta Lake is a storage layer that brings ACID transactions and schema enforcement to data lakes for reliable analytics."
    }

5.Git: Initialize Repo, Create DEV Branch, Work There

    From the fastapi/ folder:
    # 1) Initialize a local repo
    git init

    # 2) Add all files and commit
    git add .
    git commit -m "Initial commit: FastAPI + Groq minimal Prompt API"

    # 3) Create and switch to DEV branch
    git branch -M DEV
    # or: git checkout -b DEV   (if you already have a main branch)
    # Verify:
    git status
    git branch

    # 4) Create a GitHub repo (do this in GitHub UI) and copy its URL, e.g.:
    #    https://github.com/<your-username>/<your-repo>.git

    # 5) Set your origin and push DEV
    git remote add origin https://github.com/<your-username>/<your-repo>.git
    git push -u origin DEV
From now on, keep developing on DEV. You can open a Pull Request into main when you’re ready.