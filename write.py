from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("text.txt", "w") as file:
    file.write(f"text1 {now}")