So the problem is to check if a sequence of brackets is properly balanced. The key points are that each opening bracket has a corresponding closing one of the same type, and they're properly nested. 

Hmm, the standard way to solve this kind of problem is using a stack data structure. Right, because when you encounter an opening bracket, you push it onto the stack. When you see a closing bracket, you check if the top of the stack has the corresponding opening bracket. If it does, pop the stack. If not, then it's unbalanced. Also, at the end, the stack should be empty.

Wait, but what about the different types of brackets? Like, for example, if the stack has '(', and the current is ')', then it's a match. Similarly for square and curly. So I need a mapping from closing brackets to their corresponding opening ones.

So maybe create a dictionary where the keys are the closing brackets, and the values are the opening ones. Like:

matching = {')': '(', ']': '[', '}': '{'}

Yes. So when I encounter a closing bracket, I check if the stack's top matches the corresponding opening bracket.

Let me outline the steps:

1. Read N from input. Then read the string of length N.
2. Initialize a stack (can use a list in Python).
3. Iterate through each character in the string:
   a. If it's an opening bracket (i.e., in the set {'(', '[', '{'}), push to stack.
   b. If it's a closing bracket (in {')', ']', '}'}), check if the stack is empty. If empty, return NO because there's nothing to match.
   c. Pop the top element from the stack and check if it matches the corresponding opening bracket using the matching dictionary. If not, return NO.
4. After processing all characters, check if the stack is empty. If not, there are unmatched opening brackets, so return NO. Otherwise, return YES.

Edge cases to consider:

- Empty string: should return YES. But according to the input constraints, N can be 1 to 10,000. Wait, the note says empty sequence is considered balanced. But the input format says N is the length. So if N is 0, but according to the problem statement, N is at least 1. Wait, the input format says the first line is N (1 ≤ N ≤ 10,000). So the input will have N ≥1. So no empty string case. Wait, but the note says empty is considered balanced. But according to the input constraints, N can be 1. So maybe the input can have an empty string only if N is 0, but according to the problem statement, N starts from 1. So perhaps the code doesn't need to handle that. But the note is part of the problem's conditions. Wait, the note says "Note: Empty sequence is considered balanced". But the input format says the second line is a string of N characters. So if N is 0, but the input constraints say N is at least 1. So maybe the code can ignore that, but according to the problem statement, perhaps the code should handle N=0. But according to the input format, the first line is N (1 ≤ N ≤ 10,000). So the input will have N ≥1. So the code can assume that the input string is of length N, which is at least 1. But the note says that empty is considered balanced. Hmm, perhaps the problem's note is just to clarify that even if the string is empty (N=0), but according to the input constraints, that's not possible. So maybe the code doesn't need to handle that.

Other edge cases: single bracket. For example, '(', then stack has one element. At the end, stack is not empty, so output NO. Correct.

Another case: '())'. Let's see. The first '(' is pushed. Then ')', which matches, stack becomes empty. Then ')', stack is empty, so return NO. Correct.

So the algorithm seems solid.

Now, code steps:

Read N. Then read the string. Then process each character.

In Python:

n = int(input())
s = input().strip()

stack = []
matching = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in ['(', '[', '{']:
        stack.append(char)
    else:
        if not stack:
            print("NO")
            exit()
        top = stack.pop()
        if matching[char] != top:
            print("NO")
            exit()

if not stack:
    print("YES")
else:
    print("NO")

Wait, but what about the case where the input is something like "([)]"? Let's see. The example input 2 is {[}], which is output NO.

In the code, let's process "([)]".

First character '(', pushed. Stack: ['(']
Second '[', pushed. Stack: ['(', '[']
Third ')', which is a closing. Pop the top, which is '[', check matching for ')'. The matching for ')' is '(', which is not equal to '[', so returns NO. Correct.

So the code handles that.

Another example: "(()". The code processes:

'(', pushed.

'(', pushed.

')', pop '(', which matches. Stack now empty.

Then end of string. Stack is empty, so output YES. Wait, no. Wait, the input is "(()", which is length 3. The code would process:

First '(', stack becomes ['(']

Second '(', stack becomes ['(', '(']

Third ')', pop '(', which matches. Stack becomes empty.

At the end, stack is empty. So output YES. But according to the problem's definition, the brackets are balanced. Let's see:

The sequence is ( ( ), which is ( ( ) ). Wait, no. The sequence is ( ( ) → that's ( ( ) ), which is invalid because the second ( is closed by the ), leaving the first ( unclosed. Wait, no. Wait, the sequence is:

Index 0: '(' → stack ['(']

Index 1: '(' → stack ['(', '(']

Index 2: ')' → pop '(', which matches. Stack is now ['(']

At the end, stack is not empty. So code would output NO. Wait, but in the code as written, after processing all characters, check if stack is empty. So in the example "(()", after processing all three characters, the stack has one '(' left. So code outputs NO. Which is correct.

Wait, let's re-examine the code:

After the loop:

if not stack:
    print("YES")
else:
    print("NO")

Yes. So in the example "(()", the stack after processing all characters is ['('], so code outputs NO. Correct.

Another example: "(()", which is 3 characters. The code would process:

First '(', stack ['(']

Second '(', stack ['(', '(']

Third ')', pop '(', stack becomes ['(']

Loop ends. Stack is not empty → output NO. Correct.

So the code works.

What about the example input 1: {[()]}

Processing:

Characters: { [ ( ) ] }

Let's see:

First '{' → stack ['{']

Second '[' → stack ['{', '[']

Third '(' → stack ['{', '[', '(']

Fourth ')' → pop '(', which matches. Stack becomes ['{', '[']

Fifth ']' → pop '[', which matches. Stack becomes ['{']

Sixth '}' → pop '{', which matches. Stack is empty. So output YES. Correct.

Another example input 2: {[}]

Processing:

'{' → stack ['{']

'[' → stack ['{', '[']

'}' → pop '[', but matching for '}' is '{', which is not equal to '[', so code returns NO. Correct.

So the code works.

Now, what about the case where the input is a single bracket, like '('? The code will process it, push to stack. Then loop ends. Stack is not empty → output NO. Correct.

Another case: ')]', which is length 3. Let's see:

First ')', but stack is empty → output NO. Correct.

So the code seems to handle all cases.

Now, code in Python:

Read N, then the string. Then process.

But in Python, input().strip() may not be necessary, but better to use it to remove any leading/trailing whitespace. But according to the problem statement, the input is as per the format. So the code should be:

n = int(input())
s = input().strip()

stack = []
matching = {')': '(', ']': '[', '}': '{'}

for c in s:
    if c in '([{':
        stack.append(c)
    else:
        if not stack:
            print("NO")
            exit()
        if stack.pop() != matching[c]:
            print("NO")
            exit()

print("YES" if not stack else "NO")

Wait, but in the code, after popping, compare to matching[c]. So for example, when c is ')', matching[c] is '(', so stack.pop() should equal '('