#!/usr/bin/env python3
"""Convert a DiscordChatExporter JSON export to printable HTML.

Usage: python3 discord_to_html.py export.json [more.json ...] > chat.html
Then open chat.html in a browser and Print > Save as PDF. Offline, no dependencies.
"""
import html, json, sys


def body_of(m):
    parts = [m.get("content") or ""]
    for a in m.get("attachments") or []:
        parts.append(f"[attachment: {a.get('fileName', 'file')}]")
    for s in m.get("stickers") or []:
        parts.append(f"[sticker: {s.get('name', '')}]")
    if m.get("embeds") and not parts[0]:
        parts.append("[embed]")
    return " ".join(p for p in parts if p).strip()


def main(paths):
    out = ["<!doctype html><meta charset='utf-8'><title>Discord chat</title>",
           "<style>body{font:14px/1.45 system-ui,sans-serif;max-width:800px;margin:2em auto}"
           ".m{margin:.35em 0;page-break-inside:avoid}.d{color:#666;font-size:12px}"
           ".n{font-weight:600}.s{color:#888;font-style:italic}.e{color:#999;font-size:11px}h2{margin-top:2em}</style>"]
    for p in paths:
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        g = (data.get("guild") or {}).get("name", "")
        c = (data.get("channel") or {}).get("name", "")
        out.append(f"<h2>{html.escape(g)}{' / ' if g and c else ''}{html.escape(c)}</h2>")
        for m in data.get("messages", []):
            date = html.escape((m.get("timestamp") or "")[:19].replace("T", " "))
            a = m.get("author") or {}
            name = html.escape(a.get("nickname") or a.get("name") or "")
            body = html.escape(body_of(m)).replace("\n", "<br>")
            edited = " <span class='e'>(edited)</span>" if m.get("timestampEdited") else ""
            if m.get("type") not in (None, "Default", "Reply"):
                out.append(f"<div class='m s'><span class='d'>{date}</span> {name} {html.escape(m['type'])} {body}</div>")
                continue
            out.append(f"<div class='m'><span class='d'>{date}</span> <span class='n'>{name}:</span> {body}{edited}</div>")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
