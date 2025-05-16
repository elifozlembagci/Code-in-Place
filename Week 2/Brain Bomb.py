def main():
    print("💣 WELCOME TO BRAIN BOMB 💣\n")
    print("Let's check if your brain is fried today.")
    mood = input("👉 How do you feel today? (Choose one of them: happy / meh / exploding): ").strip().lower()
    tasks = int(input("How many tasks did you write today? "))
    had_class = input("🎓 Did you have any university classes today? (yes / no): ").strip().lower()
    meetings = int(input("How many online meetings did you have? "))
    sleep = int(input("How many hours did you sleep? "))

    if mood == "happy":
        mood_score = 0
    elif mood == "meh":
        mood_score = 1
    else:
        mood_score = 3

    tasks_score = tasks * 1
    
    if had_class == "yes":
        had_class_score = 4
    else:
        had_class_score = 0

    meetings_score = meetings * 2
    
    if sleep < 4:
        sleep_score = 5
    elif sleep <6:
        sleep_score =3
    else:
        sleep_score = 0

    total_score = int(mood_score + tasks_score + had_class_score + meetings_score + sleep_score)
    
    
    print(f"🧠 Your Mental Load Score: {total_score}")

    if total_score <= 6:
        print("✅ Brain Status: Stable – You survived today without frying your neurons.")
    elif total_score <= 12:
        print("⚠️ Brain Status: Warming Up – You might wanna take a break before things explode.")
    else:
        print("💣 Brain Status: EXPLODED – Your brain is toast. Shut it down and go scream into the void.")

    from ai  import call_gpt
    prompt = (f"You are a gentle, warm, and slightly funny assistant. Based on the user's daily mental load score, give them a short comforting message. Score ranges: 0–6 (stable), 7–12 (moderate stress), 13+ (exploded). Keep it under 3 sentences. Make them feel seen, supported, and a bit amused. Score: {total_score} – Mood: {mood}")
    message = call_gpt(prompt)
    print(message)

if __name__ == "__main__":
    main()