# largest rectangle in histogram


def largest_rectangle(heights):

    if not heights:
        return 0

    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            max_area = max(max_area, heights[stack.pop(-1)] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] != -1:
        max_area = max(max_area, heights[stack.pop(-1)] * (len(heights) - stack[-1] - 1))

    return max_area


print(largest_rectangle([2,1,5,6,2,3]))