from datetime import datetime

notes = [
    "Practiced JavaScript concepts",
    "Worked on React components",
    "Reviewed DSA problems",
    "Improved Next.js understanding",
    "Refactored learning notes"
]

with open("daily_log.txt", "a") as f:
    f.write(f"\n- {datetime.now().strftime('%Y-%m-%d')}: {notes[datetime.now().day % len(notes)]}")
