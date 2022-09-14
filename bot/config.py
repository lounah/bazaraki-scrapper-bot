from dataclasses import dataclass


@dataclass
class ServerConfig:
    token: str
    port: int
    url: str

    def hook_url(self) -> str:
        return f"{self.url}:{self.port}/{self.token}"
