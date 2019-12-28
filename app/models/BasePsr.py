from abc import abstractmethod, ABC
class BasePSR(ABC):

    @abstractmethod
    def calculate_deal(self,amout):pass