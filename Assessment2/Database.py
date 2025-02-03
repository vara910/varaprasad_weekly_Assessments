from abc import ABC,abstractmethod
class DataBS(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQL(DataBS):
    def update(self):
        return "updates has been done on sql database"
    def insert(self):
        return "insertion is done on sql"
    def delete(self):
        return "deletion has been done on sql database"
class NOSQL(DataBS):
    def update(self):
        return "updates has been done on nosql database"
    def insert(self):
        return "insertion is done on nosql"
    def delete(self):
        return "deletion has been done on nosql database"
sql=SQL()
print(sql.update())
print(sql.delete())
print(sql.insert())
nsql=NOSQL()
print(nsql.update())
print(nsql.delete())
print(nsql.insert())