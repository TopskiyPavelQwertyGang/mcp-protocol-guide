# Quick Start

Цель: за несколько минут поднять минимальный MCP-сервер и увидеть его возможности через MCP Inspector.

## 1. Клонируйте репозиторий

```bash
git clone https://github.com/TopskiyPavelQwertyGang/mcp-protocol-guide.git
cd mcp-protocol-guide
```

## 2. Установите зависимости

### Вариант A — uv

```bash
uv sync
```

### Вариант B — pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]"
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install "mcp[cli]"
```

## 3. Откройте сервер в Inspector

С `uv`:

```bash
uv run mcp dev server.py
```

После запуска попробуйте три примитива:

- **Tool:** вызовите `add` с `a=2`, `b=3`.
- **Resource:** откройте `package://freerdp3`.
- **Prompt:** получите `analyze_package` для `freerdp3`.

## 4. Запустите Streamable HTTP

```bash
uv run python server.py
```

Endpoint:

```text
http://127.0.0.1:8000/mcp
```

## Что важно заметить

Все три возможности публикует **один MCP Server**, а клиент получает их через стандартный протокол.

В этом учебном сервере намеренно нет shell, записи в БД и внешних API. Следующий уровень — `mcp-secure-agents`, где мы добавим реальные действия и ограничения безопасности.
