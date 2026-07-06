from datetime import datetime

def log(text):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{waktu}] {text}")

    with open("logs/zf.log", "a") as f:
        f.write(f"[{waktu}] {text}\n")
