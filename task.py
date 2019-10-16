from abc import ABC
from enum import Enum


class TaskType(Enum):
    split = 1
    map = 2
    reduce = 2
    combine = 3