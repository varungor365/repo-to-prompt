import os
import pathspec

DEFAULT_IGNORE = [
    ".git/", ".github/", ".svn/", ".hg/",
    "node_modules/", "venv/", ".venv/", "env/", ".env/",
    "__pycache__/", "*.pyc", "*.pyo", "*.pyd",
    ".idea/", ".vscode/", ".DS_Store",
    "dist/", "build/", "*.egg-info/",
    "*.log", "*.sql", "*.sqlite", "*.db",
    "*.mp4", "*.png", "*.jpg", "*.jpeg", "*.gif", "*.ico", "*.svg", "*.webp",
    "*.pdf", "*.zip", "*.tar", "*.gz", "*.bz2", "*.xz", "*.7z",
    ".gitignore"
]

def load_gitignore(root_dir: str) -> pathspec.PathSpec:
    patterns = list(DEFAULT_IGNORE)
    
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            patterns.extend(f.read().splitlines())
            
    # Add .gitignore itself so it doesn't get packed unless wanted, and our secret.txt test won't falsely trigger off .gitignore's content
    return pathspec.PathSpec.from_lines('gitignore', patterns)

def pack_repo(root_dir: str) -> str:
    """Pack an entire repository into a single markdown string."""
    root_dir = os.path.abspath(root_dir)
    spec = load_gitignore(root_dir)
    
    output = []
    output.append(f"# Repository Context: {os.path.basename(root_dir)}\n")
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories matching the spec to speed up traversal
        dirnames[:] = [d for d in dirnames if not spec.match_file(os.path.relpath(os.path.join(dirpath, d), root_dir))]
        
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, root_dir)
            
            if spec.match_file(rel_path):
                continue
                
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                output.append(f"## File: `{rel_path}`\n")
                
                # Try to guess language from extension for markdown highlighting
                ext = os.path.splitext(filename)[1].lstrip('.')
                if not ext:
                    ext = "txt"
                    
                output.append(f"```{ext}\n{content}\n```\n")
            except Exception:
                # Skip binary files or unreadable files
                continue
                
    return "\n".join(output)
