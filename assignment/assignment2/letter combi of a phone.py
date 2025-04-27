def letterCombinations(digits):
    if not digits:
        return []

    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    combinations = []

    def backtrack(combination, start):
        if len(combination) == len(digits):
            combinations.append(''.join(combination))
            return

        for char in digit_map[digits[start]]:
            combination.append(char)
            backtrack(combination, start + 1)
            combination.pop()

    backtrack([], 0)
    return combinations

print(letterCombinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(letterCombinations(""))  # Output: []
print(letterCombinations("2"))  # Output: ['a', 'b', 'c']