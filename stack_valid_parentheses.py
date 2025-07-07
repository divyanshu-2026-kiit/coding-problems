# valid parentheses , stack based approach
class Stack:
    def __init__(self):
        self.stack = []

    def isValid(self, s : str) -> bool:
        for bracket in s:
            if bracket == "(" or bracket =="{" or bracket == "[":
                self.stack.append(bracket)
            else:
                if len(self.stack) == 0:
                    return"stack is empty"
                character = self.stack.pop()
                if((bracket == ")" and character == "(")
                or (bracket == "}" and character == "{")
                or (bracket == "]" and character == "[")
                ):
                    continue
                else:
                    return False
        return len(self.stack) == 0

stack1 = Stack()
parentheses = "{([])}"
result = stack1.isValid(parentheses)
print(result)




    
                  