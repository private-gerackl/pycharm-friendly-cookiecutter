from abc import abstractmethod, ABC


class BaseSynthesizer(ABC):

    @abstractmethod
    def pfc(self) -> None:
        raise NotImplementedError