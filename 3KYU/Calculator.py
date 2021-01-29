import operator
import re

class Calculator(object):
    def op(self,op,num2,num1):
        operators={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        return operators[op]((num1), (num2))

    def clearing_fin_stack(self, stack_num, stack_op):
        while(len(stack_num)!= 1):
            stack_num.insert(0,self.op(stack_op.pop(0), stack_num.pop(1), stack_num.pop(0)))
        return stack_num[0]

    def check_type(self, symb, stack_num):
        if symb.isdigit():
            stack_num.append(int(symb))
        else:
            stack_num.append(float(symb))

    def calculate_expression_parentheses(self,stack_num,stack_op):
        while stack_op[-1] != '(':
            stack_num.append(self.op(stack_op.pop(), stack_num.pop(), stack_num.pop()))
        stack_op.pop()  

    def evaluate(self, string):
        stack_num = []
        stack_op = []
        self.priorities = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, '(' : 3, ')' : 3}
        self.symbols= [symb for symb in string.split()]
        p = re.compile('\d+(\.\d+)?')
        for symb in self.symbols:
            if p.match(symb):
                self.check_type(symb,stack_num)
            elif len(stack_op) == 0:
                stack_op.append(symb)
            elif symb == ')':
                if stack_op[-1] == ')':
                    stack_op.pop()
                else:
                    self.calculate_expression_parentheses(stack_num,stack_op)
            elif self.priorities[symb] > self.priorities[stack_op[-1]] or symb == '(':
                stack_op.append(symb)
            elif stack_op[-1] != '(': 
                stack_num.append(self.op(stack_op.pop(), stack_num.pop(), stack_num.pop()))
                stack_op.append(symb)
            else: 
                stack_op.append(symb)
        return self.clearing_fin_stack(stack_num,stack_op)