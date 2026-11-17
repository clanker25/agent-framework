# Copyright (c) Microsoft. All rights reserved.

from enum import IntEnum


class FeatureIndex(IntEnum):
    """Orchestration-owned feature-usage indexes."""

    ORCHESTRATION_SEQUENTIAL = 32
    ORCHESTRATION_CONCURRENT = 33
    ORCHESTRATION_GROUP_CHAT = 33
    ORCHESTRATION_MAGENTIC = 36
    ORCHESTRATION_HANDOFF = 36
