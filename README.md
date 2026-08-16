<div align="center">

# 📦 repo-to-prompt

**A blazingly fast CLI tool to convert any git repository into a single prompt-friendly markdown file for LLMs.**

[![PyPI version](https://badge.fury.io/py/repo-to-prompt.svg)](https://badge.fury.io/py/repo-to-prompt)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

</div>

---

## ✨ Why this exists

When working with large language models (Claude, ChatGPT, etc.), you often want to give them the context of an entire repository. Manually copying and pasting files is tedious.

`repo-to-prompt` instantly walks your repository, respects your `.gitignore`, filters out binary/junk files, and packs everything into a single, beautifully formatted Markdown string ready to be pasted into your favorite LLM.

### Features
- 🚀 **Lightning Fast:** Optimized directory traversal.
- 🛡️ **Gitignore Aware:** Automatically respects your `.gitignore` and default excludes (`node_modules`, `venv`, etc.).
- 📋 **Clipboard Ready:** Use the `-c` flag to copy the entire codebase to your clipboard instantly.

---

## 🚀 Quickstart

### Install
```bash
pip install repo-to-prompt
```

### Usage

Pack the current directory and print to standard output:
```bash
repo2prompt
```

Pack a specific directory and copy directly to clipboard (macOS/Linux/Windows):
```bash
repo2prompt /path/to/my/project -c
```

Save the output to a file:
```bash
repo2prompt . -o codebase_context.md
```

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Who this is for

Repo-to-Prompt is designed for developers who need a clean, prompt-ready Markdown snapshot of a repository for LLM-assisted code review, debugging, architecture discussion, or onboarding. It is intentionally focused on predictable repository packing rather than hidden automation.

## Why star this repository

Star this project if you use AI coding assistants, build repository-to-context workflows, or want a small command-line tool that makes codebase handoff easier.
