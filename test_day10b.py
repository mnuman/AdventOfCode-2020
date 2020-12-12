import day10b
import utils

test_adapters = [1, 2, 3, 4, 5, 6, 7, 8, 9]
TEST_JOLTAGES = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_determine_permutation_length():
    assert day10b.determine_permutation_length(test_adapters) == (3, 9)


def test_validate_adapter_sequence_full_sequence():
    assert day10b.validate_adapter_sequence(
        max_joltage=9, adapter_sequence=test_adapters)


def test_validate_adapter_sequence_invalid_max():
    assert not day10b.validate_adapter_sequence(
        max_joltage=10, adapter_sequence=test_adapters)


def test_validate_adapter_sequence_invalid_start():
    assert not day10b.validate_adapter_sequence(
        max_joltage=9, adapter_sequence=test_adapters[3:])


def test_validate_adapter_sequence_invalid_end():
    assert not day10b.validate_adapter_sequence(
        max_joltage=9, adapter_sequence=test_adapters[:-1])


def test_validate_adapter_sequence_invalid_sequence():
    assert not day10b.validate_adapter_sequence(
        max_joltage=9, adapter_sequence=[0, 4, 5, 6, 7, 8, 9])


def test_count_valid_permutations_full_length():
    assert day10b.count_valid_permutations(test_adapters, 9) == 1


def test_count_valid_permutations_min_length():
    assert day10b.count_valid_permutations(test_adapters, 3) == 1


def test_count_valid_permutations_some_length():
    """ last element MUST be 9, first must be 1, 2 or 3
        (1, 3, 6, 9) (1, 4, 6, 9) (1, 4, 7, 9) (2, 3, 6, 9) (2, 4, 6, 9)
        (2, 4, 7, 9) (2, 5, 6, 9) (2, 5, 7, 9) (2, 5, 8, 9) (3, 4, 6, 9)
        (3, 4, 7, 9) (3, 5, 6, 9) (3, 5, 7, 9) (3, 5, 8, 9) (3, 6, 7, 9)
        (3, 6, 8, 9)
    """
    assert day10b.count_valid_permutations(test_adapters, 4) == 16


def test_count_all_permutations():
    assert day10b.count_all_permutations(TEST_JOLTAGES) == 8


def test_scenario():
    mylist = utils.read_file("data/test_day10.txt", convert=int)
    assert day10b.count_all_permutations(mylist) == 19208
