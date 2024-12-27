class EmptyEntryError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CrosswordGenerationError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
