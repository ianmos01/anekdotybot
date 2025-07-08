# AnekdotyBot

Example modular Telegram bot using aiogram v3.

Run the bot locally with:

```bash
python -m app.run
```

## Deploying to Railway

Install dependencies and run the bot using the provided `Procfile`. Railway will
start the application with:

```bash
python -m app.railway
```

Make sure to set the `BOT_TOKEN` environment variable in your Railway project.
