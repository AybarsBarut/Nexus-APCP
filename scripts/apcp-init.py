import argparse
import sys
from pathlib import Path

try:
    from apcp_core_files import available_profiles, profile_description
except ImportError as exc:
    raise SystemExit(
        "ERROR: scripts/apcp_core_files.py is required next to apcp-init.py."
    ) from exc

try:
    from apcp_install import install_profile
except ImportError:
    # Need to handle the dash in the filename 'apcp-install.py'
    import importlib.util
    install_script = Path(__file__).parent / "apcp-install.py"
    if not install_script.is_file():
        raise SystemExit("ERROR: scripts/apcp-install.py is missing.")
    
    spec = importlib.util.spec_from_file_location("apcp_install", install_script)
    apcp_install = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(apcp_install)
    install_profile = apcp_install.install_profile


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def prompt_choice(question, choices, default=None):
    print(f"\n{question}")
    for idx, choice in enumerate(choices, 1):
        print(f"  {idx}. {choice['label']}")
    
    while True:
        prompt_text = f"Select an option (1-{len(choices)})"
        if default is not None:
            prompt_text += f" [{default}]"
        prompt_text += ": "
        
        try:
            answer = input(prompt_text).strip()
            if not answer and default is not None:
                return choices[default - 1]["value"]
            
            idx = int(answer)
            if 1 <= idx <= len(choices):
                return choices[idx - 1]["value"]
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a number.")
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(1)


def prompt_yes_no(question, default="y"):
    prompt_text = f"{question} (y/n) [{default}]: "
    while True:
        try:
            answer = input(prompt_text).strip().lower()
            if not answer:
                answer = default
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("Please answer 'y' or 'n'.")
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(1)


def prompt_text(question, default=""):
    prompt_text = f"{question} [{default}]: "
    try:
        answer = input(prompt_text).strip()
        return answer if answer else default
    except (KeyboardInterrupt, EOFError):
        print("\nAborted.")
        sys.exit(1)


def run_wizard():
    print("Welcome to the Nexus-APCP Interactive Setup Wizard!")
    print("This tool will help you initialize your project with the correct AI context profile.\n")

    # 1. Project Type
    profile_choices = []
    # Build choices based on available profiles
    profiles = available_profiles()
    for p in profiles:
        desc = profile_description(p)
        profile_choices.append({
            "label": f"{p} - {desc}",
            "value": p
        })
    
    # Let's put 'core' as default if it's there
    default_profile_idx = 1
    if "core" in profiles:
        default_profile_idx = profiles.index("core") + 1

    selected_profile = prompt_choice(
        "What type of project are you building?",
        profile_choices,
        default=default_profile_idx
    )

    # 2. Tech Stack
    stack_choices = [
        {"label": "Python / Flask / FastAPI", "value": "python"},
        {"label": "Node.js / Express / Next.js", "value": "node"},
        {"label": "C++ / Unreal Engine", "value": "cpp_ue"},
        {"label": "C# / Unity", "value": "cs_unity"},
        {"label": "Other", "value": "other"}
    ]
    selected_stack = prompt_choice(
        "What is your primary tech stack?",
        stack_choices,
        default=1
    )

    # 3. Target Directory
    target_dir = prompt_text("What is your target directory?", default=".")

    # 4. Overwrite
    overwrite = prompt_yes_no("Do you want to overwrite existing Nexus-APCP files?", default="n")

    print("\n--- Setup Summary ---")
    print(f"Profile: {selected_profile}")
    print(f"Tech Stack: {selected_stack}")
    print(f"Target Directory: {Path(target_dir).resolve()}")
    print(f"Overwrite Existing: {'Yes' if overwrite else 'No'}")
    
    confirm = prompt_yes_no("\nProceed with setup?", default="y")
    if not confirm:
        print("Setup aborted.")
        sys.exit(0)

    print("\nInstalling...")
    result = install_profile(
        target=target_dir,
        profile=selected_profile,
        overwrite=overwrite,
        dry_run=False,
        write_config=True
    )
    
    if result == 0:
        print("\nSetup complete! You can now start using your AI assistant with the initialized context.")
    else:
        print("\nSetup failed.")
        sys.exit(result)


def main():
    parser = argparse.ArgumentParser(description="Nexus-APCP initialization wizard.")
    parser.add_argument("--wizard", action="store_true", help="Run the interactive setup wizard.")
    
    args = parser.parse_args()
    
    if args.wizard:
        run_wizard()
    else:
        print("Please run with --wizard to start the interactive setup.")
        print("Example: python scripts/apcp-init.py --wizard")


if __name__ == "__main__":
    main()
