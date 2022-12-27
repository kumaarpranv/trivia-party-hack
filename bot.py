import keyboard, time
import pyautogui as pag
from tesseract import take_screenshot
from chatgpt import ask

# while True:
#     keyboard.write("hello")
#     keyboard.press_and_release('enter')
#     time.sleep(1)
first = (1507, 1306)
second = (2194, 1306)
third = (1658, 1563)
fourth = (2112, 1559)

map_dic = {"1": first, "2": second, "3": third, "4": fourth, "5": None}

while True:
    if keyboard.is_pressed('q'):
        dic = take_screenshot()
        question = dic.get("question","")
        option1 = dic.get("option1", "")
        option2 = dic.get("option2", "")
        option3 = dic.get("option3", "")
        option4 = dic.get("option4", "")
        q = f"Be Absolutely correct, reply with 5) if you are unsure. Answer the following: {question}? 1) {option1}, 2) {option2}, 3) {option3}, 4) {option4}. Please reply with only, 1 (or) 2 (or) 3 (or) 4"
        ans = ask(q)
        ans = ans.replace(" ", "")
        el = map_dic.get(ans, None)
        if el:
            pag.moveTo(el[0], el[1])
            pag.click()
        continue
