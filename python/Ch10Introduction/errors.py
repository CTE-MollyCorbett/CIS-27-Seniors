# =====================================================errors.py========================================================
# -- Warm-up: a program that works --
# print("Hello, World!")
# -- Experiment 1: SYNTAX ERROR --
# print("Hello, World!)
# -- Experiment 2: SYNTAX ERROR --
# print(Hello, World!)
# -- Experiment 3: NAME ERROR --
# Print("Hello, World!")
# -- Experiment 4: INDENTATION ERROR --
# print("Hello")
#     print("World")
# -- Experiment 5: EXCEPTION-ZERO DIVISION ERROR --
# print("About to divide")
# print(1/0)
# -- Experiment 6: LOGIC error with numbers --
# We want the AVERAGE of three test scores.
score1 = 90
score2 = 80
score3 = 70
average = score1 + score2 + score3 / 3
print("Average:", average) # PEMDAS divided score3 by 3 first, then added the rest
# average = (score1 + score2 + score3) / 3