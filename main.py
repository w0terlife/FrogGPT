import time

print("𓆏 Ribbit-ribbit, welcome to FrogGPT! 𓆏")
name = input("Froggie needs your name before granting access: ").strip().title()
print(f"\nWussup {name}! 🐸 You’ve just hopped into the pond of wonders.\n")

day = input("Tell Froggie... are you having a good day? (yes/no): ").strip().lower()

match day:
    case 'yes':
        print("YAYYY! Froggie does a happy jump 💚")
    case 'no':
        print("Awwww... Froggie gives you a lily pad hug 🫂")
    case _:
        print("Froggie tilts his head 🤨 — he does not understand you, hooman!")

time.sleep(1)

joke_interest = input("\nWant to hear a legendary frog joke? (yes/no): ").strip().lower()

if joke_interest == 'yes':
    print("\n🟢 Prepare thyself… this joke has been passed down by froggy ancestors.\n")
    time.sleep(1)
    answer = input("🗣 What did the frog order at FrogDonald’s? ").strip().lower()

    correct_answer = "french flies and a diet croak"
    if correct_answer in answer:
        print("WHHAAAAT 😱 You already knew?! Froggie feels betrayed… but impressed.")
    else:
        print(f"Froggie says: '{correct_answer}' 🤣🤣 You may now croak with laughter.")
else:
    print("No joke? Froggie disappointed 🐸💔 But he still likes u. Just less.")

