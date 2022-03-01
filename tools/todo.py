class ExceptionTODO(Exception):
    def __init__(self, n: None | int):
        message = f"A implémenter"
        if n is not None:
            message += f" (a peut près {n} instructions)."
        super(ExceptionTODO, self).__init__(message)


def TODO(n: None | int = 1):
    raise ExceptionTODO(n)
