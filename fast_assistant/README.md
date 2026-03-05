# Fast Assistant

A quick-response AI assistant powered by Google's Gemini model through the OpenAI Agents SDK.

## Features

- ⚡ Optimized for quick responses
- 🤖 Powered by Gemini 2.5 Flash model
- 💬 Concise, helpful answers
- 🔒 Secure API key management via environment variables
- ⚡ Built with the OpenAI Agents SDK

## Requirements

- Python 3.13+
- Gemini API key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
cd fast_assistant

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

Run the assistant:

```bash
# Using uv
uv run python main.py

# Using Python directly (after activating venv)
python main.py
```

### Example Output

```
4
```

## Project Structure

```
fast_assistant/
├── main.py              # Main assistant implementation
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
