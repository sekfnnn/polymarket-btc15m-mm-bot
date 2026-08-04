from dataclasses import dataclass


@dataclass
class ValidationResult:
    allowed: bool
    reason: str = ""


class OrderPipeline:
    def __init__(self, validator=None, position_guard=None):
        self.validator = validator
        self.position_guard = position_guard

    def validate(self, order):
        if self.validator and not self.validator.validate(order):
            return ValidationResult(False, "validator_block")

        if self.position_guard and not self.position_guard.allow(order):
            return ValidationResult(False, "position_block")

        return ValidationResult(True, "ok")
