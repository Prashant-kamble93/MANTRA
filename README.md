# MANTRA 🤖

**MANTRA - Personal AI Assistant**

MANTRA is a lightweight, local personal AI assistant inspired by JARVIS. It combines an LLM-powered conversational interface with deterministic commands, persistent JSON-based memory, and a browser-based web interface.

The project is being developed incrementally to explore practical AI application engineering, local LLM integration, memory management, task workflows, web application development, and Git-based software development.

MANTRA is designed as a practical Proof of Concept (POC) with a strong focus on being local, lightweight, understandable, and RAM-conscious.

---

## 🚀 Version

**MANTRA v0.3**

### v0.3 Highlights

* Local LLM-powered conversation
* Qwen2.5 1.5B local model
* Ollama local inference
* CPU-based local execution
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
* Typo-tolerant commands
* Natural conversational interaction
* JARVIS-inspired assistant behavior
* "Sir" addressing
* Terminal-based interface
* Browser-based web interface
* MANTRA branding and logo
* Flask web application
* Local-only architecture
* RAM-conscious design
* Git feature-branch workflow

---

## 🛠️ Technology Stack

* **Python 3.9.11**
* **Ollama**
* **Qwen2.5 1.5B**
* **Flask**
* **HTML**
* **CSS**
* **JSON**
* **Git**
* **GitHub**
* **PowerShell**
* **CPU-based local execution**

---

## 🧠 MANTRA Architecture

MANTRA v0.3 contains two user interfaces connected to the same assistant architecture.

```text
                         MANTRA v0.3
                              |
               +--------------+--------------+
               |                             |
         Terminal Interface             Web Interface
               |                             |
               +--------------+--------------+
                              |
                       Command Handler
                              |
               +--------------+--------------+
               |                             |
       Deterministic Commands          AI Conversation
               |                             |
       +-------+-------+              Qwen2.5 1.5B
       |       |       |                    |
     Notes   Tasks   Memory              Ollama
       |       |       |                    |
       +-------+-------+--------------------+
                              |
                         memory.json
                              |
                    Persistent Local Memory
```

### Architecture Philosophy

MANTRA follows a simple hybrid approach:

**Python handles predictable operations.**

Examples:

* Tasks
* Notes
* Preferences
* Name
* Date
* Time
* Status
* Help
* Other deterministic commands

**Qwen2.5 1.5B handles natural conversation.**

This prevents simple commands from unnecessarily depending on the language model.

---

## 🎯 Core Design Principles

MANTRA v0.3 is intentionally designed without unnecessary complexity.

| Requirement          | MANTRA v0.3 |
| -------------------- | ----------- |
| Cloud dependency     | ❌           |
| Huge model           | ❌           |
| Over-engineering     | ❌           |
| Local execution      | ✅           |
| Persistent memory    | ✅           |
| Terminal interface   | ✅           |
| Web interface        | ✅           |
| Open-source POC      | ✅           |
| RAM-conscious design | ✅           |
| Natural conversation | ✅           |
| Typo tolerance       | ✅           |

The main idea is:

> Small model + local execution + simple architecture + useful assistant features.

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

The memory system is intentionally simple and uses a local JSON file instead of a separate database service.

---

## 👤 User Name

MANTRA can remember the user's name.

Example:

```text
my name is Prashant
```

Then:

```text
name
```

MANTRA can respond with the stored name.

Example:

```text
MANTRA: Your name is Prashant, Sir.
```

---

## 📝 Notes

MANTRA can store simple personal notes.

Save a note:

```text
remember learn Python
```

View saved notes:

```text
notes
```

Delete a note:

```text
forget 1
```

Clear all notes:

```text
clear notes
```

MANTRA asks for confirmation before destructive clear operations when supported by the command system.

---

## ⭐ Preferences

MANTRA can store structured user preferences.

Example:

```text
remember my favorite color is blue
remember my favorite food is misal pav
```

View preferences:

```text
preferences
```

Current preferences can include information such as:

```text
Favorite Color
Favorite Food
```

Preferences are stored locally inside `memory.json`.

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

Example:

```text
MANTRA: Your tasks:
  1. ✓ learn GitHub
  2. ☐ build MANTRA v0.4
```

---

## ✍️ Typo-Tolerant Commands

One of the improvements in v0.3 is simple typo tolerance.

The user does not always need to type a command perfectly.

For example:

```text
taks
```

can be understood as:

```text
tasks
```

This makes MANTRA feel more like a natural assistant instead of a strict command-line program.

The goal is not to guess wildly.

MANTRA should handle obvious spelling mistakes when the intended meaning is clear.

---

## 💬 Natural Conversation

MANTRA v0.3 supports normal conversational input.

Example:

```text
You: what is Python?

MANTRA: Python is a programming language...
```

Natural conversation is handled by the local Qwen2.5 1.5B model through Ollama.

The Python application controls the assistant architecture and deterministic commands.

---

## 🤖 JARVIS-Inspired Behavior

MANTRA is inspired by the concept of Tony Stark's JARVIS.

The goal is to create a practical open-source assistant with a similar high-level idea:

```text
User
  ↓
MANTRA
  ↓
Understands request
  ↓
Uses command system or local AI
  ↓
Responds naturally
```

MANTRA is designed to:

* Respond naturally
* Be concise
* Address the user as **Sir**
* Understand obvious typing mistakes
* Use conversation context
* Avoid inventing personal information
* Avoid claiming abilities it does not have
* Execute available local commands
* Maintain local memory
* Work locally without a cloud AI service

MANTRA does **not** claim to have the fictional abilities of JARVIS.

The project is a practical JARVIS-inspired POC.

---

## 👨‍💻 Assistant Behavior Rules

MANTRA follows a simple set of behavioral rules.

### Be helpful

MANTRA should provide useful answers when the user asks a question.

### Be concise

MANTRA should avoid unnecessary long responses when a short answer is sufficient.

### Address the user as Sir

MANTRA is designed to address the user as:

```text
Sir
```

### Understand obvious typos

If the user's intended meaning is obvious, MANTRA should try to understand the request instead of failing because of a spelling mistake.

### Do not invent personal information

MANTRA should not make up facts about the user.

### Do not claim unsupported abilities

MANTRA should not pretend it can perform actions that are not actually implemented.

### Use conversation context

MANTRA should use the available conversation context when generating responses.

---

## 🌐 Web Interface

MANTRA v0.3 introduces a browser-based interface.

The web application is built using Flask.

Start the web application:

```powershell
python web_app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The web interface provides:

* MANTRA branding
* MANTRA logo
* Chat interface
* Natural AI conversation
* Command handling
* Persistent memory
* JARVIS-inspired visual styling
* Local Ollama integration

The web interface communicates with the Python backend through Flask routes.

---

## 💻 Terminal Interface

MANTRA continues to support the original terminal interface.

Start:

```powershell
python mantra.py
```

You should see:

```text
MANTRA: Hello Sir! Type 'help' for commands or talk naturally.
```

The terminal interface provides access to the same core assistant functionality.

---

## 🌐 Web Application Flow

The web version follows this basic flow:

```text
Browser
   |
   v
index.html
   |
   v
Flask /chat route
   |
   v
MANTRA Python logic
   |
   +------> Known command
   |             |
   |             v
   |          Command result
   |
   +------> Normal conversation
                 |
                 v
              Ollama
                 |
                 v
          Qwen2.5 1.5B
                 |
                 v
              Response
                 |
                 v
              Browser
```

---

## 📋 Available Commands

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

## 📊 Status Information

MANTRA can display information about its current state.

Example:

```text
status
```

Example output:

```text
MANTRA STATUS
----------------
Model        : Qwen 2.5 1.5B
Engine       : Ollama
Mode         : Local / CPU
Memory       : Active
Name         : Prashant
Notes        : 2
Tasks        : 2
Preferences  : 2
Cloud        : Disabled
```

This provides a quick overview of the current MANTRA environment.

---

## 📁 Project Structure

```text
MANTRA/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── mantra.py
├── web_app.py
├── mantra_v0.2_backup.py
├── memory.json
├── README.md
├── requirements.txt
└── .gitignore
```

### Main Components

**`mantra.py`**

Main terminal application containing:

* Command handling
* AI conversation
* Memory operations
* Notes
* Preferences
* Tasks
* Task completion
* Status information
* Date/time functions

**`web_app.py`**

Flask-based web application providing the browser interface.

**`memory.json`**

Local persistent storage for MANTRA's structured memory.

**`templates/index.html`**

HTML structure for the MANTRA web interface.

**`static/style.css`**

Styling for the MANTRA web interface.

**MANTRA Logo**

The MANTRA logo is implemented directly in the web interface using HTML/CSS. A separate logo image file is not required.

**`requirements.txt`**

Python packages required to run MANTRA.

**`.gitignore`**

Prevents unnecessary environment-specific files from being committed.

**`mantra_v0.2_backup.py`**

Backup copy of the previous v0.2 implementation.

---

## ⚙️ Installation

### 1. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Verify Python

```powershell
python --version
```

MANTRA v0.3 was developed with:

```text
Python 3.9.11
```

### 3. Install Python dependencies

```powershell
pip install -r requirements.txt
```

Required packages include:

```text
Flask==3.1.3
ollama==0.6.2
```

### 4. Verify Ollama

Make sure Ollama is installed.

Check:

```powershell
ollama --version
```

### 5. Verify the model

Run:

```powershell
ollama list
```

The required model is:

```text
qwen2.5:1.5b
```

If the model is not installed:

```powershell
ollama pull qwen2.5:1.5b
```

---

## ▶️ How to Run

### Terminal Version

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python mantra.py
```

Expected:

```text
MANTRA: Hello Sir! Type 'help' for commands or talk naturally.
```

### Web Version

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python web_app.py
```

Expected:

```text
MANTRA Web: Starting...
Open http://127.0.0.1:5000
```

Open the address in a browser:

```text
http://127.0.0.1:5000
```

---

## 🧪 Testing

MANTRA v0.3 should be tested through both interfaces.

### Terminal Tests

Test:

```text
help
name
notes
preferences
tasks
status
time
date
```

Test natural conversation:

```text
what is Python?
```

Test typo tolerance:

```text
taks
helo mantra
```

Test memory:

```text
remember my favorite color is blue
preferences
```

Test tasks:

```text
add task test task
tasks
done 1
tasks
```

### Web Tests

Open:

```text
http://127.0.0.1:5000
```

Test:

* Normal conversation
* Commands
* Typo handling
* Memory
* Tasks
* Preferences
* "Sir" addressing
* UI responsiveness

---

## 💾 RAM-Conscious Design

RAM usage was an important design consideration for MANTRA v0.3.

Instead of using a large language model, MANTRA uses:

```text
Qwen2.5 1.5B
```

The model runs locally through:

```text
Ollama
```

This keeps the project significantly lighter than using a large local model.

MANTRA intentionally avoids:

* Huge AI models
* Multiple AI models running simultaneously
* Cloud AI dependencies
* Unnecessary databases
* Complex agent frameworks
* Unnecessary background services

Actual RAM usage depends on:

* Operating system
* Ollama
* Model runtime
* Other running applications
* Available system memory

The objective is not to guarantee a specific RAM number, but to keep the architecture lightweight and practical.

---

## ☁️ Cloud Dependency

MANTRA v0.3 is designed for local execution.

Normal AI operation does not require a cloud API.

The architecture is:

```text
User
 ↓
MANTRA
 ↓
Ollama
 ↓
Qwen2.5 1.5B
 ↓
Local response
```

This makes MANTRA suitable as a local AI POC.

---

## 🔒 Privacy and Local Memory

MANTRA's structured memory is stored locally in:

```text
memory.json
```

There is no cloud database required for the memory system.

Users should still avoid storing:

* Passwords
* API keys
* Financial information
* Authentication credentials
* Other sensitive secrets

inside `memory.json`.

---

## 🧩 Why Qwen2.5 1.5B?

The v0.3 model was selected with the project's hardware limitations and POC requirements in mind.

The goal was to find a practical balance between:

```text
Model capability
       +
Local execution
       +
RAM usage
       +
Simple setup
```

Qwen2.5 1.5B provides a lightweight local model suitable for experimenting with a JARVIS-style assistant without requiring a large model.

---

## 🔄 Version History

### v0.1 - Foundation

* Initial MANTRA concept
* Local AI assistant
* Ollama integration
* TinyLlama
* Basic commands
* Initial memory system

---

### v0.2 - Application Layer

* Persistent JSON memory
* User name storage
* User preferences
* Notes management
* Task management
* Task completion
* Confirmation workflows
* Status and system information
* Date and time commands
* Structured command handling
* Improved command system
* Git feature-branch workflow

A backup of this version is retained as:

```text
mantra_v0.2_backup.py
```

---

### v0.3 - Local JARVIS-Style POC

* Replaced TinyLlama with Qwen2.5 1.5B
* Improved local AI conversation
* Added typo-tolerant command handling
* Improved conversational behavior
* Added "Sir" addressing
* Added terminal + natural conversation flow
* Added Flask web application
* Added browser-based UI
* Added MANTRA logo and branding
* Added web styling
* Connected web UI with local MANTRA backend
* Maintained persistent JSON memory
* Maintained notes, preferences, and tasks
* Added RAM-conscious architecture
* Removed unnecessary cloud dependency
* Kept the architecture simple
* Continued Git feature-branch workflow

---

## 🌿 Git Workflow

MANTRA follows a versioned feature-branch workflow.

Example:

```text
main
 │
 └── feature/v0.3
        │
        ├── Development
        ├── Testing
        ├── UI Development
        ├── Documentation
        ├── Final Verification
        │
        └── Pull Request
                │
                ▼
               main
```

This keeps the stable `main` branch separate from active development.

Typical workflow:

```powershell
git status
git add .
git commit -m "MANTRA v0.3"
git push
```

---

## 🗂️ Development Approach

MANTRA is intentionally developed one version at a time.

The development approach is:

```text
Build
 ↓
Test
 ↓
Fix
 ↓
Improve
 ↓
Document
 ↓
Git commit
 ↓
GitHub
```

Each version builds on the previous version instead of rebuilding the entire project.

---

## 🎯 Project Goal

The goal of MANTRA is to progressively evolve a simple local AI assistant into a more capable personal AI application.

The project focuses on:

* AI application development
* Local LLM integration
* Persistent memory
* State management
* Command architecture
* Natural language interaction
* Typo tolerance
* Task workflows
* Web application development
* Software engineering practices
* Git and GitHub workflows
* Lightweight local AI architecture

---

## 🗺️ Roadmap

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

### v0.3 - Local JARVIS-Style POC

* Qwen2.5 1.5B
* Local AI conversation
* Typo-tolerant commands
* Natural interaction
* "Sir" addressing
* Persistent memory
* Terminal interface
* Web interface
* MANTRA logo
* MANTRA web styling
* Flask integration
* RAM-conscious architecture
* Local-first operation

### Future Versions

Future versions may explore improvements such as:

* Better conversation context
* More robust intent recognition
* Additional local tools
* Improved UI
* Better memory organization
* Voice interaction
* More assistant capabilities

Future features will only be added when they provide real value without unnecessarily increasing system requirements or complexity.

---

## 🚫 What MANTRA v0.3 Does NOT Use

MANTRA v0.3 intentionally avoids:

```text
❌ Cloud AI dependency
❌ Huge language models
❌ Multiple large models
❌ Cloud database
❌ Complex agent framework
❌ Unnecessary microservices
❌ Over-engineered architecture
```

The purpose is to keep MANTRA:

```text
Local
Lightweight
Understandable
Practical
Expandable
```

---

## 🏗️ Project Philosophy

MANTRA is not intended to be a production-scale enterprise AI platform.

It is a practical Proof of Concept.

The project demonstrates how a personal AI assistant can be built step-by-step using simple technologies.

The philosophy is:

> Start small. Make it work. Understand it. Improve it.

---

## 📌 Current v0.3 Status

MANTRA v0.3 currently includes:

```text
Terminal Interface       ✅
Web Interface            ✅
MANTRA Branding          ✅
MANTRA Logo              ✅
Local AI                 ✅
Qwen2.5 1.5B             ✅
Ollama                   ✅
Persistent Memory        ✅
Notes                    ✅
Preferences              ✅
Tasks                    ✅
Task Completion          ✅
Typo Tolerance           ✅
Natural Conversation     ✅
Sir Addressing           ✅
Local CPU Mode           ✅
Cloud Dependency         ❌
Huge Model               ❌
Over-engineering         ❌
```

---

## 👨‍💻 Project

**MANTRA** is a personal learning and engineering project focused on building practical AI applications from the ground up.

The project demonstrates how a lightweight local AI assistant can combine:

```text
Python
+
Ollama
+
Qwen2.5 1.5B
+
JSON Memory
+
Flask
+
HTML/CSS
+
Git/GitHub
```

into a simple JARVIS-inspired personal assistant.

---

## 🧠 Final v0.3 Philosophy

```text
Small model.
Local AI.
Simple architecture.
Persistent memory.
Useful commands.
Natural conversation.
Typo tolerance.
Web + Terminal.
MANTRA branding.
No cloud dependency.
No huge model.
No unnecessary complexity.

MANTRA v0.3
A practical JARVIS-inspired local AI POC.
```

🚀 **One version at a time.**

**Built with Python + Ollama + Qwen2.5 1.5B + Flask.**
