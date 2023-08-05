from . import DOMAIN as DOMAIN
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation import TRIGGER_BASE_SCHEMA as TRIGGER_BASE_SCHEMA
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE, STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

TRIGGER_TYPES: Any
TRIGGER_SCHEMA: Any

async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...
