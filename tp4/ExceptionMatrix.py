class ExceptionMatrix(Exception):
    pass


class NotNegative(ExceptionMatrix):
    def __init__(self, var_name=None, val=None, message="cannot be negative."):
        self.var_name = var_name
        self.val = val
        self.message = message
        super(NotNegative, self).__init__(message)

    def __str__(self):
        match (self.var_name, self.val):
            case (var, val):
                return f"\"{var} = {val}\" {self.message}"
            case (var, None):
                return f"\"{var}\" {self.message}"
            case (None, None):
                return self.message


class OutOfRange(ExceptionMatrix):
    def __init__(self, min_val, max_value, var_name=None, val=None, message="not in range[{}, {}["):
        self.var_name = var_name
        self.val = val
        self.message = message.format(min_val, max_value)
        super(OutOfRange, self).__init__(message)

    def __str__(self):
        match (self.var_name, self.val):
            case (var, val):
                return f"\"{var} = {val}\" {self.message}"
            case (var, None):
                return f"\"{var}\" {self.message}"
            case (None, None):
                return self.message


class NoStep(ExceptionMatrix):
    def __init__(self):
        super(NoStep, self).__init__("matrix cannot use step (usage mat[i:j])")


class NotMatchSize(ExceptionMatrix):
    def __init__(self, arr: [int], attend: int):
        """
        contruct exception if len(arr) != attend
        :param arr: tableau utilisé
        :param attend: longuer attendu
        """
        super(NotMatchSize, self).__init__(f"lentgh array need to be {attend} and is {len(arr)}")


class NotCompatible(ExceptionMatrix):
    pass


class NotSquared(ExceptionMatrix):
    def __init__(self, mat: "Matrix"):
        super(NotSquared, self).__init__(f"matrix is not squared {mat.lines=} {mat.colums=}")
