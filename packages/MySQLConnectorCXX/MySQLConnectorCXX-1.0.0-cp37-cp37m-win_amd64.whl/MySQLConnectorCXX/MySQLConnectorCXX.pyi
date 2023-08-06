from typing import overload, Any


class Result:
    def getData(self) -> dict: ...


class Connection:
    def execute(self, sql: str) -> Result: ...

    def executePreparment(self, sql: str, params: Any = ...) -> Result: ...

    def release(self) -> bool: ...

    def setAutoCommit(self, autoCommit: bool): ...

    def setSchema(self, schema: str) -> bool: ...
    """
        This method can set schema (database) to this connection. It is equal to use "use" SQL.
        Attention, the change of schema is only useful during this connection is alive. When the connection is released, 
        the schema will change to the default. If you want to change the schema forever to all connections in the pool, 
        please use setSchema method of ConnectionPool class.
    """


class ConnectionPool:
    @overload
    def __init__(self, option: dict): ...

    @overload
    def __init__(self, url: str, user: str, password: str): ...

    @overload
    def __init__(self, host: str, username: str, password: str, port: int, database: str, autocommit: bool,
                 max_pool_size: int): ...

    def init(self): ...

    def getConnection(self) -> Connection: ...
