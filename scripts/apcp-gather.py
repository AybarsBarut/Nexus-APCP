import datetime
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]

CORE_FILES = [
    "AI_PROJECT_CONTEXT_PROTOCOL.md",
    "AI_MAIN.md",
    "TASK_PROGRESS.yaml",
    "DECISION_LOG_PROTOCOL.md",
    "CONTEXT_OPTIMIZATION.md",
    "CAVEMAN_RULES.md",
    "EMOJI_POLICY.md",
    "VISUAL_CONTEXT_MERMAID.md",
    "AI_AGENT_SKILLS_PROTOCOL.md",
    "AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md",
    "FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
    "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "DEBLOAT_APPLICATION_GUIDE.md",
]


def gather_context(caveman_mode=False):
    """
    Automates the gathering of APCP files for the AI prompt.
    Run: python scripts/apcp-gather.py [--caveman]
    """
    output_file = ROOT / "PROMPT_READY.txt"
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    print(f"Gathering project context at {timestamp}...")
    if caveman_mode:
        print("CAVEMAN MODE ENABLED")
    
    try:
        with output_file.open("w", encoding="utf-8") as out:
            out.write(f"--- APCP CONTEXT PACKAGE ---\n")
            out.write(f"Generated: {timestamp}\n")
            out.write(f"Project Root: {ROOT}\n")
            if caveman_mode:
                out.write("Mode: CAVEMAN (Token Optimized)\n")
            out.write(f"---------------------------\n\n")
            
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
                out.write("Please read the context above and confirm you understand the current task and architecture.\n")
            
        print(f"\nSuccess! Context gathered in: {output_file}")
        print("Review the generated bundle before sharing it outside the local workspace.")
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    is_caveman = "--caveman" in sys.argv
    raise SystemExit(gather_context(caveman_mode=is_caveman))
