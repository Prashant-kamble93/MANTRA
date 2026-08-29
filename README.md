# MANTRA 🤖

**MANTRA - Personal AI Assistant**

MANTRA is a lightweight, local AI assistant built with Python, Ollama, and TinyLlama. It combines an LLM-powered conversational interface with deterministic commands and persistent JSON-based memory.

The project is being developed incrementally to explore practical AI application engineering, local LLM integration, memory management, task workflows, and Git-based software development.

---

## 🚀 Version

**MANTRA v0.2**

### v0.2 Highlights

* Local LLM-powered conversation
* Persistent JSON memory
* User name storage
* User preferences
* Notes management
* Task management
* Task completion tracking
* Confirmation before clearing notes/tasks
* Status and system information
* Date and time commands
* Structured command handling
* Git feature-branch workflow

---

## 🛠️ Technology Stack

* **Python 3.9**
* **Ollama**
* **TinyLlama**
* **JSON**
* **Git**
* **GitHub**
* **PowerShell**
* **CPU-based local execution**

---

## 🧠 Memory System

MANTRA stores persistent information locally in:

```text
memory.json
```

The memory structure includes:

```json
{
    "name": "",
    "notes": [],
    "preferences": {},
    "tasks": []
}
```

This allows MANTRA to retain selected information between sessions without relying on a cloud database.

---

## 📝 Notes

MANTRA can manage personal notes.

Examples:

```text
remember my favorite color is blue
```

```text
notes
```

```text
forget 1
```

```text
clear notes
```

Clearing notes requires confirmation.

---

## ⚙️ Preferences

MANTRA can store structured user preferences.

Example:

```text
preferences
```

Current preferences can include information such as:

```text
Favorite Color
Favorite Food
```

---

## ✅ Task Management

MANTRA provides a simple task-management system.

Add a task:

```text
add task learn GitHub
```

View tasks:

```text
tasks
```

Complete a task:

```text
done 1
```

Clear all tasks:

```text
clear tasks
```

Completed tasks are displayed separately from pending tasks.

---

## 💻 Available Commands

```text
help              - Show commands
about             - Show MANTRA information
status            - Show MANTRA status
name              - Show your name
notes             - Show saved notes
preferences       - Show saved preferences
remember X        - Save a note
forget X          - Delete note number X
clear notes       - Clear all notes
clear preferences - Clear all preferences
clear tasks       - Clear all tasks
tasks             - Show tasks
add task X        - Add a task
done X            - Complete task number X
time              - Show current time
date              - Show today's date
exit              - Exit MANTRA
```

---

## 🏗️ Project Structure

```text
MANTRA/
│
├── mantra.py
├── memory.json
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

### Main Components

**`mantra.py`**
Main application containing command handling, AI conversation, memory operations, notes, preferences, and task management.

**`memory.json`**
Local persistent storage for MANTRA's structured memory.

**`requirements.txt`**
Python dependencies required by the project.

**`.gitignore`**
Prevents unnecessary or environment-specific files from being committed.

---

## ▶️ How to Run

### 1. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Verify Python

```powershell
python --version
```

MANTRA v0.2 was developed with:

```text
Python 3.9.11
```

### 3. Start Ollama

Make sure Ollama is installed and the TinyLlama model is available.

### 4. Run MANTRA

```powershell
python mantra.py
```

You should see:

```text
MANTRA: Hello Sir! Type 'help' for commands or 'exit' to quit.
```

---

## 🌿 Git Workflow

MANTRA follows a versioned feature-branch workflow.

Example:

```text
main
 │
 └── feature/v0.2
        │
        ├── Development
        ├── Testing
        ├── GitHub Push
        └── Pull Request
                │
                ▼
               main
```

This keeps the stable `main` branch separate from active development.

---

## 🎯 Project Goal

The goal of MANTRA is to progressively evolve a simple local AI assistant into a more capable personal AI application.

The project is being developed version by version, focusing on:

* AI application development
* Local LLM integration
* Persistent memory
* State management
* Command architecture
* Task workflows
* Software engineering practices
* Git and GitHub collaboration workflows

---

## 📌 Roadmap

### v0.1 - Foundation

* Local AI assistant
* Ollama integration
* TinyLlama
* Basic commands
* Initial memory system

### v0.2 - Application Layer

* Persistent preferences
* Notes management
* Task management
* Task completion
* Confirmation workflows
* Improved command system
* Git feature-branch workflow

### v0.3 — Next 🚀

Further improvements to MANTRA's intelligence, usability, and architecture.

---

## 👨‍💻 Project

**MANTRA** is a personal learning and engineering project focused on building practical AI applications from the ground up.

**Built with Python + Ollama + TinyLlama.**

🚀 **One version at a time.**
