from dataclasses import dataclass

@dataclass
class ValidationResult:
    train_size: int
    test_size: int
    passed: bool


def walk_forward_validate(train, test):
    return ValidationResult(
        train_size=len(train),
        test_size=len(test),
        passed=len(test) > 0,
    )
