"""
Infix to postfix converter

by Uriel de Oliveira Alves 
   https://github.com/uriel-oa
   02/10/17
"""

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items) -1]
    def size(self):
        return len(self.items)

def precedence(item, stackTop):
    if ((item == '*') or (item == '/')) and ((stackTop == '+') or (stackTop == '-') or (stackTop == '*') or (stackTop == '/')):
        return True
    elif ((item == '+') or (item == '-')) and ((stackTop == '+') or (stackTop == '-')):
        return True
    elif (item == stackTop):
        return True
    else:
        return False


def infixToPostfix(infix):
    infix = infix.lower()
    _stack = Stack()
    _input = []
    _output = []
    postfix = ''

    #convert list to string
    for i in infix:
        _input.append(i)

    while (len(_input) > 0):

        # step1
        item = str(_input.pop(0))

        # step2
        if (item >= 'a') and (item <= 'z'):
            _output.append(item)

            # step3
        elif (item == '('):
            _stack.push(item)

        # step5
        elif (item == ')'):
            while (_stack.size() > 0):

                if (_stack.peek() == '('):
                    _stack.pop()
                    break

                else:
                    _output.append(str(_stack.pop()))

        # step4
        else:
            flag = True
            while (flag):
                if not (_stack.isEmpty()):
                    # 4.1
                    if (_stack.peek() == '('):
                        _stack.push(item)
                        flag = False

                    # 4.2
                    elif (precedence(item, _stack.peek())):
                        _stack.push(item)
                        flag = False

                    # 4.3 ABC*+DE+F*+
                    else:
                        while not (_stack.isEmpty()):
                            _output.append(str(_stack.pop()))
                            flag = True
                else:
                    _stack.push(item)
                    flag = False


    # step7
    while (_stack.size() > 0):
        _output.append(str(_stack.pop()))

    #convert list to string
    for i in _output:
        postfix += str(i)
    postfix = postfix.upper()
    
    return postfix


def main():
    # Example:
    infix = 'A+B*C+(D+E)*F'
    print("Infix: ", infix)
    print("Postfix: ", infixToPostfix(infix))

if __name__ == "__main__":
    main()
