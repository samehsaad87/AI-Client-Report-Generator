from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
Path("reports").mkdir(exist_ok=True)

print("AI Client Report Generator")
print("-" * 40)

client_name = input("Client name: ").strip()
notes = input("Paste client/project notes: ").strip()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"""Create a professional client report from these notes.

Client: {client_name}
Notes:
{notes}

Format:
# Client Report
## Executive Summary
## Key Updates
## Issues / Risks
## Decisions
## Action Items
## Next Steps
Use concise professional language."""
)

report = response.output_text
print("\n" + report)
Path("reports/client_report.txt").write_text(report, encoding="utf-8")
print("\nSaved to reports/client_report.txt")
