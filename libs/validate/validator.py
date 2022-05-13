from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Optional


class Validator(metaclass=ABCMeta):
    """
    The Validator Interface (Superclass)
    """

    @abstractmethod
    def __call__(self, data: Any) -> bool:
        """
        Check if data is validate
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

    """ Input data type must be "data_type" """
    data_type: type

    """
    Input data must be passed by this validate logic
    Recomented about function which return type is bool or has Exception
    """
    validate_logic: Callable

    def __init__(self, data_type: type, validate_logic: Callable):
        """
        set data_type and validate_logic
        :param data_type:
        :param validate_logic:
        """
        if not isinstance(data_type, type):
            raise TypeError("data_type must be type class")
        self.data_type = data_type

        if not isinstance(validate_logic, Callable):
            raise TypeError("logic must be Callable Function")
        self.validate_logic = validate_logic

    def __call__(self, data: Any) -> (bool, Optional[Exception]):
        """
        :param data: the data for check validate
        :return: (True, None) if data is valid, then Exception is None
        :return: (False, Exception) if data is not valid, then Exception is returned
        """

        # check type of data
        if not isinstance(data, self.data_type):
            return False, Exception("Data Type Not Matched")
        try:
            # run validate logic for validate data
            is_valid = self.validate_logic(data)
        except Exception as e:
            # if is called exception Then return False
            return False, e

        if isinstance(is_valid, bool) and not is_valid:
            return False, ValueError("Validate Failed")
        return True, None
