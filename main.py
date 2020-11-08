import SelfMadeAkinator
import functions

if __name__ == "__main__":
    d = functions.open_file('file/questions')
    q = functions.dict_to_class(d)
    akinator = SelfMadeAkinator.SelfMadeAkinator(q)
    akinator.run()
    # qestions = functions.initialize()
    # functions.write(functions.class_to_dict(qestions), 'file/tree')

    # dict = SelfMadeAkinator.ClassToDict(qestions)
    # write(dict)
    # d = open_file()
    # q = SelfMadeAkinator.dict_to_class(d)
    # SelfMadeAkinator.print_tree(q)
