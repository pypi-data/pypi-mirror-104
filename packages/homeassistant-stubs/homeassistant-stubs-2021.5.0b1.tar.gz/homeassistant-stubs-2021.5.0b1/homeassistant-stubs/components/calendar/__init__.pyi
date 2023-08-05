from aiohttp import web
from homeassistant.components import http as http
from homeassistant.const import HTTP_BAD_REQUEST as HTTP_BAD_REQUEST, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, time_period_str as time_period_str
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.template import DATE_STR_FORMAT as DATE_STR_FORMAT
from homeassistant.util import dt as dt
from typing import Any

_LOGGER: Any
DOMAIN: str
ENTITY_ID_FORMAT: Any
SCAN_INTERVAL: Any

async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...
def get_date(date: Any): ...
def normalize_event(event: Any): ...
def calculate_offset(event: Any, offset: Any): ...
def is_offset_reached(event: Any): ...

class CalendarEventDevice(Entity):
    @property
    def event(self) -> None: ...
    @property
    def state_attributes(self): ...
    @property
    def state(self): ...
    async def async_get_events(self, hass: Any, start_date: Any, end_date: Any) -> None: ...

class CalendarEventView(http.HomeAssistantView):
    url: str = ...
    name: str = ...
    component: Any = ...
    def __init__(self, component: EntityComponent) -> None: ...
    async def get(self, request: Any, entity_id: Any): ...

class CalendarListView(http.HomeAssistantView):
    url: str = ...
    name: str = ...
    component: Any = ...
    def __init__(self, component: EntityComponent) -> None: ...
    async def get(self, request: web.Request) -> web.Response: ...
