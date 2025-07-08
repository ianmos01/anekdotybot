from dataclasses import dataclass
import os

@dataclass
class BotConfig:
    token: str = os.getenv('BOT_TOKEN', '')
    parse_mode: str = 'HTML'

config = BotConfig()
