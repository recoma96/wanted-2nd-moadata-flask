from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Optional, List


class Validator(metaclass=ABCMeta):
    """
    The Validator Interface (Superclass)
    """

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        """
        Check if data is validator
        :returns True if data is valid
        :return False if data is not valid
        """
        pass


class AutomaticValidator(Validator):
    """
    AutomaticValidator is the child class from Validator that is Validator Interface.
    just input "Data Type" and "Validate Logic" when construct this class
    instead of overriting "__call__" function
    """


    """
    Input data must be passed by this validator logic
    Recomented about function which return type is bool or has Exception
    """
    validate_logic: Callable

    def __init__(self, validate_logic: Callable):
        """
        set data_type and validate_logic
        :param validate_logic:
        """

        if not isinstance(validate_logic, Callable):
            raise TypeError("logic must be Callable Function")
        self.validate_logic = validate_logic

    def __call__(self, *args, **kwargs) -> (bool, Optional[Exception]):
        """
        :param data: the data for check validator
        :return: (True, None) if data is valid, then Exception is None
        :return: (False, Exception) if data is not valid, then Exception is returned
        """
        try:
            # run validator logic for validator data
            is_valid = self.validate_logic(**kwargs) if kwargs else self.validate_logic(*args)
        except Exception as e:
            # if is called exception Then return False
            return False, e

        if isinstance(is_valid, bool) and not is_valid:
            return False, ValueError("Validate Failed")
        return True, None
