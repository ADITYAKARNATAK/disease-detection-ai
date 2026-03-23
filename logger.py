import datetime


LOG_FILE = "log.txt"


def log(text):

    now = datetime.datetime.now()

    line = f"{now} : {text}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)