from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: int


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
