hasattr

print("1. Why is Jar Jar binks the real villain of the clone wars?")

# Right answer to question 1: C
correctAnswer1 = "C"

# A) He was a master of the dark side 
print("A) He was a master of the dark side")
# B) He was just stupid
print("B) He was just stupid")
# C) He controld and manuipulated the events of the clone wars while staying in the shadows.
print("C) He controld and manuipulated the events of the clone wars while staying in the shadows.")
# D) He really wasn't the villain of the clone wars
print("D) He really wasn't the Villain of the clone wars")
# E) Jar Jar binks wanted to be the hero but instead made it worse
print("E) Jar Jar binks wanted to be the hero but instead made it worse")
# F) He was driven by his own selfish desires and wanted to rule the galaxy
print("F) He was driven by his own selfish desires and wanted to rule the galaxy")
# G ) None of the above
print("G) None of the above")


userAnswer1 = input("What is the correct answer?...")
name = input("What is your name? ")

questions = {
        "question": "Why is Jar Jar binks the real villain of the clone wars?",
        "options": [

"A) He was a master of the dark side",
"B) He was just stupid",
"C) He controld and manuipulated the events of the clone wars while staying in the shadows",
"D) He really wasn't the Villain of the clone wars",
"E) Jar Jar binks wanted to be the hero but instead made it worse",
"F) He was driven by his own selfish desires and wanted to rule the galaxy",
"G) None of the above",
        ],
        "answer": "C"
    }
score = 0
user_answer = input("Your answer: ").upper()

if user_answer == questions["answer"]:
        print("Correct!")
        score = 1
else:
        print("Wrong!")

print("\nQuiz finished!")
print("Congratulations,", name)
print("You got", score, "out of", 1, "correct!")