from abc import ABCMeta
from typing import Any, List, Callable, Tuple, Optional
from libs.validate.validator import AutomaticValidator


class ValidatorChain(metaclass=ABCMeta):
    """
    Multiple Validators Machine
    Data can be check many validate by using this class only one
    """

    """
    List of validator
    List has Tuples that first is AutomaticValidator and other one is function
    these functions are pre-process function for pre-processing input data
    because some validator could need different type of input data each other
    so, pre-process function can make input data to fit input type of validator logic
    """
    validators: List[Tuple[AutomaticValidator, Callable]]

    def __init__(self):
        self.validators = []

    def add_validator(self,
                      validator: AutomaticValidator,
                      pre_procssor: Optional[Callable] = None):
        """
        :param validator:       Validate Class
        :param pre_procssor:    pre-processor function, None if not used function
        :return: id valif of validator
        """
        self.validators.append((validator, pre_procssor))
        return len(self.validators)

    def __call__(self, data: Any) -> (bool, Optional[Exception]):
        for validator, pre_processor in self.validators:
            pre_processed_data = data if not pre_processor else pre_processor(data)
            is_valid, err = validator(pre_processed_data)
            if not is_valid:
                return False, err
        return True, None

