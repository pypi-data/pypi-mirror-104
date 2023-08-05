from .const import DATA_CLIENT as DATA_CLIENT, DATA_UNSUBSCRIBE as DATA_UNSUBSCRIBE, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity, DEVICE_CLASS_GARAGE as DEVICE_CLASS_GARAGE, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from typing import Any, Callable
from zwave_js_server.client import Client as ZwaveClient

LOGGER: Any
BARRIER_TARGET_CLOSE: int
BARRIER_TARGET_OPEN: int
BARRIER_STATE_CLOSED: int
BARRIER_STATE_CLOSING: int
BARRIER_STATE_STOPPED: int
BARRIER_STATE_OPENING: int
BARRIER_STATE_OPEN: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: Callable) -> None: ...
def percent_to_zwave_position(value: int) -> int: ...

class ZWaveCover(ZWaveBaseEntity, CoverEntity):
    @property
    def is_closed(self) -> Union[bool, None]: ...
    @property
    def current_cover_position(self) -> Union[int, None]: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...

class ZwaveMotorizedBarrier(ZWaveBaseEntity, CoverEntity):
    _target_state: Any = ...
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def supported_features(self) -> Union[int, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def is_opening(self) -> Union[bool, None]: ...
    @property
    def is_closing(self) -> Union[bool, None]: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
