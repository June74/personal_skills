# WSL foundation

Inventory the existing Windows/WSL versions and available RAM/disk before changing them. Ubuntu 24.04 LTS and Python 3.13 were the report's conservative baselines, not newest-version claims. Do not reinstall a working environment merely to match them.

1. Establish WSL2/Ubuntu with a normal Linux user using Microsoft's official instructions.
2. Apply OS updates; confirm Git, CA certificates, Bash/help and ripgrep. Explain each missing apt package before installing it.
3. Place Linux projects in `~/projects`; copy this canonical kit to `~/ai-dev-system` if using Linux clients. Do not share one .venv/node_modules between Windows and Linux.
4. Install a reviewed uv binary; let it manage project Python without replacing `/usr/bin/python3`.
5. For a new Python learning project, `uv init`, select its interpreter, then add dev tools using `uv add --dev pytest ruff mypy`. Inspect pyproject.toml and uv.lock. These commands create/change the project and download dependencies; run them intentionally inside that project.
6. Add Node 24 LTS/npm when browser/frontend tooling is needed. Choose one installation method. Preserve existing lockfile ownership.
7. Connect the chosen coding client to that workspace, then use setup/CLIENTS.md.

Use `pwd`, `command -v python`, `git diff`, `uv tree`, and `npm ls` to understand the environment. Explain unknown flags, pipes, redirects, ports, permissions and PATH as encountered. Avoid sudo pip, blanket chmod and hidden destructive setup scripts.

Keep Unity and Blender beside the Windows GUI when used there. Your custom voice tool can capture microphone/hotkeys on Windows and insert reviewed text into the client while source code lives in WSL. iOS native builds require macOS/Xcode. A container is optional infrastructure, not a prerequisite for ordinary Python, SQLite or Playwright work.

[Microsoft WSL](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) · [uv](https://docs.astral.sh/uv/getting-started/installation/) · [Node releases](https://nodejs.org/en/about/previous-releases)
