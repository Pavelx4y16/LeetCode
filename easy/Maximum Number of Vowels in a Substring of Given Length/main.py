def get_max_number(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_max = sum([1 for ch in s[:k] if ch in vowels])
    current = current_max

    for i in range(k, len(s)):
        current += (s[i] in vowels) - (s[i - k] in vowels)
        current_max = max(current, current_max)

    return current_max
