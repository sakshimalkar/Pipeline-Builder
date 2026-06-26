# 🧩 Pipeline Builder - VectorShift Technical Assessment

A **visual workflow editor** that allows users to create, connect, and validate data pipelines through an intuitive drag-and-drop interface. Built with React.js, FastAPI, and React Flow.

## 🚀 Live Demo

- **Frontend:** [https://your-app-link.vercel.app](https://your-app-link.vercel.app) *(optional)*
- **Backend API:** `http://localhost:8000`

## ✨ Features

- **Drag & Drop Interface** – 9 node types (Input, LLM, Text, Output, Calculator, Filter, Date/Time, JSON Parser, Email)
- **Smart Text Node** – Auto-detects `{{variables}}` and creates dynamic handles
- **Auto-Resizing** – Text area grows with content
- **Pipeline Validation** – DAG detection using Kahn's algorithm
- **Full-Stack Integration** – React.js frontend + FastAPI backend

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React.js, Zustand, React Flow |
| **Backend** | FastAPI (Python) |
| **Styling** | Custom CSS |
| **State Management** | Zustand |

## 📁 Project Structure
pipeline-builder/
├── backend/
│ └── main.py # FastAPI server with DAG detection
├── frontend/
│ ├── public/
│ └── src/
│ ├── nodes/
│ │ ├── BaseNode.js # Core abstraction
│ │ ├── inputNode.js
│ │ ├── textNode.js # Variables & auto-resize
│ │ ├── llmNode.js
│ │ ├── outputNode.js
│ │ ├── calculatorNode.js
│ │ ├── filterNode.js
│ │ ├── dateNode.js
│ │ ├── jsonNode.js
│ │ └── emailNode.js
│ ├── App.js
│ ├── submit.js
│ ├── toolbar.js
│ ├── store.js
│ └── index.css
├── package.json
└── README.md

```

## 🏃 Getting Started

### Prerequisites

- Node.js 18+ ([Download](https://nodejs.org/))
- Python 3.8+ ([Download](https://python.org/))

### Backend Setup

```bash
cd backend
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

