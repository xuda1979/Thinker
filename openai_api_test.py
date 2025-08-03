#!/usr/bin/env python
import os, sys, httpx
from openai import OpenAI, APITimeoutError

# --------- user input & env ----------
prompt   = " ".join(sys.argv[1:]) or "ping"
api_key  = os.environ["OPENAI_API_KEY"]           # must be set
proxy    = os.getenv("HTTPS_PROXY")               # e.g. http://127.0.0.1:7078
timeout  = httpx.Timeout(120, connect=10)

 

transport = httpx.HTTPTransport(proxy=proxy)        # works with no extra deps
http_client = httpx.Client(transport=transport,
                           timeout=httpx.Timeout(120, connect=10))


# --------- OpenAI client ----------
client = OpenAI(api_key=api_key, http_client=http_client)

try:
    for chunk in client.chat.completions.create(
            model="gpt-4o-mini",                 # pick any ID from your curl list
            stream=True,
            messages=[{"role": "user", "content": prompt}]
        ):
        if (delta := chunk.choices[0].delta.content):
            print(delta, end="", flush=True)
    print()
except APITimeoutError:
    print("⏱️  Still timing out – check quota, try another model, or switch exit node.")
