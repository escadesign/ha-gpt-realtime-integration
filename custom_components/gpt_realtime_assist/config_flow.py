from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from .const import CONF_USERNAME, CONF_PASSWORD
import voluptuous as vol, aiohttp

class ConfigFlow(config_entries.ConfigFlow, domain="gpt_realtime_assist"):
    VERSION=1
    async def async_step_user(self, user_input=None):
        errors={}
        if user_input:
            host=user_input[CONF_HOST].rstrip("/")
            try:
                async with aiohttp.ClientSession() as s:
                    async with s.get(f"{host}/api/health", timeout=5) as r:
                        if r.status==200:
                            return self.async_create_entry(title="GPT Realtime Assist", data=user_input)
                        errors["base"]="cannot_connect"
            except Exception:
                errors["base"]="cannot_connect"
        schema=vol.Schema({
            vol.Required(CONF_HOST, default="https://homeassistant.local:8443"): str,
            vol.Optional(CONF_USERNAME, default="admin"): str,
            vol.Optional(CONF_PASSWORD, default="ha"): str
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
