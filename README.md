# MANTRA

**MANTRA** is a local AI personal assistant built with Python and Ollama.

## Features

* Local AI chat using TinyLlama
* Persistent user name
* Notes and memory
* Task management
* Date and time commands
* System status
* Error handling
* Runs locally without a cloud API

## Tech Stack

* Python 3.9
* Ollama
* TinyLlama
* Ollama Python library

## Commands

```text
help
status
name
notes
remember <text>
forget <number>
tasks
add task <text>
done <number>
time
date
exit
```

## Run MANTRA

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python mantra.py
```

## Architecture

```text
User
  ↓
MANTRA (Python)
  ↓
Ollama
  ↓
TinyLlama
  ↓
Response
```

## Project Status

**MANTRA V0.1 — Complete ✅**
