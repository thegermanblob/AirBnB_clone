#!/usr/bin/python3
'''Command line interpreter for AirBnB console'''

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''This class defines the actions the user can do inside of the console'''
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        print()
        return True

    def do_create(self, line):
        '''Creates a new instance'''

        if len(line) == 0:
            print("** class name missing **")

        elif line in storage.classes:
            new = storage.classes[line]()
            print(new.id)
            storage.new(new)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''Print string representation of instance'''
        args = line.split()
        objs = storage.all()
        key = args[0] + "." + args[1]

        if len(line) == 0:
            print("** class name missing **")

        elif args[0] in storage.classes:
            if len(args) != 2:
                print("** instance id missing **")
            elif key not in objs:
                print("** no instance found **")
            else:
                print(storage.all()[key])

        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        objs = storage.all()

        if len(line) == 0:
            print("** class name missing **")

        elif args[0] in storage.classes:
            key = args[0] + "." + args[1]
            if len(args) != 2:
                print("** instance id missing **")
            elif key not in objs:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        '''Prints all string representation of all instances'''
        args = line.split()
        objs = storage.all()

        if len(line) == 0:
            for key in objs.keys():
                print(objs[key])

        elif args[0] in storage.classes:
            for key, value in objs.items():
                if key[0: key.index('.')] == args[0]:
                    print(value)

    def do_update(self, line):
        '''Updates an instance based on the class name and id'''
        args = line.split()
        objs = storage.all()

        try:
            key = args[0] + "." + args[1]
        except:
            pass
        if len(line) == 0:
            print("** class name missing **")

        elif args[0] in storage.classes:
            if len(args) < 2:
                print("** instance id missing **")
            elif key not in objs:
                print("** no instance found **")
            elif len(args) < 3:
                print("** atttribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                for clas, value in objs.items():
                    if args[1] == value.id:
                        setattr(value, args[2], args[3])
                        storage.save()

        else:
            print("** class doesn't exist **")

    def emptyline(self):
        '''Overrides default emptyline method'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
