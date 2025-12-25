from time import sleep
from src.Calculate.Calculate import eval
from src.Discord.Discord import send_message, get_message

user_name = "baihufox"
last_id = None

while True:
    msg = get_message()

    if msg["id"] == last_id:
        sleep(0.5)
        continue

    last_id = msg["id"]

    n = eval(msg["content"].split(" ")[0])

    if n is not None and msg["author"]["username"] != user_name:
        send_message(n + 1)
        print(f"發送數字: {n + 1}")

    sleep(0.1)