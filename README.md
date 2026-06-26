# 🧩 Pipeline Builder

> A visual workflow editor that enables users to create, connect, and validate data pipelines through an intuitive drag-and-drop interface.

[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat-square&logo=react&logoColor=white)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![Zustand](https://img.shields.io/badge/Zustand-4.4.0-000000?style=flat-square)](https://github.com/pmndrs/zustand)
[![React Flow](https://img.shields.io/badge/ReactFlow-11.8.0-FF007F?style=flat-square)](https://reactflow.dev/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Testing](#-testing)

---

## 🎯 Overview

**Pipeline Builder** is a full-stack application developed as a technical assessment for VectorShift. It allows users to:

- 🖱️ Drag and drop nodes onto a canvas
- 🔗 Connect nodes to define data flow
- 📝 Use Text nodes with dynamic variable detection (`{{variables}}`)
- ✅ Validate pipeline structure using DAG (Directed Acyclic Graph) detection

The application demonstrates clean code architecture, component abstraction, and full-stack integration.

---

## ✨ Features

### 🧩 **Node System**
- **9 Node Types:** Input, LLM, Text, Output, Calculator, Filter, Date/Time, JSON Parser, Email
- **Reusable Abstraction:** BaseNode component reduces code duplication by 70%
- **Customizable:** New nodes can be created in under 2 minutes

### 📝 **Smart Text Node**
- **Variable Detection:** Automatically detects `{{variableName}}` patterns
- **Dynamic Handles:** Creates input handles for each detected variable
- **Auto-Resize:** Text area grows dynamically with content

### 🔗 **Drag & Drop Interface**
- Smooth drag-and-drop from toolbar to canvas
- Connect nodes by dragging from output (right) to input (left) handles
- Zoom, pan, and reposition nodes

### ✅ **Pipeline Validation**
- Real-time validation on submission
- Returns node count, edge count, and DAG status
- User-friendly alert with results

### 🔬 **DAG Detection**
- Implements Kahn's Algorithm for cycle detection
- Time Complexity: O(V + E)
- Space Complexity: O(V)

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React 18.2.0 | Component-based UI |
| **State Management** | Zustand 4.4.0 | Lightweight state handling |
| **Node Editor** | React Flow 11.8.0 | Drag-drop & connection management |
| **Backend** | FastAPI 0.95.0 | REST API & DAG validation |
| **Language** | Python 3.8+ | Backend logic |
| **Styling** | Custom CSS | Unified design system |

---

## 📁 Project Structure

pipeline-builder/
│
├── backend/ # FastAPI Backend
│ ├── main.py # API endpoints & DAG detection
│ └── requirements.txt # Python dependencies
│
├── frontend/ # React Frontend
│ ├── public/ # Static assets
│ └── src/
│ ├── nodes/ # Node components
│ │ ├── BaseNode.js # Core abstraction ⭐
│ │ ├── inputNode.js
│ │ ├── textNode.js # Variables & auto-resize
│ │ ├── llmNode.js
│ │ ├── outputNode.js
│ │ ├── calculatorNode.js
│ │ ├── filterNode.js
│ │ ├── dateNode.js
│ │ ├── jsonNode.js
│ │ └── emailNode.js
│ ├── App.js # Main application
│ ├── submit.js # Pipeline submission
│ ├── toolbar.js # Node toolbar
│ ├── store.js # Zustand state
│ ├── draggableNode.js # Drag functionality
│ ├── index.js # Entry point
│ └── index.css # Global styles
│
├── .gitignore # Git ignore rules
├── package.json # Frontend dependencies
└── README.md # Project documentation

---

## 🚀 Getting Started

### Prerequisites

| Software | Version | Download |
|----------|---------|----------|
| **Node.js** | 18+ | [Download](https://nodejs.org/) |
| **Python** | 3.8+ | [Download](https://python.org/) |
| **npm** | 9+ | Included with Node.js |
| **pip** | Latest | Included with Python |

---
## 🎯 How it Work

1. Drag nodes from toolbar to canvas
         ↓
2. Connect nodes (output → input)
         ↓
3. Configure node content
         ↓
4. Text nodes: Type {{variables}}
         ↓
5. Click "Submit Pipeline"
         ↓
6. Backend validates pipeline
         ↓
7. Alert shows: nodes, edges, DAG status

---
## 🧪 Testing

Test Scenarios

Scenario	Expected Result

Valid pipeline (no cycles)	        is_dag: true ✅
Pipeline with cycle	        is_dag: false ⚠️
Single node	                 1 node, 0 edges
Multiple connections	        Correct edge count
Text node {{name}}	        Handle created
Auto-resize	                 Grows with content
