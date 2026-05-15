import os
import datetime
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def gather_context(caveman_mode=False):
    """
    Automates the gathering of APCP files for the AI prompt.
    Run: python scripts/apcp-gather.py [--caveman]
    """
    # Files to gather
    core_files = [
        "AI_PROJECT_CONTEXT_PROTOCOL.md",
        "TASK_PROGRESS.yaml",
        "DECISION_LOG_PROTOCOL.md",
        "CONTEXT_OPTIMIZATION.md",
        "CAVEMAN_RULES.md"
    ]
    
    output_file = "PROMPT_READY.txt"
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    print(f"🔍 Gathering project context at {timestamp}...")
    if caveman_mode:
        print("🪨 CAVEMAN MODE ENABLED")
    
    try:
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(f"--- APCP CONTEXT PACKAGE ---\n")
            out.write(f"Generated: {timestamp}\n")
            out.write(f"Project Root: {os.getcwd()}\n")
            if caveman_mode:
                out.write("Mode: CAVEMAN (Token Optimized)\n")
            out.write(f"---------------------------\n\n")
            
            for f in core_files:
                if os.path.exists(f):
                    print(f"✅ Adding: {f}")
                    out.write(f"=== START OF FILE: {f} ===\n")
                    with open(f, "r", encoding="utf-8") as content:
                        out.write(content.read())
                    out.write(f"\n=== END OF FILE: {f} ===\n\n")
                else:
                    print(f"⚠️  Skipped (Not Found): {f}")
            
            out.write("\n--- INSTRUCTIONS ---\n")
            if caveman_mode:
                out.write("TALK LIKE CAVEMAN. Follow rules in CAVEMAN_RULES.md.\n")
                out.write("Why use many token when few token do trick?\n")
            else:
                out.write("Please read the context above and confirm you understand the current task and architecture.\n")
            
        print(f"\n🚀 Success! Context gathered in: {output_file}")
        print("👉 Copy the contents of this file and paste it into your AI session.")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    is_caveman = "--caveman" in sys.argv
    gather_context(caveman_mode=is_caveman)
