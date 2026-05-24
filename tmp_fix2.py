import sys
import re
sys.path.insert(0, 'scripts')
from apcp_core_files import LOCAL_EXCLUDE_PATTERNS

ps1_lines = ['    "' + p + '"' for p in LOCAL_EXCLUDE_PATTERNS]
sh_lines = ['add_pattern "' + p + '"' for p in LOCAL_EXCLUDE_PATTERNS]

with open('scripts/install-local-excludes.ps1', 'r', encoding='utf-8') as f:
    ps1_text = f.read()
    
ps1_text = re.sub(r'\$patterns = @\([^)]+\)', '$patterns = @(\n    "# Nexus-APCP local agent operating files",\n' + ',\n'.join(ps1_lines) + '\n)', ps1_text)

with open('scripts/install-local-excludes.ps1', 'w', encoding='utf-8') as f:
    f.write(ps1_text)

with open('scripts/install-local-excludes.sh', 'r', encoding='utf-8') as f:
    sh_text = f.read()
    
sh_text = re.sub(r'(add_pattern "# Nexus-APCP local agent operating files".*?)echo "Updated local Git excludes:', 'add_pattern "# Nexus-APCP local agent operating files"\n' + '\n'.join(sh_lines) + '\n\necho "Updated local Git excludes:', sh_text, flags=re.DOTALL)

with open('scripts/install-local-excludes.sh', 'w', encoding='utf-8') as f:
    f.write(sh_text)
