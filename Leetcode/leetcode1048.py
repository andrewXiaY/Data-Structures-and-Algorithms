"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it
equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2,
word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.


Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5

"""

"""
思路：其中最有意思的就是将一个word中任意一个位置删除掉得到deleted_word，然后判断deleted_word是否在原来的words中，
如果有的话相当于deleted_word是word的predecessor, 我们只需要计算出以deleted_word结尾的subsequence长度，并加1即可
"""


def solve(words):
    words = sorted(words, key=lambda x: len(x))
    counts = {w: 1 for w in words}

    longest = 1
    for word in words:
        for i in range(len(word)):
            deleted_word = word[:i] + word[i+1:]
            if deleted_word in words:
                counts[word] = max(counts[word], counts[deleted_word] + 1)
                longest = max(longest, counts[word])

    return longest


if __name__ == '__main__':
    assert solve(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert solve(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5