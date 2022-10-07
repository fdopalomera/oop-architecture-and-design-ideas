from abc import ABC, abstractmethod


class Database(ABC):
    """Blueprint for the class in charge of connecting and interact with a database"""
    @abstractmethod
    def get_data(self, query: str) -> dict[str, str]:
        """Run a query to the database and return the results in a dictionary"""
        pass
