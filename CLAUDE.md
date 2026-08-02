# repo-to-prompt - AI Agent Guidelines

## Agent Context
If a user asks you to add new features to this tool:
1. Efficiency is key. When walking the filesystem, modify `dirnames` in-place so `os.walk` doesn't traverse massive directories like `node_modules`.
2. Do not execute any files. Only read them as UTF-8 text.
