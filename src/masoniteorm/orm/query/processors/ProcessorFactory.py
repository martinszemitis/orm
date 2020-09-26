from .SQLitePostProcessor import SQLitePostProcessor
from .MySQLPostProcessor import MySQLPostProcessor
from .PostgresPostProcessor import PostgresPostProcessor


class ProcessorFactory:

    processors = {
        "sqlite": SQLitePostProcessor,
        "mysql": MySQLPostProcessor,
        "postgres": PostgresPostProcessor,
    }

    def make(self, processor):
        return self.processors[processor]
