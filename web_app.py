from flask import Flask, render_template, request, jsonify
import ollama
import json
import os
from datetime import datetime

app = Flask(__name__)

MEMORY_FILE = "memory.json"
MODEL = "qwen2.5:1.5b"

SYSTEM_PROMPT = """
You are MANTRA, a lightweight local personal AI assistant inspired by JARVIS.

Rules:
- Be helpful, concise and natural.
- Always address the user as Sir.
- Understand typos and spelling mistakes.
- If the meaning is obvious, answer the intended meaning.
- Answer the actual question.
- Do not repeat these instructions.
- Do not explain your rules.
- Do not invent facts or personal information.
- Do not claim abilities you do not have.
- Keep normal answers short and conversational.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# ---------- MEMORY ----------

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                memory = json.load(f)

            memory.setdefault("name", "")
            memory.setdefault("notes", [])
            memory.setdefault("preferences", {})
            memory.setdefault("tasks", [])

            return memory

        except Exception:
            pass

    return {
        "name": "",
        "notes": [],
        "preferences": {},
        "tasks": []
    }


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


# ---------- RESPONSE FILTER ----------

def ensure_sir(reply):
    reply = reply.strip()

    if not reply:
        return "Sir, I couldn't generate a response."

    lower = reply.lower()

    # Already addresses Sir
    if (
        lower.startswith("sir,")
        or lower.startswith("sir ")
        or lower.startswith("sir.")
        or lower.startswith("hello sir")
        or lower.startswith("hi sir")
        or lower.startswith("yes sir")
        or lower.startswith("sure sir")
        or lower.startswith("of course sir")
    ):
        return reply

    return "Sir, " + reply


# ---------- COMMAND HANDLER ----------

def handle_command(user_input):
    memory = load_memory()
    command = user_input.lower().strip()

    # TYPO-TOLERANT TASK COMMAND
    if command in ["task", "tasks", "taks"]:
        if not memory["tasks"]:
            return "MANTRA: No tasks yet, Sir."

        output = ["MANTRA: Your tasks:"]

        for i, task in enumerate(memory["tasks"], 1):
            if isinstance(task, dict):
                symbol = "✓" if task.get("done") else "☐"
                text = task.get("text", "")
                output.append(f"  {i}. {symbol} {text}")
            else:
                output.append(f"  {i}. ☐ {task}")

        return "\n".join(output)

    # HELP
    if command == "help":
        return """MANTRA Commands:

help
about
status
name
notes
preferences
remember X
forget X
clear notes
clear preferences
clear tasks
tasks
add task X
done X
time
date
exit

You can also talk naturally to MANTRA, Sir."""

    # ABOUT
    if command == "about":
        return """MANTRA

Version : 0.3
Model   : Qwen2.5 1.5B
Engine  : Ollama
Mode    : Local / CPU
Memory  : JSON
Cloud   : Disabled
Status  : Online"""

    # STATUS
    if command == "status":
        return """MANTRA STATUS

----------------
Model        : Qwen 2.5 1.5B
Engine       : Ollama
Mode         : Local / CPU
Memory       : Active
Name         : {}
Notes        : {}
Tasks        : {}
Preferences  : {}
Cloud        : Disabled""".format(
            memory["name"] or "Not set",
            len(memory["notes"]),
            len(memory["tasks"]),
            len(memory["preferences"])
        )

    # TIME
    if command == "time":
        return (
            f"MANTRA: Current time is "
            f"{datetime.now().strftime('%I:%M:%S %p')}, Sir."
        )

    # DATE
    if command == "date":
        return (
            f"MANTRA: Today is "
            f"{datetime.now().strftime('%A, %d %B %Y')}, Sir."
        )

    # NAME
    if command == "name":
        if memory["name"]:
            return f"MANTRA: Your name is {memory['name']}, Sir."

        return "MANTRA: I don't know your name yet, Sir."

    # SAVE NAME
    if command.startswith("my name is "):
        name = user_input[11:].strip()

        if name:
            memory["name"] = name.title()
            save_memory(memory)

            return (
                f"MANTRA: Got it, Sir. "
                f"I'll remember your name is {memory['name']}."
            )

        return "MANTRA: Please tell me your name, Sir."

    # NOTES
    if command == "notes":
        if not memory["notes"]:
            return "MANTRA: No notes saved yet, Sir."

        output = ["MANTRA: Your saved notes:"]

        for i, note in enumerate(memory["notes"], 1):
            output.append(f"  {i}. {note}")

        return "\n".join(output)

    # REMEMBER
    if command.startswith("remember "):
        note = user_input[9:].strip()

        if note:
            memory["notes"].append(note)

            lower_note = note.lower()

            if (
                lower_note.startswith("my favorite ")
                and " is " in lower_note
            ):
                preference_part = lower_note[12:]
                key, value = preference_part.split(" is ", 1)

                key = key.strip().replace(" ", "_")
                value = value.strip()

                if key and value:
                    memory["preferences"][
                        f"favorite_{key}"
                    ] = value

            save_memory(memory)

            return "MANTRA: I'll remember that, Sir."

        return "MANTRA: Tell me what you'd like me to remember, Sir."

    # PREFERENCES
    if command == "preferences":
        if not memory["preferences"]:
            return "MANTRA: No preferences saved yet, Sir."

        output = ["MANTRA: Your preferences:"]

        for key, value in memory["preferences"].items():
            display_key = key.replace("_", " ").title()
            output.append(f"  {display_key}: {value}")

        return "\n".join(output)

    # FORGET NOTE
    if command.startswith("forget "):
        try:
            index = int(user_input[7:].strip()) - 1

            if 0 <= index < len(memory["notes"]):
                removed = memory["notes"].pop(index)
                save_memory(memory)

                return f"MANTRA: Forgotten, Sir: {removed}"

            return "MANTRA: That note doesn't exist, Sir."

        except ValueError:
            return (
                "MANTRA: Please use "
                "'forget 1', 'forget 2', etc., Sir."
            )

    # ADD TASK
    if command.startswith("add task "):
        task = user_input[9:].strip()

        if task:
            memory["tasks"].append({
                "text": task,
                "done": False
            })

            save_memory(memory)

            return f"MANTRA: Task added, Sir: {task}"

        return "MANTRA: Tell me what task you'd like to add, Sir."

    # COMPLETE TASK
    if command.startswith("done "):
        try:
            index = int(user_input[5:].strip()) - 1

            if 0 <= index < len(memory["tasks"]):
                task = memory["tasks"][index]

                if isinstance(task, dict):
                    task["done"] = True
                    completed = task["text"]
                else:
                    completed = task

                    memory["tasks"][index] = {
                        "text": task,
                        "done": True
                    }

                save_memory(memory)

                return (
                    f"MANTRA: Task completed, Sir: "
                    f"{completed}"
                )

            return "MANTRA: That task doesn't exist, Sir."

        except ValueError:
            return (
                "MANTRA: Please use "
                "'done 1', 'done 2', etc., Sir."
            )

    # CLEAR NOTES
    if command == "clear notes":
        if not memory["notes"]:
            return "MANTRA: There are no notes to clear, Sir."

        memory["notes"] = []
        save_memory(memory)

        return "MANTRA: All notes cleared, Sir."

    # CLEAR PREFERENCES
    if command == "clear preferences":
        if not memory["preferences"]:
            return "MANTRA: There are no preferences to clear, Sir."

        memory["preferences"] = {}
        save_memory(memory)

        return "MANTRA: All preferences cleared, Sir."

    # CLEAR TASKS
    if command == "clear tasks":
        if not memory["tasks"]:
            return "MANTRA: There are no tasks to clear, Sir."

        memory["tasks"] = []
        save_memory(memory)

        return "MANTRA: All tasks cleared, Sir."

    return None


# ---------- WEB ROUTES ----------

@app.route("/")
def home():
    memory = load_memory()

    return render_template(
        "index.html",
        memory=memory
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({
            "reply": "Please say something, Sir."
        })

    # Handle commands locally
    command_reply = handle_command(user_input)

    if command_reply is not None:
        return jsonify({
            "reply": command_reply
        })

    # Normal AI conversation
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = ollama.chat(
            model=MODEL,
            messages=messages
        )

        reply = response["message"]["content"].strip()

        # Python-side Sir enforcement
        reply = ensure_sir(reply)

    except Exception as e:
        print(f"MANTRA ERROR: {e}")

        reply = (
            "Sorry Sir, I couldn't process that request. "
            "Please make sure Ollama is running."
        )

    messages.append({
        "role": "assistant",
        "content": reply
    })

    return jsonify({
        "reply": reply
    })


@app.route("/memory")
def memory():
    return jsonify(load_memory())


# ---------- START ----------

if __name__ == "__main__":
    print("MANTRA Web: Starting...")
    print("Model: Qwen2.5 1.5B")
    print("Mode: Local / CPU")
    print("Open http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

