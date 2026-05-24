import os

mapping = {
    "./AI_MAIN.md": "./rules/AI_MAIN.md",
    "AI_MAIN.md": "rules/AI_MAIN.md",
    "./DECISION_LOG_PROTOCOL.md": "./rules/DECISION_LOG_PROTOCOL.md",
    "DECISION_LOG_PROTOCOL.md": "rules/DECISION_LOG_PROTOCOL.md",
    "./CONTEXT_OPTIMIZATION.md": "./rules/CONTEXT_OPTIMIZATION.md",
    "CONTEXT_OPTIMIZATION.md": "rules/CONTEXT_OPTIMIZATION.md",
    "./VISUAL_CONTEXT_MERMAID.md": "./rules/VISUAL_CONTEXT_MERMAID.md",
    "VISUAL_CONTEXT_MERMAID.md": "rules/VISUAL_CONTEXT_MERMAID.md",
    "./AI_AGENT_SKILLS_PROTOCOL.md": "./rules/AI_AGENT_SKILLS_PROTOCOL.md",
    "AI_AGENT_SKILLS_PROTOCOL.md": "rules/AI_AGENT_SKILLS_PROTOCOL.md",
    "./AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md": "./rules/AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md",
    "AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md": "rules/AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md",
    "./CODEGRAPH_INTEGRATION_PROTOCOL.md": "./rules/CODEGRAPH_INTEGRATION_PROTOCOL.md",
    "CODEGRAPH_INTEGRATION_PROTOCOL.md": "rules/CODEGRAPH_INTEGRATION_PROTOCOL.md",
    "./FILE_STRUCTURE_REFACTOR_PROTOCOL.md": "./rules/FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "FILE_STRUCTURE_REFACTOR_PROTOCOL.md": "rules/FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "./AI_ASSISTANT_PROMPT_TEMPLATES.md": "./templates/AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "AI_ASSISTANT_PROMPT_TEMPLATES.md": "templates/AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "./DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md": "./rules/DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
    "DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md": "rules/DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
    "./WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md": "./rules/WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md": "rules/WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "./MACP_IMPLEMENTATION_GUIDE.md": "./rules/MACP_IMPLEMENTATION_GUIDE.md",
    "MACP_IMPLEMENTATION_GUIDE.md": "rules/MACP_IMPLEMENTATION_GUIDE.md",
    "./WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md": "./templates/WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md": "templates/WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "./UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md": "./rules/UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md": "rules/UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "./DEBLOAT_APPLICATION_GUIDE.md": "./templates/DEBLOAT_APPLICATION_GUIDE.md",
    "DEBLOAT_APPLICATION_GUIDE.md": "templates/DEBLOAT_APPLICATION_GUIDE.md",
    "./WATERFALL_DEVELOPMENT_PROTOCOL.md": "./templates/WATERFALL_DEVELOPMENT_PROTOCOL.md",
    "WATERFALL_DEVELOPMENT_PROTOCOL.md": "templates/WATERFALL_DEVELOPMENT_PROTOCOL.md",
    "./DISCOVER_ALGORITHM_DESIGN_GUIDE.md": "./templates/DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "DISCOVER_ALGORITHM_DESIGN_GUIDE.md": "templates/DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "./FRONTEND_APPLICATION_DESIGN_PROTOCOL.md": "./templates/FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "FRONTEND_APPLICATION_DESIGN_PROTOCOL.md": "templates/FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "./UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md": "./templates/UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
    "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md": "templates/UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
    "./CAVEMAN_RULES.md": "./CONTRIBUTING.md",
    "CAVEMAN_RULES.md": "CONTRIBUTING.md",
    "./EMOJI_POLICY.md": "./CONTRIBUTING.md",
    "EMOJI_POLICY.md": "CONTRIBUTING.md",
}

def fix_links_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return
        
    new_content = content
    folder = os.path.basename(os.path.dirname(os.path.abspath(filepath)))
    
    for old, new in mapping.items():
        if folder in ["rules", "templates"]:
            if old.startswith("./"):
                new_relative = new.replace("./", "../")
            else:
                new_relative = "../" + new
            
            # Special case for files that moved to root or stayed in root
            if old in ["./AI_PROJECT_CONTEXT_PROTOCOL.md", "AI_PROJECT_CONTEXT_PROTOCOL.md"]:
                new_relative = "../AI_PROJECT_CONTEXT_PROTOCOL.md"
            elif old in ["./TASK_PROGRESS.yaml", "TASK_PROGRESS.yaml"]:
                new_relative = "../TASK_PROGRESS.yaml"
            
            new_content = new_content.replace(f"({old})", f"({new_relative})")
            new_content = new_content.replace(f"[{old}]", f"[{new_relative}]")
        else:
            new_content = new_content.replace(f"({old})", f"({new})")
            new_content = new_content.replace(f"[{old}]", f"[{new}]")

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root_dir, _, files in os.walk("."):
    if ".git" in root_dir or "node_modules" in root_dir:
        continue
    for file in files:
        if file.endswith(".md"):
            fix_links_in_file(os.path.join(root_dir, file))
