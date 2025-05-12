def main():
    print("🐍 Welcome to the Python Time Machine! Tell me your name, birth year, and I’ll tell you whether you’re Gen Z or just old 😉")
    
    this_year = int(2025)
    name = input("What's your name? ")
    year = int(input("What year were you born? "))
    calculate = this_year - year
    
    print("🎉 Drum roll please...")

    print(f"Hi {name}! According to my calculations, in 2025 you are... {calculate} years old! 😱")

    if calculate < 18:
        print("You're a baby genius 👶🧠 Probably learned Python before puberty.")
    elif calculate < 25:
        print("Zoomer energy detected ⚡ Now go touch some grass (or code).")
    elif calculate < 30:
        print("Peak millennial chaos. Espresso? Existential crisis? Both? ☕😵")
    elif calculate < 50:
        print("Mature. Calm. But still a little unhinged. Probably drinks black coffee ☕")
    else:
        print("Legend. You’ve seen it all. And now you're coding? RESPECT 🙏👑")

    zodiac = input("What’s your zodiac sign? ").lower()


    shades = {
        "aries": "Always starting things, rarely finishing. Iconic tho.",
        "taurus": "You'd rather nap than talk to people. Same.",
        "gemini": "Do you ever stop talking? No? Cool.",
        "cancer": "Cry now or cry later? Your choice.",
        "leo": "Main character syndrome? Say less.",
        "virgo": "Your Google Calendar has feelings.",
        "libra": "You still can’t decide what to eat, right?",
        "scorpio": "The mystery isn’t mysterious anymore 👀",
        "sagittarius": "Gone before commitment enters the room.",
        "capricorn": "Working? On a Saturday? Again?",
        "aquarius": "You believe you're different. And... you are.",
        "pisces": "Emotionally in 2075. Physically in bed.",
    }

    if zodiac in shades:
        print(shades[zodiac])
    else:
        print("Sorry, we don't roast non-zodiacs 😅")


if __name__ == "__main__":
    main()