print("======================================")
print("        🤖 AI KNOWLEDGE QUIZ 🤖       ")
print("======================================")

name = input("Enter your name: ")

score = 0

questions = [
("1. What does AI stand for?",
["a) Artificial Intelligence","b) Automatic Internet","c) Applied Information","d) Advanced Interface"],"a"),

("2. Who is known as the father of AI?",
["a) Alan Turing","b) John McCarthy","c) Elon Musk","d) Bill Gates"],"b"),

("3. Which programming language is widely used in AI?",
["a) Python","b) HTML","c) CSS","d) PHP"],"a"),

("4. Machine Learning is a part of?",
["a) Artificial Intelligence","b) Networking","c) Hardware","d) Database"],"a"),

("5. What does NLP stand for?",
["a) Natural Language Processing","b) Network Link Process","c) New Logic Program","d) Neural Link Process"],"a"),

("6. Which company created ChatGPT?",
["a) Google","b) Apple","c) OpenAI","d) IBM"],"c"),

("7. Face recognition belongs to?",
["a) Computer Vision","b) Networking","c) Storage","d) Programming"],"a"),

("8. AI voice assistants use?",
["a) NLP","b) CPU","c) GPU","d) RAM"],"a"),

("9. Deep Learning is based on?",
["a) Neural Networks","b) Routers","c) Switches","d) Printers"],"a"),

("10. Self-driving cars use?",
["a) Artificial Intelligence","b) Keyboard","c) Monitor","d) Mouse"],"a")
]

for q in questions:

    print("\n" + q[0])
    for option in q[1]:
        print(option)

    answer = input("Enter your answer (a/b/c/d): ")

    if answer.lower() == q[2]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print("\n======================================")
print("           🎯 QUIZ RESULT             ")
print("======================================")

print("Your Score:", score, "/10")

# Rank System
if score == 10:
    rank = "👑 AI Master"
elif score >= 8:
    rank = "🏆 AI Champion"
elif score >= 6:
    rank = "🥇 AI Expert"
elif score >= 4:
    rank = "🥈 AI Learner"
else:
    rank = "🥉 AI Beginner"

print("Your Rank:", rank)

# Certificate
print("\n======================================")
print("         🎓 QUIZ CERTIFICATE 🎓       ")
print("======================================")
print("This certificate is proudly presented to\n")
print("              ", name)
print("\nFor successfully completing the")
print("           AI Knowledge Quiz\n")
print("Score :", score, "/10")
print("Rank  :", rank)
print("\n🏆 Congratulations on your achievement!")
print("======================================")

# Thank You Card
print("\n======================================")
print("           💖 THANK YOU 💖            ")
print("======================================")
print("Thank you for participating in the")
print("          AI Knowledge Quiz")
print("Keep learning and exploring AI! 🤖")
print("======================================")