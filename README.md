# Agents SDK Mini Projects

> 🤖 A curated collection of AI agent mini-projects built with the OpenAI Agents SDK and Google's Gemini models.

A hands-on exploration of AI agent implementations, demonstrating various configurations, use cases, and integration patterns. Each project is a standalone application showcasing different aspects of conversational AI development.

---

## 📁 Projects Overview

### Core Assistants

| Project | Description | Version | Status |
|---------|-------------|---------|--------|
| [`assistant/`](./assistant/) | General-purpose AI assistant with friendly, brief responses | v2.0.0 | ✅ Complete |
| [`fast_assistant/`](./fast_assistant/) | Optimized for quick, concise answers | v2.0.0 | ✅ Complete |
| [`first_agent/`](./first_agent/) | Introductory agent - perfect for learning AI agent basics | v2.0.0 | ✅ Complete |

### Specialized Assistants

| Project | Description | Version | Status |
|---------|-------------|---------|--------|
| [`gemini_assistant/`](./gemini_assistant/) | Concise responses using Gemini 2.0 Flash | v1.0.0 | ✅ Complete |
| [`local_assistant/`](./local_assistant/) | Locally-running assistant with full customization | v1.0.0 | ✅ Complete |
| [`news_agent/`](./news_agent/) | News aggregation and summarization agent | - | 🚧 In Progress |
| [`support_desk/`](./support_desk/) | Customer support desk simulation agent | - | 🚧 In Progress |
| [`task_manager/`](./task_manager/) | Task management and productivity agent | - | 🚧 In Progress |
| [`time_agent/`](./time_agent/) | Time-related queries and scheduling agent | - | 🚧 In Progress |

---

## 🎯 Purpose

This collection serves as:

- **Learning Resource**: Understand AI agent architecture and implementation patterns
- **Reference Code**: Quick starting point for building your own agents
- **Experimentation Platform**: Test different models, configurations, and instructions
- **Portfolio**: Showcase practical AI integration skills

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.13+** installed
2. **[uv](https://github.com/astral-sh/uv)** package manager (recommended)
3. **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Setup Any Project

```bash
# 1. Clone the repository
git clone https://github.com/sheikh-mohammad/agents-sdk-mini-projects.git
cd agents-sdk-mini-projects

# 2. Navigate to a project
cd assistant

# 3. Install dependencies
uv sync

# 4. Configure environment
cp .env.example .env

# 5. Edit .env and add your API key
# GEMINI_API_KEY=your_actual_api_key_here

# 6. Run the project
uv run python main.py
```

### Alternative: Using pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install openai openai-agents python-dotenv

# Run the project
python main.py
```

---

## 🏗️ Project Structure

Each project follows a consistent structure:

```
project_name/
├── main.py              # Main agent implementation
├── pyproject.toml       # Dependencies and project metadata
├── .env.example         # Environment variable template
├── .gitignore           # Git ignore rules
└── README.md            # Project-specific documentation
```

### Typical Agent Implementation

```python
from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize client with Gemini API
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Configure model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=client
)

# Create agent with custom instructions
agent = Agent(
    name="My Assistant",
    instructions="You are a helpful assistant.",
    model=model,
)

# Run the agent
result = Runner.run_sync(agent, "Your prompt here")
print(result.final_output)
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

### Available Models

| Model | Description | Best For |
|-------|-------------|----------|
| `gemini-2.0-flash` | Fast, efficient model | General tasks, quick responses |
| `gemini-2.5-flash` | Latest flash model | Improved accuracy and speed |

---

## 📚 Technologies Used

| Technology | Purpose |
|------------|---------|
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Agent framework and runtime |
| [Google Gemini API](https://ai.google.dev/) | LLM backend |
| [uv](https://github.com/astral-sh/uv) | Fast Python package management |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variable management |
| [OpenAI Python Client](https://github.com/openai/openai-python) | API client compatibility |

---

## 📖 Learning Resources

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/)
- [Getting Your Gemini API Key](https://aistudio.google.com/app/apikey)

---

## ⚠️ License and Usage Terms

> **This is a personal project collection created by Sheikh Mohammad Ahmed.**

### Permitted Use

- ✅ **Review**: Study the code for learning purposes
- ✅ **Inspiration**: Use as inspiration for your own projects
- ✅ **Educational Use**: Understand AI agent implementation patterns

### Restrictions

- ❌ **No Direct Copying**: Copying code or ideas without attribution is **not allowed**
- ❌ **No Plagiarism**: Presenting this work as your own is **prohibited**
- ❌ **No Commercial Use**: Commercial use requires explicit permission

### Attribution Requirement

If you draw inspiration from this collection, you **must**:

1. Credit **Sheikh Mohammad Ahmed** as the original author
2. Link to this repository: `https://github.com/sheikh-mohammad/agents-sdk-mini-projects`
3. State that your work was inspired by this project collection

**Example Attribution:**
```
Inspired by agents-sdk-mini-projects by Sheikh Mohammad Ahmed
https://github.com/sheikh-mohammad/agents-sdk-mini-projects
```

See [LICENSE](./LICENSE) for complete terms.

---

## 🤝 Contributing

This is a personal learning project. However, feel free to:

- ⭐ Star the repository if you find it useful
- 📢 Share with others learning AI development
- 💡 Open issues for suggestions or improvements

---

## 📬 Contact

- **Author**: Sheikh Mohammad Ahmed
- **GitHub**: [@sheikh-mohammad](https://github.com/sheikh-mohammad)
- **Repository**: [agents-sdk-mini-projects](https://github.com/sheikh-mohammad/agents-sdk-mini-projects)

---

**Copyright © 2026 Sheikh Mohammad Ahmed. All Rights Reserved.**
