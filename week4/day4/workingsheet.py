magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


def show_magicians(args):
    for arg in args:
        print(arg)


show_magicians(magician_names)

# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.


def make_great(args):
    for arg in args:
        index_of_aargs = args.index(arg)
        args.pop(index_of_aargs)
        args.insert(index_of_aargs, f"{arg} the Great")


make_great(magician_names)
show_magicians(magician_names)
