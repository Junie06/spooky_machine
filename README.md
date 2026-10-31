# Spooky Machine

A tiny ghost story generator powered by a local open-weight model.

## Run

Install [Python 3.11+](https://www.python.org/) and [Ollama](https://ollama.com/), then run:

```powershell
ollama create spooky-qwen3 -f Modelfile
python server.py
```

The `Modelfile` makes a small `spooky-qwen3` variant from your already-installed Qwen3 model and disables its reasoning prefix, so the app gets the story instead of the model's planning text. Open <http://127.0.0.1:8000>, optionally add a story idea, and ask for a ghost story. Your idea stays on this computer.

If you don't have `qwen3:4b` yet, run `ollama pull qwen3:4b` first. Run the tests with:

```powershell
python -m unittest discover -s tests -v
```
