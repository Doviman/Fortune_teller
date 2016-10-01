import random

fortune = ['no', 'maybe', 'for sure', 'try again later', 'you ask too many questions',
           'look to the stars, you will find your answer there', 'yes', 'I think so',
           'I am sorry I just woke up from a nap, can you repeat the question',
           'what do you think?', 'the mind wants what it wants',
           'you already asked that question', 'the square root of 3', 'you already know the answer',
           'PRG 105', 'every ending is a new beginning', 'you should buy a new computer']
print 'Ask me a question, "I know all"'

selection = random.choice(fortune)
answer = selection

jumble = list(selection)

# scramble the letters in jumble


text = raw_input("\nWhat is your question? ")


print answer

