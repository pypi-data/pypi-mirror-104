import homeassistant.core
from enum import Enum
from typing import Any, Dict, Mapping, Optional, Tuple, Union

GPSType = Tuple[float, float]
ConfigType = Dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = Dict[str, Any]
EventType = homeassistant.core.Event
ServiceCallType = homeassistant.core.ServiceCall
ServiceDataType = Dict[str, Any]
StateType = Union[None, str, int, float]
TemplateVarsType = Optional[Mapping[str, Any]]
HomeAssistantType = homeassistant.core.HomeAssistant
QueryType = Any

class UndefinedType(Enum):
    _singleton: int = ...

UNDEFINED: Any
