import argparse
import sys
import os
import pyperclip
from rich.console import Console
from repo2prompt.packer import pack_repo

console = Console()

def main():
    parser = argparse.ArgumentParser(description="📦 Repo-to-Prompt Converter")
    parser.add_argument("path", nargs="?", default=".", help="Directory to pack (default: current directory)")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    parser.add_argument("-c", "--copy", action="store_true", help="Copy to clipboard instead of printing")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        console.print(f"[bold red]Error:[/bold red] Directory not found: {args.path}")
        sys.exit(1)
        
    console.print(f"[cyan]Packing repository:[/cyan] {args.path}")
    prompt = pack_repo(args.path)
    
    if args.copy:
        try:
            pyperclip.copy(prompt)
            console.print("[bold green]✅ Successfully copied to clipboard![/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error copying to clipboard:[/bold red] {e}")
            sys.exit(1)
    elif args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(prompt)
        console.print(f"[bold green]✅ Successfully written to {args.output}[/bold green]")
    else:
        # Just print to stdout
        print(prompt)

if __name__ == "__main__":
    main()
