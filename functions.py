import Node
import json


def initialize():
    a1 = Node.Answer("answer 1")
    a2 = Node.Answer("answer 2")
    a3 = Node.Answer("answer 3")
    a4 = Node.Answer("answer 4")
    a5 = Node.Answer("answer 5")
    a6 = Node.Answer("answer 6")
    a7 = Node.Answer("answer 7")
    a8 = Node.Answer("answer 8")
    q4 = Node.Question('question4', a1, a2)
    q5 = Node.Question('question 5', a3, a4)
    q6 = Node.Question('question 6', a5, a6)
    q7 = Node.Question('question 7', a7, a8)
    q2 = Node.Question('question 2', q4, q5)
    q3 = Node.Question('question 3', q6, q7)
    q1 = Node.Question('question 1', q2, q3)
    return q1


def class_to_dict(root):
    dictionary = {}
    if type(root) == Node.Answer:
        dictionary['answer'] = root.answer
        return dictionary
    dictionary['question'] = root.question
    dictionary['left'] = class_to_dict(root.left)
    dictionary['right'] = class_to_dict(root.right)
    return dictionary


def dict_to_class(dictionary):
    if 'answer' in dictionary:
        answer = Node.Answer(dictionary['answer'])
        return answer
    question = Node.Question(dictionary['question'])
    question.left = dict_to_class(dictionary['left'])
    question.right = dict_to_class(dictionary['right'])
    return question


def print_tree(root):
    if type(root) == Node.Answer:
        print(root.answer)
        return
    print(root.question)
    print_tree(root.left)
    print_tree(root.right)


def write(val, path):
    with open(path, 'w') as file:
        json.dump(val, file, indent=4)


def ask_question(question):
    while True:
        reply = input(question)
        if reply == 'да':
            return True
        elif reply == 'нет':
            return False
        else:
            print('Повторите ввод')


def open_file(path):
    with open(path, 'r') as file:
        val = json.load(file)
        print(val)
        return val
