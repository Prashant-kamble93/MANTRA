import ollama
import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

# ---------- MEMORY ----------

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "name": "",
        "notes": [],
        "preferences": {},
        "tasks": []
    }

memory.setdefault("name", "")
memory.setdefault("notes", [])
memory.setdefault("preferences", {})
memory.setdefault("tasks", [])


def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


# ---------- AI ----------

SYSTEM_PROMPT = """
You are MANTRA, a personal AI assistant.

Rules:
- Be helpful and concise.
- Call the user Sir.
- Never ask the user to call you Sir.
- Do not invent personal information.
- Use conversation context when answering.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# ---------- START ----------

print("MANTRA: Hello Sir! Type 'help' for commands or 'exit' to quit.")


# ---------- MAIN LOOP ----------

while True:

    user_input = input("You: ").strip()
    command = user_input.lower()

    # ---------- EXIT ----------

    if command == "exit":
        print("MANTRA: Goodbye Sir!")
        break

    # ---------- HELP ----------

    elif command == "help":
        print("""
MANTRA Commands:

  help          - Show commands
  status        - Show MANTRA status
  name          - Show your name
  notes         - Show saved notes
  remember X    - Save a note
  forget X      - Delete note number X
  tasks         - Show tasks
  add task X    - Add a task
  done X        - Complete task number X
  time          - Show current time
  date          - Show today's date
  exit          - Exit MANTRA
""")
        continue

    # ---------- STATUS ----------

    elif command == "status":
        print("""
MANTRA STATUS
--------------
Model   : TinyLlama
Engine  : Ollama
Mode    : CPU
Memory  : Active
Name    : {}
Notes   : {}
Tasks   : {}
""".format(
            memory["name"] or "Not set",
            len(memory["notes"]),
            len(memory["tasks"])
        ))
        continue

    # ---------- TIME ----------

    elif command == "time":
        now = datetime.now()
        print(
            f"MANTRA: Current time is "
            f"{now.strftime('%I:%M:%S %p')}, Sir."
        )
        continue

    # ---------- DATE ----------

    elif command == "date":
        now = datetime.now()
        print(
            f"MANTRA: Today is "
            f"{now.strftime('%A, %d %B %Y')}, Sir."
        )
        continue

    # ---------- NAME ----------

    elif command == "name":
        if memory["name"]:
            print(
                f"MANTRA: Your name is {memory['name']}, Sir."
            )
        else:
            print(
                "MANTRA: I don't know your name yet, Sir."
            )
        continue

    # ---------- SAVE NAME ----------

    elif command.startswith("my name is "):
        name = user_input[11:].strip()

        if name:
            memory["name"] = name.title()
            save_memory()

            print(
                f"MANTRA: Got it, Sir. "
                f"I'll remember your name is {memory['name']}."
            )
        continue

    # ---------- SHOW NOTES ----------

    elif command == "notes":
        if not memory["notes"]:
            print("MANTRA: No notes saved yet, Sir.")
        else:
            print("MANTRA: Your saved notes:")
            for i, note in enumerate(memory["notes"], 1):
                print(f"  {i}. {note}")
        continue

    # ---------- REMEMBER ----------

    elif command.startswith("remember "):
        note = user_input[9:].strip()

        if note and note not in memory["notes"]:
            memory["notes"].append(note)
            save_memory()
            print("MANTRA: I'll remember that, Sir.")
        elif note in memory["notes"]:
            print("MANTRA: I already remember that, Sir.")
        continue

    # ---------- FORGET ----------

    elif command.startswith("forget "):
        try:
            index = int(user_input[7:].strip()) - 1

            if 0 <= index < len(memory["notes"]):
                removed = memory["notes"].pop(index)
                save_memory()

                print(
                    f"MANTRA: Forgotten, Sir: {removed}"
                )
            else:
                print(
                    "MANTRA: That note doesn't exist, Sir."
                )

        except ValueError:
            print(
                "MANTRA: Please use 'forget 1', "
                "'forget 2', etc., Sir."
            )

        continue

    # ---------- SHOW TASKS ----------

    elif command == "tasks":
        if not memory["tasks"]:
            print("MANTRA: No tasks yet, Sir.")
        else:
            print("MANTRA: Your tasks:")
            for i, task in enumerate(memory["tasks"], 1):
                print(f"  {i}. {task}")
        continue

    # ---------- ADD TASK ----------

    elif command.startswith("add task "):
        task = user_input[9:].strip()

        if task:
            memory["tasks"].append(task)
            save_memory()

            print(
                f"MANTRA: Task added, Sir: {task}"
            )
        continue

    # ---------- COMPLETE TASK ----------

    elif command.startswith("done "):
        try:
            index = int(user_input[5:].strip()) - 1

            if 0 <= index < len(memory["tasks"]):
                completed = memory["tasks"].pop(index)
                save_memory()

                print(
                    f"MANTRA: Task completed, Sir: {completed}"
                )
            else:
                print(
                    "MANTRA: That task doesn't exist, Sir."
                )

        except ValueError:
            print(
                "MANTRA: Please use 'done 1', "
                "'done 2', etc., Sir."
            )

        continue

    # ---------- SMART MEMORY LOOKUP ----------

    elif "what is my name" in command:
        if memory["name"]:
            print(
                f"MANTRA: Your name is {memory['name']}, Sir."
            )
        else:
            print(
                "MANTRA: I don't know your name yet, Sir."
            )
        continue

    elif "favorite color" in command:
        matches = [
            note for note in memory["notes"]
            if "favorite color" in note.lower()
        ]

        if matches:
            print(
                "MANTRA: Your favorite color is blue, Sir."
            )
        else:
            print(
                "MANTRA: I don't know your favorite color yet, Sir."
            )
        continue

    elif "what are my tasks" in command:
        if memory["tasks"]:
            print("MANTRA: Your tasks are:")
            for i, task in enumerate(memory["tasks"], 1):
                print(f"  {i}. {task}")
        else:
            print("MANTRA: You have no tasks, Sir.")
        continue

    # ---------- NORMAL AI CHAT ----------

    messages.append(
        {"role": "user", "content": user_input}
    )

    try:
        response = ollama.chat(
            model="tinyllama",
            messages=messages
        )

        reply = response["message"]["content"]

    except Exception as e:
        reply = "Sorry Sir, I couldn't process that request."
        print(f"MANTRA ERROR: {e}")

    messages.append(
        {"role": "assistant", "content": reply}
    )

    print("MANTRA:", reply)

