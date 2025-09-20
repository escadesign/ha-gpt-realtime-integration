from homeassistant.core import HomeAssistant
from .const import CONF_USERNAME, CONF_PASSWORD, CONF_HOST
import aiohttp, base64

class RealtimeClient:
    def __init__(self, hass:HomeAssistant, cfg):
        self.hass=hass
        self.host=cfg["host"].rstrip("/")
        self.user=cfg.get(CONF_USERNAME,"admin")
        self.pw=cfg.get(CONF_PASSWORD,"ha")

    async def post(self, path:str):
        auth=base64.b64encode(f"{self.user}:{self.pw}".encode()).decode()
        async with aiohttp.ClientSession() as s:
            async with s.post(f"{self.host}{path}", headers={"Authorization": f"Basic {auth}"}, timeout=30) as r:
                if r.status not in (200,204):
                    raise RuntimeError(f"POST {path} failed: {r.status} {await r.text()}")
