class Question:

    ask= None
    answer=None


class Add(Question):
    def __init__(self, num1, num2):
        self.ask = '{} + {}'.format(num1, num2)
        self.answer= num1 + num2

       

# >>> from question import Add
# >>> x = Add(5, 9)
# >>> x.ask
# '5 + 9'
# >>> x.answer
# 14

# ######################################
# ==========>>فرقی نمیکنه با پایینی
class Add:
    def __init__(self, num1, num2):
        self.ask = '{} + {}'.format(num1, num2)
        self.answer= num1 + num2


# >>> from question import Add
# >>> x = Add(5, 9)
# >>> x.ask
# '5 + 9'
# >>> x.answer
# 14