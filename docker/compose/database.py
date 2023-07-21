from netkiller.docker import *
from compose.service.mysql import *

database = Composes("database")
database.version("3.9")
database.services(mysql)
