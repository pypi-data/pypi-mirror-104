from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from typing import Any

_LOGGER: Any
DOMAIN: str
ENTITY_ID_FORMAT: Any
SCAN_INTERVAL: Any
DEVICE_CLASSES: Any
DEVICE_CLASSES_SCHEMA: Any

async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...

class SensorEntity(Entity): ...
