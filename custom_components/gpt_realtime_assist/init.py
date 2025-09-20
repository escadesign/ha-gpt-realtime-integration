from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN
from .coordinator import RealtimeClient

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    client=RealtimeClient(hass, entry.data)
    hass.data.setdefault(DOMAIN,{})[entry.entry_id]=client

    async def ptt_start(call): await client.post("/api/ptt/start")
    async def ptt_stop(call):  await client.post("/api/ptt/stop")

    hass.services.async_register(DOMAIN, "ptt_start", ptt_start)
    hass.services.async_register(DOMAIN, "ptt_stop",  ptt_stop)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
