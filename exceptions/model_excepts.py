from .base_except import Base_Exception

class NoPeriod(Exception):

    def __init__(self, *args, **kwargs):
        self.message = 'No hay un perido académico al cual asignar las clases. Favor de asignar uno.'
        super().__init__(self.message)
