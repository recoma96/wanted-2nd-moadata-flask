from libs.validator import AutomaticValidator, ValidatorChain
from utils.validator_logics.job_validator_logics import *


def get_job_validator_chain() -> ValidatorChain:
    """
    Job Data 유효성을 측정하기 위한 ValidatorChain
    """
    validator_chain = ValidatorChain()
    validator_chain.add_validator(
        AutomaticValidator(data_type=dict, validate_logic=validate_job_list),
        lambda job: job['task_list']
    )
    validator_chain.add_validator(
        AutomaticValidator(data_type=dict, validate_logic=validate_job_properties),
        lambda job: job['property']
    )
    return validator_chain