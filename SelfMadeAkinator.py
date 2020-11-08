import Node
import functions


class SelfMadeAkinator:

    def __init__(self, root):
        self.root = root

    def run(self):
        while type(self.root) == Node.Question:

            if functions.ask_question(self.root.question + ": "):
                self.root = self.root.right
            else:
                self.root = self.root.left
            # print(type(self.root))
            if type(self.root) == Node.Question:
                if not functions.ask_question("Продолжить?: "):
                    functions.write(functions.class_to_dict(self.root), 'file/questions')
                    break
        else:
            print(self.root.answer)
            d = functions.open_file('file/tree')
            q = functions.dict_to_class(d)
            functions.write(functions.class_to_dict(q), 'file/questions')
