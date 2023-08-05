"""
"""

import enum
import logging

LOGGER = logging.getLogger(__name__)


@enum.unique
class SpatialType(enum.Enum):
    """The spatial type of the model - i.e. either plane wave or modal based."""

    PLANE = 0
    MODAL = 1
