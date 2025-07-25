from marsRover.Spatial import Spatial


from abc import ABC, abstractmethod


class Moveable(ABC):
    @abstractmethod
    def Move(cls):pass
    @abstractmethod
    def Left(cls):pass
    @abstractmethod
    def Right(cls):pass
    @abstractmethod
    def LandToPlateau(clas, spatial: 'Spatial'):pass