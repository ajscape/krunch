from abc import ABC, abstractmethod

from task import TaskType


class ComputeClient(ABC):
    def __init__(self, storage_client):
        self._storage = storage_client

    @abstractmethod
    def runtask(self, task_type: TaskType, input):
        pass