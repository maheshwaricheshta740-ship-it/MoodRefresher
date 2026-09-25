# --- STACK IMPLEMENTATION FOR MOOD REFRESHER ---

def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False


def Push(stk, item):
    stk.append(item)


def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        return stk.pop()


def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]


# --- Helper function to give smart recommendations based on mood ---

def get_mood_response(mood_type):
    mood_type = mood_type.lower()

    if mood_type in ['happy', 'excited', 'joyful', 'great', 'calm']:
        return "CELEBERATION TIME! YOU'RE IN HIGH SPIRITS! Take a quick break to dance,enjoy with friends or reward yourself with a self treat."

    elif mood_type in ['sad', 'tired', 'bored', 'uninspired', 'stressed', 'angry', 'fearless', 'angry']:
        return "KEEP GOING! Take a deep breath, play your favorite song and drink some water!"

    else:
        return "Stay balanced!,Take a moment to stretch and stay focused!"


def Display(stk):
    if isEmpty(stk):
        print("\nNo history of mood is recorded yet!")
    else:
        top = len(stk) - 1
        print("--- MOODS YOU ADDED ---")

        for i in range(top, -1, -1):
            mood_type = stk[i]
            # advice = get_mood_response(mood_type)
            print(f"-Mood:{mood_type.upper()}")
            # print(f"Advice:{advice}\n")


# ================================
# ------ INITIAL MOOD ENTRY -------
# ================================

Stack = []

print("=============================================")
print("           WELCOME TO MOOD REFRESHER         ")
print("=============================================")
print("Lets log your moods first!\n")

while True:
    mood = input("Enter your mood (or type 'done' to finish setting):")

    # Push(Stack, mood)

    if mood.lower() == "done":
        if isEmpty(Stack):
            print("Please enter atleast one mood for proceeding further!")
            continue
        break

    Push(Stack, mood)
    print(f"-> Logged: '{mood}'")

print("\nAll the moods stored successfully! Move to advice dashboard.....")


# =======================================================
# -------------- ADVICE DASHBOARD FUNCTION -------------
# =======================================================

while True:
    print("===============================================")
    print("------------MOOD ADVICE DASHBOARD--------------")
    print("===============================================")
    print("1. View advice for current/latest mood")  # Push function display
    print("2. View advice for ALL Recorded Moods")   # Display function display
    print("3. Remove unwanted/mistakenly added mood")
    print("4. Exit")

    ch = int(input("Enter the choice (1-4): "))

    if ch == 1:
        item = Peek(Stack)

        if item == "Underflow":
            print("NO mood recorded!")
        else:
            print(f"\n---CURRENT MOOD:{item.upper()}---")
            print("Advice", get_mood_response(item))

    elif ch == 2:
        Display(Stack)

    elif ch == 3:
        item = pop(Stack)

        if item == "Underflow":
            print("Stack is empty! No more moods left.")
        else:
            print(f"\nRemoved latest mood:'{item}'")

    elif ch == 4:
        print("Thank you for using MOOD REFRESHER! Have a great day!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")
