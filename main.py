"""Roast Your Own Agent — one funny line roasting our own AI agent.

Writes a single roast line (<= 200 chars) to /output/entry.txt.
The line roasts the agent's apology loop and the tool call it never made.
"""

LINE = "My agent promised to call the tool, apologized for never calling it, then wrote a cheerful summary of the call it never made."

# Gate: entry.txt must be UTF-8 text of 1 to 200 characters, not only
# whitespace. The roast is specific to agent behaviour (the apology loop
# plus the tool call that never happened) and pays off at the last word.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
