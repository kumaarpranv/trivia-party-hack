from chatgpt_wrapper import ChatGPT
import re

bot = ChatGPT()

def ask(question):
    response = bot.ask(question)
    print(response)
    objs = re.findall(r"[0-9]+\)", response)
    if len(objs) > 0:
        return(objs[0].replace(')',''))
    else:
        return "5"