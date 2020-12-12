"""
--- Part Two ---

To completely determine whether you have enough adapters, you'll need to
figure out how many
different ways they can be arranged. Every arrangement needs to connect the
charging outlet to
your device. The previous rules about when adapters can successfully connect
still apply.

The first example above (the one that starts with 16, 10, 15) supports the
following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

(The charging outlet and your device's built-in adapter are shown in
parentheses.) Given the
adapters from the first example, the total number of arrangements that
connect the charging
outlet to your device is 8.

The second example above (the one that starts with 28, 33, 18) has many
arrangements. Here are a
few:

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)

In total, this set of adapters can connect the charging outlet to your device
in 19208 distinct
arrangements.

You glance back down at your bag and try to remember why you brought so many
adapters; there must
be more than a trillion valid ways to arrange them! Surely, there must be an
efficient way to
count the arrangements.

What is the total number of distinct ways you can arrange the adapters to
connect the charging
outlet to your device?
"""
import math
from itertools import permutations


def determine_permutation_length(source_adapters):
    """ As we must bridge min 1 and max 3 jolts per step, we can determine
    the minimum and the
    maximum length of the chain of adapters required.
    E.g. if max(adapter_joltage) = 9, the device requires an input joltage of
    12.
    Hence, we require at least (minimum) of 3 adapters (3, 6, 9 ) to bridge
    the input 0 to the output of 12. When the max joltage is 8, this does not
    change: we still need 3, so we need the ceil (max/3).
    """
    min_adapters = math.ceil(max(source_adapters) / 3)
    max_adapters = len(source_adapters)
    return min_adapters, max_adapters


def validate_adapter_sequence(max_joltage, adapter_sequence):
    # Valid sequence must end with the max_adapter and start with either 1,
    # 2 or 3. Furthermore, all neighbouring adapters must be with 1-3 jolts.
    return adapter_sequence[0] in (1, 2, 3) and \
           adapter_sequence[-1] == max_joltage and \
           all(1 <= adapter_sequence[i] - adapter_sequence[i - 1] <= 3 for i
               in range(1, len(adapter_sequence)))


def count_valid_permutations(adapter_sequence, permutation_length):
    max_adapter_joltage = max(adapter_sequence)
    sorted_adapter_sequence = sorted(adapter_sequence)
    permutation_generator = permutations(sorted_adapter_sequence,
                                         permutation_length)
    valid_permutations = 0
    # iterate over generator for early exit if first step exceeds maximum (3)
    for perm in permutation_generator:
        if perm[0] > 3:
            break
        if validate_adapter_sequence(max_joltage=max_adapter_joltage,
                                     adapter_sequence=perm):
            valid_permutations += 1
    print(f"Found {valid_permutations} of length {permutation_length}")
    return valid_permutations


def count_all_permutations(adapter_sequence):
    min_perm, max_perm = determine_permutation_length(adapter_sequence)
    perm_length = min_perm
    total_perms = 0
    while perm_length <= max_perm:
        total_perms += count_valid_permutations(adapter_sequence, perm_length)
        perm_length += 1
    return total_perms
