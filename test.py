class Stack(object):
    def __init__(self):
        self.array = []
        self.count=0
    def l_push(self, data):
        self.count=self.count+1
        self.array.insert(0,data)

    def l_pop(self):
        if self.count == 0:
            print('Left Stack is empty')
        else:
            self.array.pop(0)
            self.count = self.count - 1

    def r_push(self, data):
        self.array.append(data)

    def r_pop(self):
        if len(self.array)-self.count== 0:
            print('Right Stack is empty')
        else:
            self.array.pop()

    def show(self):
        if self.count == 0:
            print('Left Stack is empty')
        else:
            print('Left Stack:', self.array[0:self.count])
        if len(self.array)-self.count== 0:
            print('Right Stack is empty')
        else:
            print('Right Stack:', self.array[self.count:])


import unittest
class TestStack(unittest.TestCase):
    stack=Stack()
    def testLstack(self):
        print("Left Stack")
        self.stack.l_push(1)
        self.stack.l_pop()
        self.stack.l_pop()
        self.stack.l_push(1)
        self.stack.l_push(2)

    def testRstack(self):
        print("Right Stack")
        self.stack.r_push(1)
        self.stack.r_pop()
        self.stack.r_pop()
        self.stack.r_push(1)
        self.stack.r_push(2)
    def testShow(self):
        print("Stack Show")
        self.stack.show()

def suite():
  suite = unittest.TestSuite()
  suite.addTest(TestStack("testLstack"))
  suite.addTest(TestStack("testRstack"))
  suite.addTest(TestStack("testShow"))
  return suite
if __name__ == "__main__":
  unittest.main(defaultTest = 'suite')
# .Left Stack
# Left Stack is empty
# .Right Stack
# Right Stack is empty
# .Stack Show
# Left Stack: [2, 1]
# Right Stack: [1, 2]
