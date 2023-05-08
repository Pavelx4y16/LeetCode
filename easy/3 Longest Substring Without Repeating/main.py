def get_substring(s):
    alphas = {}
    answer = left = 0

    for i, ch in enumerate(s):
        if ch in alphas and left <= alphas[ch]:
            left = alphas[ch] + 1
        else:
            answer = max(answer, i - left + 1)
        alphas[ch] = i

    return answer


def get_substring_1(s):
    alphas = [False] * 255
    answer = left = right = 0

    while right < len(s):
        x = ord(s[right])
        if alphas[x]:
            answer = max(answer, right - left)
            while s[left] != s[right]:
                alphas[ord(s[left])] = False
                left += 1
            if left != right:
                left += 1
        else:
            alphas[x] = True
        right += 1

    return max(answer, right - left)
