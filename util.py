class EmptyEntryError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class EmptyWordlistNameError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CrosswordGenerationError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidWordlistNameError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
