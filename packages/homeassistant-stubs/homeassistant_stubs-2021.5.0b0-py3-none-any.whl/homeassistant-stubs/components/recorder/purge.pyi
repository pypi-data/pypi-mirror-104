from . import Recorder as Recorder
from .const import MAX_ROWS_TO_PURGE as MAX_ROWS_TO_PURGE
from .models import Events as Events, RecorderRuns as RecorderRuns, States as States
from .repack import repack_database as repack_database
from .util import session_scope as session_scope
from datetime import datetime
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Any
RETRYABLE_MYSQL_ERRORS: Any

def purge_old_data(instance: Recorder, purge_days: int, repack: bool, apply_filter: bool=...) -> bool: ...
def _select_event_ids_to_purge(session: Session, purge_before: datetime) -> list[int]: ...
def _select_state_ids_to_purge(session: Session, purge_before: datetime, event_ids: list[int]) -> list[int]: ...
def _purge_state_ids(session: Session, state_ids: list[int]) -> None: ...
def _purge_event_ids(session: Session, event_ids: list[int]) -> None: ...
def _purge_old_recorder_runs(instance: Recorder, session: Session, purge_before: datetime) -> None: ...
def _purge_filtered_data(instance: Recorder, session: Session) -> bool: ...
def _purge_filtered_states(session: Session, excluded_entity_ids: list[str]) -> None: ...
def _purge_filtered_events(session: Session, excluded_event_types: list[str]) -> None: ...
