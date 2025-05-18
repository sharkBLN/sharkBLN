from datetime import datetime

readme_path = "README.md"

with open(readme_path, "a") as f:
    f.write(f"\n\n🦈 Updated at {datetime.utcnow().isoformat()} UTC")

print("README.md wurde aktualisiert.")

