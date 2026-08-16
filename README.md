# MCP Protocol Guide

Практический русскоязычный гайд по **Model Context Protocol (MCP)**: от базовой идеи до первого рабочего сервера.

> Цель репозитория — за 10–15 минут дать понятную картину: **что такое MCP, как устроена связка Host → Client → Server и чем отличаются Tools, Resources и Prompts**.

## Что такое MCP

MCP — открытый протокол, который стандартизирует взаимодействие AI-приложений с внешними данными, инструментами и контекстом.

Вместо того чтобы писать отдельную интеграцию под каждый источник, приложение использует единый протокол общения с MCP-серверами.

Упрощённо:

```text
Пользователь
    ↓
Host / AI-приложение
    ↓
MCP Client
    ↓
MCP Server
    ↓
Tools / Resources / Prompts
```

## Три ключевые примитивы

| Примитив | Что это | Пример |
|---|---|---|
| **Tools** | Выполняемые функции, которые модель может вызвать | запрос к API, поиск CVE, запись файла |
| **Resources** | Данные и контекст, которые приложение может передать модели | файл, конфиг, git history, документация |
| **Prompts** | Переиспользуемые шаблоны взаимодействия | шаблон анализа CVE, формат отчёта |

Главная мысль:

> **MCP не делает модель умнее. Он даёт ей стандартизированный способ видеть и использовать внешние возможности.**

## Архитектура

- **Host** — приложение, в котором работает пользователь и AI-логика.
- **MCP Client** — клиентская часть внутри Host, которая говорит с MCP Server.
- **MCP Server** — публикует доступные инструменты, ресурсы и промпты.
- **Tools / Resources / Prompts** — конкретные возможности, которые сервер открывает клиенту.

Подробно: [`docs/architecture.md`](docs/architecture.md)

## Быстрый старт

Репозиторий содержит минимальный сервер на официальном Python SDK.

### Требования

- Python 3.10+
- `uv` или `pip`

### Установка

```bash
git clone https://github.com/TopskiyPavelQwertyGang/mcp-protocol-guide.git
cd mcp-protocol-guide

uv sync
```

Или через `pip`:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install "mcp[cli]"
```

### Запуск через MCP Inspector

```bash
uv run mcp dev server.py
```

Inspector позволит увидеть, какие **Tools, Resources и Prompts** публикует сервер, и вызвать их вручную.

### Запуск как HTTP MCP Server

```bash
uv run python server.py
```

По умолчанию сервер поднимается через Streamable HTTP на endpoint:

```text
http://127.0.0.1:8000/mcp
```

## Что есть в демо

`server.py` публикует три простых объекта:

```text
Tool      → add(a, b)
Resource  → package://{name}
Prompt    → analyze_package(name)
```

Это специально минимальный пример: сначала важно увидеть саму механику протокола, а уже потом подключать реальные API, базы данных и shell.

## Структура репозитория

```text
.
├── README.md
├── QUICKSTART.md
├── server.py
├── pyproject.toml
├── docs/
│   ├── architecture.md
│   └── primitives.md
└── SECURITY_NOTES.md
```

## Что изучать дальше

Этот репозиторий — **первый уровень learning path**.

1. **mcp-protocol-guide** — понять протокол и базовые примитивы.
2. **mcp-secure-agents** — научиться ограничивать агента: allowlist, permissions, validation, HITL, sandbox.
3. **mcp-use-cases** — посмотреть готовые сценарии: CVE-анализ, API, базы данных, файлы и автоматизация.

## Важно про безопасность

MCP стандартизирует взаимодействие, но **не является автоматической границей безопасности**.

Если сервер публикует опасный инструмент, модель потенциально сможет его вызвать. Поэтому права, валидация, allowlist, sandbox и подтверждение человеком должны проектироваться отдельно.

Коротко: [`SECURITY_NOTES.md`](SECURITY_NOTES.md)

## Версия протокола

Материалы ориентированы на актуальную спецификацию MCP **2026-07-28** и официальный Python SDK v2.

## Полезные ссылки

- Официальная документация MCP: https://modelcontextprotocol.io/
- Спецификация: https://github.com/modelcontextprotocol/modelcontextprotocol
- Python SDK: https://github.com/modelcontextprotocol/python-sdk

---

Сделано как практическое дополнение к докладу про AI-агентов, MCP и безопасность.