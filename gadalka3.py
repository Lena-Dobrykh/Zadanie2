from brain import Brain

brain = Brain()
prompt = "Вопрос:"

question = ""
while question != "хватит":
    print(prompt, end =' ')
    answer = brain.think(input())
    print(answer)
