from abc import ABC, abstractmethod


class StorageClient(ABC):
    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def write(self, data):
        pass
