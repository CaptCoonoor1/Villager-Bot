import subprocess

while True:
    p = subprocess.Popen("python3 bot.py", stderr=subprocess.PIPE, shell=True)
    stop = False
    while not stop:
        for line in p.stderr:
            print(line.decode("utf-8").rstrip("\n"))
            if "heartbeat blocked" in line.decode("utf-8").lower():
                stop = True
                break
    print("== BOT EXITED ==")
    p.kill()