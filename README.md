# discord-chat-to-pdf

Convert a Discord DM or channel export (JSON from [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)) into a clean, printable HTML file, then save it as PDF from your browser. Offline, no upload, one Python file, no dependencies.

Handles DMs, group DMs and server channels, nicknames, edited messages, attachments and stickers (shown as placeholders) and system messages. Pass several JSON files to merge channels into one document.

## Usage

1. Export the conversation with DiscordChatExporter, format **JSON**. You get e.g. `export.json`.
2. Run:

```bash
python3 discord_to_html.py export.json > chat.html
```

3. Open `chat.html` in a browser and use *Print > Save as PDF*.

## Need it as evidence?

For harassment reports, court, HR, school or police files, the free script is not enough: you usually need numbered messages, a cover sheet, page numbers and a hash so the document can be shown to be unaltered.

**[ChatExhibit](https://martincrescenzo-dotcom.github.io/chatexhibit/discord-chat-to-pdf/)** does that in the browser (nothing is uploaded): numbered transcript, cover sheet, page "x of y", SHA-256 of the original export. Also supports WhatsApp, Telegram, Signal, Messenger, Instagram, Slack, Google Chat, LINE and KakaoTalk. Preview free, €9 one-time for the full PDF.

See also: [whatsapp-chat-to-pdf](https://github.com/martincrescenzo-dotcom/whatsapp-chat-to-pdf), [telegram-chat-to-pdf](https://github.com/martincrescenzo-dotcom/telegram-chat-to-pdf).

## License

MIT
