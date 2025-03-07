def check_guess(guess, target_word):
    result = []
    for i, char in enumerate(guess):
        if char == target_word[i]:
            result.append({'value': char, 'result': 'correct'})
        elif char in target_word:
            result.append({'value': char, 'result': 'present'})
        else:
            result.append({'value': char, 'result': 'absent'})
    return result
