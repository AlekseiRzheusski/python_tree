class Question:
    def __init__(self, question, left=None, right=None):
        self.__question = question
        self.left = left
        self.right = right

    @property
    def question(self):
        return self.__question


class Answer:
    def __init__(self, answer):
        self.__answer = answer

    @property
    def answer(self):
        return self.__answer
