import re

for line in open("./configs/github_activity_report_ignorelist.txt"):
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", line.strip()):
        print(f'Invalid email: {line}')
        exit(1)
