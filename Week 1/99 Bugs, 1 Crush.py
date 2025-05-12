def main():

    print("👋 Welcome to the Crush Quiz – Python Edition 💘\nLet’s find out if you’re here for code... or just for vibes 😏")
    
    score = 0

    name = input("What’s your name? ")
    q1 = input("🤓 Q1: Ideal Saturday plan?\na) Debugging in pajamas\nb) Long coffee & YouTube tutorials\nc) Sending memes to your situationship\nAnswer: ").lower()
    
    if q1 == "a":
        score += 3
    elif q1 == "b":
        score += 2
    elif q1 == "c":
        score += 1
    else:
        print("Invalid input for Q3.") 
    
    q2 = input("🐛 Q2: You see a bug in your code. What do you do?\na) Fix it immediately\nb) Google it + stackoverflow rabbit hole\nc) Cry and close your laptop dramatically\nAnswer: ").lower()
    
    if q2 == "a":
        score += 3
    elif q2 == "b":
        score += 2
    elif q2 == "c":
        score += 1
    else:
        print("Invalid input for Q3.") 

    q3 = input("💬 Q3: Your crush texts “wyd?” while you’re coding.\na) I reply with a GitHub link 😌\nb) “Nm hbu” and keep coding\nc) Drop everything and answer instantly 😩\nAnswer: ").lower()
    
    
    if q3 == "a":
        score += 3
    elif q3 == "b":
        score += 2
    elif q3 == "c":
        score += 1
    else:
        print("Invalid input for Q3.") 

    q4 = input("🧪 Q4: What's your favorite kind of code?\na) Clean, documented, and beautiful\nb) If it runs, I’m happy\nc) Copy-paste magic 🪄\nAnswer: ").lower()
    
    if q4 == "a":
        score += 3
    elif q4 == "b":
        score += 2
    elif q4 == "c":
        score += 1
    else:
        print("Invalid input for Q4.")
    
    q5 = input("🎯 Q5: What’s your toxic coding trait?\na) Never naming variables properly\nb) Forgetting to commit anything for 3 hours\nc) Starting new projects at 2AM\nAnswer: ").lower()
    
    if q5 == "a":
        score += 3
    elif q5 == "b":
        score += 2
    elif q5 == "c":
        score += 1
    else:
        print("Invalid input for Q5.")   
    
    q6 = input("🎭 Q6: If your code breaks, who do you blame?\na) Myself, obviously. I am responsible. 😇\nb) Python, IDE, compiler, moon cycle\nc) Whoever looked at me while I was typing 🙄\nAnswer: ").lower()

    if q6 == "a":
        score += 3
    elif q6 == "b":
        score += 2
    elif q6 == "c":
        score += 1
    else:
        print("Invalid input for Q6.")

    print("")
    print(f"{name}, your total score is: {score} points!✨")
    print("")
    
    if score <= 5:
        print("This Ain’t Code. It’s Chaos. But Make It Cute™ 🫠\nYour favorite language? Copy & Paste.\nYou open VS Code just to feel productive.\nYou’ve never used git, but your vibe is ✨iconic✨.\nConclusion: You’re not here to code. You’re here to slay.:")
    elif score < 9:
        print("You Like Tech, But Mostly for the Aesthetic ✨:\nYou’re here because Python looks cute on your Notion page.:\nYou once said “I love coding” but meant “I love color-coded sticky notes.”:\nDebugging? Only if Mercury isn’t in retrograde.:\nCatchphrase: “I vibe with tech, not errors.”")
    elif score < 15:
        print("Main Character Coder with Softcore Energy 🎬💅::\nYou love coding... but also love ✨vibes✨.:\nYou’ll fix that bug — eventually. After coffee. And a 30-min scroll break.:\nYou have a custom font in VS Code and you care.:\nCoding style: 80% logic, 20% aesthetic.")
    else:
        print("Certified Code Addict 💻💍::\nYou’re not just in a relationship with code — you are the relationship.:\nYour tabs are always aligned. Your GitHub green squares are borderline obsessive.:\nYou might even name your pet “Syntax.”:\nKeep slaying, caffeinated queen 👑☕:\nIDE Crush: VS Code, obviously (in dark mode).")

if __name__ == "__main__":
    main()