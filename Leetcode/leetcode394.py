def decode_string(s: str) -> str:
    stack = [] # this is stack used to store decoded string

    for c in s:
        if c.isalnum() or c == '[':
            stack.append(c)
        elif c == "]": # at this point we have to prepare to decode string
            cur_str = ""
            # here to assemble the target string, for example 3[ab], we find "ab" and replicate it 3 times
            # so we meed 3 steps:
            #    Step 1: find the string to be replicated
            #    Step 2: assemble the number
            #    Step 3: put the replicated string into stack

            #   Step 1
            while stack[-1] != '[':  # this process innermost string
                cur_str = stack.pop(-1) + cur_str
            stack.pop(-1)  # pop '['

            #  Step 2
            counts = ''
            while stack and stack[-1].isdigit():
                counts = stack.pop(-1) + counts

            cur_str = cur_str * int(counts)

            # Step 3
            stack.extend(list(cur_str))

    return ''.join(stack)


if __name__ == '__main__':
    example = "3[abc]"

    print(decode_string(example))