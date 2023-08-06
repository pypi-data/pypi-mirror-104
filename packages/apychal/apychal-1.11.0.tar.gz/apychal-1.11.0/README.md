# Apychal
## What?
This is the async version of [pychal](https://github.com/ZEDGR/pychal).

*Why don't you submit this as a PR?* What I did here was very simple. However it breaks compatibility with older versions of Python, which can be an issue. If you're going to use an async version of `pychal`, I think you're already aware of the reason why! `apychal` was initially made to work with [ATOS](https://github.com/Wonderfall/ATOS) (which is now [here](https://github.com/retke/Laggrons-Dumb-Cogs/tree/v3/tournaments)), a Discord bot relying on asynchronous tasks to be efficient.

## Requirements
Please note that it :
- Only supports **Python 3.6+** (modern `asyncio`, removed legacy code).
- Replaces `requests` with `aiohttp` (which makes this module asynchronous).

## How to use
That's it for the main differences, otherwise it should be the same to use as the original.

You can install `apychal` with PyPI :
```
pip install apychal
```

## Get started (example)
```python
import asyncio
import achallonge

achallonge.set_credentials("user", "my_api_key")

async def main():
    participants = await achallonge.participants.index('mytournament')
    print(participants)

asyncio.run(main())
```