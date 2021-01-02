

# Using the sliding window concept, keep record of the last appearance of current char in a map.
# The starting point of slide window should be the index of the first char of current
# unrepeated substring and we use a variable to store current maximum length, every time we
# update the slide window, we update the maximum length of unrepeated substring
def length_longest_substring(s: str):
    char_pos = {}
    window_start = 0
    ans = 0

    for idx, c in enumerate(s):
        if c in char_pos:
            window_start = max(window_start, char_pos[c] + 1)
        ans = max(ans, idx - window_start + 1)
        char_pos[c] = idx

    return ans


if __name__ == '__main__':
    s = "abcabcbb"

    print(length_longest_substring(s))