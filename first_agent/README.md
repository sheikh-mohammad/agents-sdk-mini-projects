# First Agent

Your first AI agent powered by Google's Gemini model through the OpenAI Agents SDK. A great starting point for learning about AI agents.

## Features

- 🎯 Perfect introduction to AI agents
- 🤖 Powered by Gemini 2.5 Flash model
- 💬 Friendly, helpful responses
- 🔒 Secure API key management via environment variables
- ⚡ Built with the OpenAI Agents SDK

## Requirements

- Python 3.13+
- Gemini API key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
cd first_agent

# Install dependencies
uv sync
```

### Using pip

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:

```bash
cp .env.example .env  # On Windows: copy .env.example .env
```

2. Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the agent:

```bash
# Using uv
uv run python main.py

# Using Python directly (after activating venv)
python main.py
```

### Example Output

```
Hello! I'm here to help you with a wide range of tasks. I can answer questions, provide information, help with problem-solving, assist with writing, or just have a friendly conversation. What would you like help with today?
```

## Project Structure

```
first_agent/
├── main.py              # Main agent implementation
├── pyproject.toml       # Project dependencies and metadata
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| openai | >=2.24.0 | OpenAI Python client |
| openai-agents | >=0.10.2 | OpenAI Agents SDK |
| python-dotenv | >=1.2.1 | Environment variable management |

## Learning Resources

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/)