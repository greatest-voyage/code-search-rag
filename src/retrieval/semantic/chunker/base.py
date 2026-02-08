from abc import ABC, abstractmethod

class Chunker(ABC):
    @abstractmethod
    def chunk_repo(self, path: str):
        pass