def main():

    print( "✨ Welcome to Terminal Tarot ✨\nThink of a question, and let the code do its magic... ")
    name = input("What’s your name, seeker of vibes? 👀 → ")
    print(f"\nNice to meet you, {name} 💫 Let's check in with your current energy.\n")

    feel = input("How are you feeling today? \n😌  😵  🔥  🪫  🤡  🐢  💘  🧠  🫠  ⏳\nChoose an emoji that matches your vibe: ")
    mode = input("\nChoose your reading theme:\n1️⃣ Love & Code 💖\n2️⃣ Career Vibes 💼\n3️⃣ Pure Chaos 🌀\nEnter 1, 2, or 3: ")
    question = input("\n💭 What's your question or intention? ")


    if mode == "1":
        theme = "This reading focuses on emotional connections and code."
    elif mode == "2":
        theme = "This reading relates to ambition, learning, and developer career energy."
    elif mode == "3":
        theme = "Let the chaos guide us. No filter, full energy."

    
    print("\n🔀 Drawing your card\n")

    cards = [
        "The Fool of the Frameworks",
        "The Magician of the Command Line",
        "The High Priestess of Git",
        "The Empress of Frontend",
        "The Emperor of Regex",
        "The Hierophant of Stack Overflow",
        "The Lovers (You & Your Favorite IDE)",
        "The Chariot of Deadlines",
        "Strength (a.k.a. Pushing to Main)",
        "The Hermit Debugger",
        "The Wheel of Scope Creep",
        "Justice (Indentation Matters)",
        "The Hanged Commit",
        "Death (of Your Old Codebase)",
        "Temperance (a.k.a. Clean Architecture)",
        "The Devil (a.k.a. Quick Fixes)",
        "The Tower of Merge Conflicts",
        "The Star of Documentation",
        "The Moon of Imposter Syndrome",
        "The Sun of Your First Green Commit",
        "Judgement Day (a.k.a. Code Review)",
        "The World (a.k.a. It Finally Runs!)"
]
    import random
    past_card = random.choice(cards)
    present_card = random.choice(cards)
    future_card = random.choice(cards)

    print(f"🔮 Your Past Card is: {past_card}\n")
    print(f"🔮 Your Present Card is: {present_card}\n")
    print(f"🔮 Your Future Card is: {future_card}\n")


    print("🧠 Message from the universe:")

    print("\n🌙 Breathing in... pulling energy from the stars... aligning with your inner dev self 🌌\n")

    from ai  import call_gpt
    prompt = (f"You are an AI tarot reader.\nThe user's name is {name}, and The user asked: '{question}'\nThe user's current mood is {feel}.\nThe reading theme is: {theme}\nThe three cards drawn are:\n- Past: {past_card}\n- Present: {present_card}\n- Future: {future_card}\n\nGive a short interpretation for each card in relation to the user's question.\nGive a fun, creative, and slightly deep interpretation that connects the card’s energy to the user’s question.\nWrite your answer in 3 to 5 sentences. \nEnd with a one-sentence 'Vibe Check' message that’s playful but insightful.")
    message = call_gpt(prompt)
    print(message)

    
    follow_up = input("\n Was anything unclear or off in your reading? (yes/no): ").lower()
    if follow_up == ("yes"):
        issue = input("💬 Tell me what felt confusing or wrong: ")
        prompt_q1 = (f"You gave a tarot-style reading earlier based on this user's question: '{question}' and cards: {past_card}, {present_card}, {future_card}.\nThe user said they had an issue with the reading: '{issue}'.\nPlease respond kindly, clarify the original message if needed, and offer a brief follow-up insight in a supportive tone.")
        response2 = call_gpt(prompt_q1)
        print(response2)
        print(f"\n🌈 Glad it resonated, {name}! See you next sync ✨")
    else:
        print(f"🌈 Glad it resonated, {name}! See you next sync ✨")




if __name__ == "__main__":
    main()