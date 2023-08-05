from . import GroupEntity as GroupEntity
from collections.abc import Iterator
from homeassistant.components import light as light
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_MIREDS as ATTR_MAX_MIREDS, ATTR_MIN_MIREDS as ATTR_MIN_MIREDS, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE_VALUE as ATTR_WHITE_VALUE, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_COLOR_TEMP as SUPPORT_COLOR_TEMP, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_FLASH as SUPPORT_FLASH, SUPPORT_TRANSITION as SUPPORT_TRANSITION, SUPPORT_WHITE_VALUE as SUPPORT_WHITE_VALUE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Callable

DEFAULT_NAME: str
SUPPORT_GROUP_LIGHT: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Any, discovery_info: Any=...) -> None: ...

class LightGroup(GroupEntity, light.LightEntity):
    _name: Any = ...
    _entity_ids: Any = ...
    _is_on: bool = ...
    _available: bool = ...
    _icon: str = ...
    _brightness: Any = ...
    _hs_color: Any = ...
    _color_temp: Any = ...
    _min_mireds: int = ...
    _max_mireds: int = ...
    _white_value: Any = ...
    _effect_list: Any = ...
    _effect: Any = ...
    _supported_features: int = ...
    def __init__(self, name: str, entity_ids: list[str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def icon(self): ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def white_value(self) -> Union[int, None]: ...
    @property
    def effect_list(self) -> Union[list[str], None]: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def extra_state_attributes(self): ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...

def _find_state_attributes(states: list[State], key: str) -> Iterator[Any]: ...
def _mean_int(*args: Any): ...
def _mean_tuple(*args: Any): ...
def _reduce_attribute(states: list[State], key: str, default: Union[Any, None]=..., reduce: Callable[..., Any]=...) -> Any: ...
