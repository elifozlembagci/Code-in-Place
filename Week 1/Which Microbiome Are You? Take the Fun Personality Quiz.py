def intro():
    print("🦠 WHICH MICROBIOME ARE YOU? 🦠")
    print("Let’s find out which gut bacteria matches your lifestyle!")
    print("1 = YES    2 = NO\n")

def get_answers():
    q1 = get_input("Do you consume yogurt or kefir regularly?")
    q2 = get_input("Do you enjoy eating fiber-rich vegetables?")
    q3 = get_input("Do you crave sweets or carbs often?")
    q4 = get_input("Are you generally a very stressed person?")
    return q1, q2, q3, q4

def diagnose(q1, q2, q3, q4):
    print("\n🔬 Analyzing your inner bacteria...\n")
    if q1 == "1" and q2 == "1":
        print("✨ You're a *Lactobacillus*! Calm, probiotic-friendly and digestive system's BFF.")
    elif q3 == "1" and q4 == "1":
        print("🔥 You're a *Firmicutes*! Energy-loving and possibly sugar-powered.")
    elif q2 == "1" and q3 == "2":
        print("💪 Definitely *Akkermansia*! Lean, clean, and fiber-fueled.")
    elif q1 == "2" and q2 == "2":
        print("🧨 Giving off *Clostridium* vibes... might be time to rethink your gut habits 😅")
    else:
        print("🤔 Hmm... sounds like a *Bacteroides*! Versatile, efficient, always adapting.")

def get_input(question):
    while True:
        answer = input(question + " (1 = Yes / 2 = No): ").strip()
        if answer in ["1", "2"]:
            return answer
        else:
            print("⚠️ Please enter 1 for YES or 2 for NO.\n")


def main():
    intro()
    q1, q2, q3, q4 = get_answers()
    diagnose(q1, q2, q3, q4)



if __name__ == "__main__":
    main()