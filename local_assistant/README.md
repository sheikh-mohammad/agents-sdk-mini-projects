# Local Assistant

A locally-running AI assistant powered by Google's Gemini model through the OpenAI Agents SDK.

## Features

- 🏠 Runs locally on your machine
- 🤖 Powered by Gemini 2.0 Flash model
- 💬 Helpful, contextual responses
- 🔒 Secure API key management via environment variables
- ⚡ Built with the OpenAI Agents SDK
- 🔧 Easy to customize and extend

## Requirements

- Python 3.13+
- Gemini API key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
cd local_assistant

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
The capital of France is Paris.
```

## Project Structure

```
local_assistant/
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
| openai-agents | >=0.10.4 | OpenAI Agents SDK |
| python-dotenv | >=1.2.2 | Environment variable management |

## Customization

### Change the Assistant's Personality

Modify the `instructions` parameter in `main.py`:

```python
local_assistant: Agent = Agent(
    name="Local Assistant",
    instructions="You are a helpful assistant running locally.",  # Customize this
    model=external_model,
)
```

### Change the Query

Modify the input query in `main.py`:

```python
result = Runner.run_sync(local_assistant, "Your question here")
```

## License

MIT
