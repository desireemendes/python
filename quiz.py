class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

question_prompts = [
  "What is the capital of Peru? \n (a) Lima\n(b) Cusco\n(c) Arequipa\n\n",
  "Which country has the smallest land mass \n (a) Liechtenstein\n(b) Saint Kitts and Nevis\n(c) Monaco\n\n",
  "Which year was Canada born? \n (a) 1864\n(b) 1901\n(c) 1867\n\n"
]

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "c"),
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score +=1
    print("You got " + str(score) + "/" + str(len(questions) + " correct"))

  run_test(questions)