import datetime
import sys
from pathlib import Path

try:
    from apcp_core_files import CORE_FILES
except ImportError as exc:
    raise SystemExit(
        "ERROR: scripts/apcp_core_files.py is required next to apcp-gather.py."
    ) from exc


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parents[1]


def gather_context(caveman_mode=False):
    """
    Gather canonical APCP files into PROMPT_READY.txt.
    Run: python scripts/apcp-gather.py [--caveman]
    """
    output_file = ROOT / "PROMPT_READY.txt"
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )

    print(f"Gathering project context at {timestamp}...")
    if caveman_mode:
        print("CAVEMAN MODE ENABLED")

    try:
        with output_file.open("w", encoding="utf-8") as out:
            out.write("--- APCP CONTEXT PACKAGE ---\n")
            out.write(f"Generated: {timestamp}\n")
            out.write(f"Project Root: {ROOT}\n")
            if caveman_mode:
                out.write("Mode: CAVEMAN (Token Optimized)\n")
            out.write("---------------------------\n\n")

            for relative in CORE_FILES:
                path = ROOT / relative
                if path.exists():
                    print(f"Adding: {relative}")
                    out.write(f"=== START OF FILE: {relative} ===\n")
                    out.write(path.read_text(encoding="utf-8"))
                    out.write(f"\n=== END OF FILE: {relative} ===\n\n")
                else:
                    print(f"Skipped (Not Found): {relative}")

            out.write("\n--- INSTRUCTIONS ---\n")
            if caveman_mode:
                out.write("TALK LIKE CAVEMAN. Follow rules in CAVEMAN_RULES.md.\n")
                out.write("Why use many token when few token do trick?\n")
            else:
                out.write(
                    "Please read the context above and confirm you understand "
                    "the current task and architecture.\n"
                )

        print(f"\nSuccess! Context gathered in: {output_file}")
        print("Review the generated bundle before sharing it outside the local workspace.")
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    is_caveman = "--caveman" in sys.argv
    raise SystemExit(gather_context(caveman_mode=is_caveman))
