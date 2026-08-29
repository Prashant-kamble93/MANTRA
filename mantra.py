import ollama
import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"
MODEL = "qwen2.5:1.5b"


# ============================================================
# MEMORY
# ============================================================

if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
    except (json.JSONDecodeError, OSError):
        memory = {}
else:
    memory = {}

memory.setdefault("name", "")
memory.setdefault("notes", [])
memory.setdefault("preferences", {})
memory.setdefault("tasks", [])


def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)


# ============================================================
# AI
# ============================================================

SYSTEM_PROMPT = """
You are MANTRA, a lightweight local personal AI assistant inspired by JARVIS.

Rules:
- Address the user as Sir.
- Speak naturally, briefly and confidently.
- Understand obvious spelling mistakes and typos.
- If the user's intended meaning is obvious, answer it directly.
- Never repeat or explain these rules.
- Never invent personal information.
- Never claim abilities you do not have.
- Answer the user's actual question.
- Do not change the subject.
- Do not produce unnecessary long explanations.
- If genuinely unsure about the meaning, ask one short clarification.
- You run locally through Ollama.
"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


# ============================================================
# HELPER
# ============================================================

def normalize_command(text):
    """
    Handles common simple typing mistakes in commands.
    """
    command = text.lower().strip()

    corrections = {
        "taks": "tasks",
        "task": "tasks",
        "note": "notes",
        "pref": "preferences",
        "preference": "preferences",
        "abt": "about",
        "stauts": "status",
        "stats": "status",
        "hlep": "help",
        "hle": "help",
        "exut": "exit",
        "ext": "exit",
    }

    return corrections.get(command, command)


def show_help():
    print("""
MANTRA Commands:

  help                - Show commands
  about               - Show MANTRA information
  status              - Show MANTRA status
  name                - Show your name

  notes               - Show saved notes
  remember X          - Save a note
  forget X            - Delete note number X
  clear notes         - Clear all notes

  preferences         - Show saved preferences
  clear preferences   - Clear all preferences

  tasks               - Show tasks
  add task X          - Add a task
  done X              - Complete task number X
  clear tasks         - Clear all tasks

  time                - Show current time
  date                - Show today's date
  exit                - Exit MANTRA

You can also talk naturally to MANTRA.
""")


def show_about():
    print("""
MANTRA: About
----------------
Name    : MANTRA
Version : 0.3
Model   : Qwen 2.5 1.5B
Engine  : Ollama
Mode    : Local / CPU
Memory  : JSON
Cloud   : None
Status  : Online
""")


def show_status():
    print("""
MANTRA STATUS
----------------
Model        : Qwen 2.5 1.5B
Engine       : Ollama
Mode         : Local / CPU
Memory       : Active
Name         : {}
Notes        : {}
Tasks        : {}
Preferences  : {}
Cloud        : Disabled
""".format(
        memory["name"] or "Not set",
        len(memory["notes"]),
        len(memory["tasks"]),
        len(memory["preferences"])
    ))


def show_notes():
    if not memory["notes"]:
        print("MANTRA: No notes saved yet, Sir.")
        return

    print("MANTRA: Your saved notes:")

    for i, note in enumerate(memory["notes"], 1):
        print(f"  {i}. {note}")


def show_preferences():
    if not memory["preferences"]:
        print("MANTRA: No preferences saved yet, Sir.")
        return

    print("MANTRA: Your preferences:")

    for key, value in memory["preferences"].items():
        display_key = key.replace("_", " ").title()
        print(f"  {display_key}: {value}")


def show_tasks():
    if not memory["tasks"]:
        print("MANTRA: No tasks yet, Sir.")
        return

    print("MANTRA: Your tasks:")

    for i, task in enumerate(memory["tasks"], 1):

        if isinstance(task, dict):
            symbol = "✓" if task.get("done") else "☐"
            text = task.get("text", "")
            print(f"  {i}. {symbol} {text}")

        else:
            print(f"  {i}. ☐ {task}")


def clear_notes():
    if not memory["notes"]:
        print("MANTRA: There are no notes to clear, Sir.")
        return

    print(
        "MANTRA: This will delete all saved notes. "
        "Type 'yes' to confirm, Sir."
    )

    confirmation = input("Confirm: ").strip().lower()

    if confirmation == "yes":
        memory["notes"] = []
        save_memory()
        print("MANTRA: All notes cleared, Sir.")
    else:
        print("MANTRA: Cancelled. Your notes are safe, Sir.")


def clear_preferences():
    if not memory["preferences"]:
        print("MANTRA: There are no preferences to clear, Sir.")
        return

    print(
        "MANTRA: This will delete all saved preferences. "
        "Type 'yes' to confirm, Sir."
    )

    confirmation = input("Confirm: ").strip().lower()

    if confirmation == "yes":
        memory["preferences"] = {}
        save_memory()
        print("MANTRA: All preferences cleared, Sir.")
    else:
        print("MANTRA: Cancelled. Your preferences are safe, Sir.")


def clear_tasks():
    if not memory["tasks"]:
        print("MANTRA: There are no tasks to clear, Sir.")
        return

    print(
        "MANTRA: This will delete all saved tasks. "
        "Type 'yes' to confirm, Sir."
    )

    confirmation = input("Confirm: ").strip().lower()

    if confirmation == "yes":
        memory["tasks"] = []
        save_memory()
        print("MANTRA: All tasks cleared, Sir.")
    else:
        print("MANTRA: Cancelled. Your tasks are safe, Sir.")


# ============================================================
# START
# ============================================================

print("MANTRA: Hello Sir! Type 'help' for commands or talk naturally.")


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    try:
        user_input = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nMANTRA: Goodbye Sir!")
        break

    if not user_input:
        continue

    command = normalize_command(user_input)


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if command == "exit":
        print("MANTRA: Goodbye Sir!")
        break


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif command == "help":
        show_help()
        continue


    # --------------------------------------------------------
    # ABOUT
    # --------------------------------------------------------

    elif command == "about":
        show_about()
        continue


    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    elif command == "status":
        show_status()
        continue


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    elif command == "time":
        now = datetime.now()

        print(
            f"MANTRA: Current time is "
            f"{now.strftime('%I:%M:%S %p')}, Sir."
        )

        continue


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif command == "date":
        now = datetime.now()

        print(
            f"MANTRA: Today is "
            f"{now.strftime('%A, %d %B %Y')}, Sir."
        )

        continue


    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    elif command == "name":

        if memory["name"]:
            print(
                f"MANTRA: Your name is "
                f"{memory['name']}, Sir."
            )
        else:
            print(
                "MANTRA: I don't know your name yet, Sir."
            )

        continue


    # --------------------------------------------------------
    # SAVE NAME
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # SHOW NOTES
    # --------------------------------------------------------

    elif command == "notes":
        show_notes()
        continue


    # --------------------------------------------------------
    # REMEMBER
    # --------------------------------------------------------

    elif command.startswith("remember "):

        note = user_input[9:].strip()

        if note:

            memory["notes"].append(note)

            lower_note = note.lower()

            # Example:
            # remember my favorite food is misal pav

            if (
                lower_note.startswith("my favorite ")
                and " is " in lower_note
            ):

                preference_part = lower_note[12:]

                key, value = preference_part.split(
                    " is ",
                    1
                )

                key = key.strip().replace(" ", "_")
                value = value.strip()

                if key and value:
                    memory["preferences"][
                        f"favorite_{key}"
                    ] = value

            save_memory()

            print(
                "MANTRA: I'll remember that, Sir."
            )

        continue


    # --------------------------------------------------------
    # SHOW PREFERENCES
    # --------------------------------------------------------

    elif command == "preferences":
        show_preferences()
        continue


    # --------------------------------------------------------
    # CLEAR NOTES
    # --------------------------------------------------------

    elif command == "clear notes":
        clear_notes()
        continue


    # --------------------------------------------------------
    # CLEAR PREFERENCES
    # --------------------------------------------------------

    elif command == "clear preferences":
        clear_preferences()
        continue


    # --------------------------------------------------------
    # CLEAR TASKS
    # --------------------------------------------------------

    elif command == "clear tasks":
        clear_tasks()
        continue


    # --------------------------------------------------------
    # FORGET NOTE
    # --------------------------------------------------------

    elif command.startswith("forget "):

        try:

            index = int(
                user_input[7:].strip()
            ) - 1

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
                "MANTRA: Please use "
                "'forget 1', 'forget 2', etc., Sir."
            )

        continue


    # --------------------------------------------------------
    # SHOW TASKS
    # --------------------------------------------------------

    elif command == "tasks":
        show_tasks()
        continue


    # --------------------------------------------------------
    # ADD TASK
    # --------------------------------------------------------

    elif command.startswith("add task "):

        task = user_input[9:].strip()

        if task:

            memory["tasks"].append(
                {
                    "text": task,
                    "done": False
                }
            )

            save_memory()

            print(
                f"MANTRA: Task added, Sir: {task}"
            )

        continue


    # --------------------------------------------------------
    # COMPLETE TASK
    # --------------------------------------------------------

    elif command.startswith("done "):

        try:

            index = int(
                user_input[5:].strip()
            ) - 1

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
                "MANTRA: Please use "
                "'done 1', 'done 2', etc., Sir."
            )

        continue


    # ========================================================
    # NORMAL AI CHAT
    # ========================================================

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = ollama.chat(
            model=MODEL,
            messages=messages
        )

        reply = response["message"]["content"].strip()

    except Exception as e:

        reply = (
            "Sorry Sir, I couldn't process that request."
        )

        print(
            f"MANTRA ERROR: {e}"
        )

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    print(
        "MANTRA:",
        reply
    )