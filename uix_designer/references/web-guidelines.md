# Web Guidelines — Vercel Source

Fetch fresh before each review:
```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Output terse `file:line` findings. No caching stale. Host must authorize outbound fetch.

Use `tools/web_guidelines.py:fetch_guidelines()` then apply to `checks/guideline.py`.
