from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    name='ElonMusk',
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
)

talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m elon musk.']

math_talk1 = ['pythagorean theorem',
              'a squared plus b squared equals c squared.']
math_talk2 = ['law of cosines',
              'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)
for item in (talk, math_talk1, math_talk2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("hi"))
print(my_bot.get_response("i'm great!"))
print(my_bot.get_response("what's your name?"))
print(my_bot.get_response("what is pythagorean theorem"))
print(my_bot.get_response("do you know the law of cosines?"))

while True:
 try:
    bot_input = input("you: ")
    bot_response = my_bot.get_response(bot_input)
    print(f"{my_bot.name}: {bot_response}")
 except(KeyboardInterrupt, EOFError, SystemExit):
     break;
