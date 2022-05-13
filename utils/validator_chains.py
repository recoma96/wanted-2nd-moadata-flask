from libs.validate.validator_chain import ValidatorChain
from libs.validate.validator import AutomaticValidator
from typing import Dict
from utils.validator_logics.job_validator_logics import *


def get_job_validator_chain() -> ValidatorChain:

    validator_chain = ValidatorChain()

    validator_chain.add_validator(AutomaticValidator(data_type=dict,
                                                     validate_logic=validate_job_list),
                                  lambda job: job['task_list'])
    validator_chain.add_validator(AutomaticValidator(data_type=dict,
                                                     validate_logic=validate_job_properties),
                                  lambda job: job['property'])

    return validator_chain