# Mood Refresher

A simple command-line **Mood Refresher** application written in Python.  
The project demonstrates a **Stack data structure (LIFO — Last In, First Out)** to store, view, and remove moods while providing mood-based recommendations.

## Features

- Add/log multiple moods using a stack.
- View advice for the latest/current mood.
- View all recorded moods, with the latest mood displayed first.
- Remove the latest mood using the stack's `pop` operation.
- Prevent proceeding without entering at least one mood.
- Provides different recommendations based on the entered mood.
- Runs completely from the command line with no external libraries.

## Project Structure

The repository should contain the following file at the root level:

```text
.
├── mood_refresher.py
└── README.md
```

> If your Python file has a different name, replace `mood_refresher.py` with your actual filename in the commands below.

## Requirements

- Python 3.x
- No third-party Python packages are required.
- A terminal/command-line environment.

## Setup

### 1. Install Python

Make sure Python 3 is installed.

Check the installation:

```bash
python --version
```

If your system uses `python3` instead, run:

```bash
python3 --version
```

The project does not require a virtual environment or any external dependency installation.

### 2. Clone the repository

Clone the GitHub repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd <YOUR_REPOSITORY_NAME>
```

### 3. Run the project

Run the Python program from the terminal:

```bash
python mood_refresher.py
```

Or, on systems where Python 3 is invoked using `python3`:

```bash
python3 mood_refresher.py
```

## How to Use

### Step 1: Enter moods

When the program starts, it asks you to enter your moods one by one.

Example:

```text
WELCOME TO MOOD REFRESHER
Lets log your moods first!

Enter your mood (or type 'done' to finish setting): happy
-> Logged: 'happy'

Enter your mood (or type 'done' to finish setting): stressed
-> Logged: 'stressed'

Enter your mood (or type 'done' to finish setting): done
```

Type `done` when you have finished entering moods.

At least one mood must be entered before proceeding to the dashboard.

### Step 2: Use the Advice Dashboard

After the initial mood entry, the application displays four options:

```text
1. View advice for current/latest mood
2. View advice for ALL Recorded Moods
3. Remove unwanted/mistakenly added mood
4. Exit
```

#### Option 1 — View advice for current/latest mood

Displays the most recently added mood and generates advice for it.

This uses the stack's **Peek** operation, so the mood is viewed without removing it.

#### Option 2 — View advice for all recorded moods

Displays all stored moods from the latest mood to the oldest mood.

This uses the stack to traverse the moods in reverse insertion order.

#### Option 3 — Remove latest mood

Removes the most recently added mood.

This uses the stack's **Pop** operation and follows the LIFO principle.

Example:

```text
Removed latest mood:'stressed'
```

#### Option 4 — Exit

Terminates the application.

## Stack Implementation

The project implements a stack using a Python list.

### `isEmpty(stk)`

Checks whether the stack contains any elements.

```python
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
```

### `Push(stk, item)`

Adds a new mood to the top of the stack.

```python
def Push(stk, item):
    stk.append(item)
```

### `pop(stk)`

Removes and returns the latest mood.

If the stack is empty, it returns `"Underflow"`.

```python
def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        return stk.pop()
```

### `Peek(stk)`

Returns the latest mood without removing it from the stack.

```python
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]
```

### `Display(stk)`

Displays the recorded moods from the top of the stack to the bottom.

## Mood-Based Recommendations

The `get_mood_response()` function provides recommendations based on the entered mood.

Moods such as:

- happy
- excited
- joyful
- great
- calm

receive a positive/celebratory recommendation.

Moods such as:

- sad
- tired
- bored
- uninspired
- stressed
- angry
- fearless

receive a motivational recommendation.

Other moods receive a general balanced recommendation.

Mood matching is case-insensitive. For example, `Happy`, `happy`, and `HAPPY` are treated the same way.

## Example Session

```text
=============================================
           WELCOME TO MOOD REFRESHER
=============================================
Lets log your moods first!

Enter your mood (or type 'done' to finish setting): happy
-> Logged: 'happy'

Enter your mood (or type 'done' to finish setting): tired
-> Logged: 'tired'

Enter your mood (or type 'done' to finish setting): done

All the moods stored successfully! Move to advice dashboard.....

===============================================
------------MOOD ADVICE DASHBOARD--------------
===============================================
1. View advice for current/latest mood
2. View advice for ALL Recorded Moods
3. Remove unwanted/mistakenly added mood
4. Exit

Enter the choice (1-4): 1

---CURRENT MOOD:TIRED---
Advice KEEP GOING! Take a deep breath, play your favorite song and drink some water!
```

## Stack / LIFO Concept

The application follows the **LIFO (Last In, First Out)** principle.

For example, if the user enters:

```text
happy
excited
stressed
```

The stack conceptually becomes:

```text
TOP -> stressed
       excited
       happy
```

Therefore:

- `Peek()` returns `stressed`.
- `pop()` removes `stressed`.
- The next `Peek()` returns `excited`.

This demonstrates how stacks can be used to manage the most recently added item first.

## Error Handling

The application handles an empty stack using an `"Underflow"` response.

If the user attempts to remove a mood when no moods remain, the program displays:

```text
Stack is empty! No more moods left.
```

If the user tries to finish the initial mood entry without entering any mood, the program asks them to enter at least one mood.

## Dependencies

No external packages are required.

The application uses only Python's built-in functionality, primarily:

- Lists
- Functions
- Loops
- Conditional statements
- User input/output

## Running in a Terminal

The project is designed to be executed entirely from a terminal and does not require a GUI.

From the repository root:

```bash
python mood_refresher.py
```

The evaluator can interact with the application using the terminal by entering moods and dashboard choices as requested by the prompts.

## Author

**Mood Refresher — Stack Implementation Project**
