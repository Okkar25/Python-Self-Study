import argparse

# create thr parser
parser = argparse.ArgumentParser(description="A simple argument parser")

# Add arguments
parser.add_argument("name", help="The user's name") # Positional argument
parser.add_argument("--age", type=int, help="The user's age") # optional argument

# Parse arguments
args = parser.parse_args()

print(f"Hello, {args.name}!")

if args.age:
    print(f"You are {args.age} years old.")

# python 10_command_line.py Okkar --age 23

import argparse

parser = argparse.ArgumentParser(description="Process some integers")

parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)

parser.add_argument(
    "--sum", dest="accumulate", action="store_const", const=sum, default=max
)

args = parser.parse_args()
print(args.accumulate(args.integers))  # sum([10, 20, 30])

# print(sum([10,20,30,100]))

import argparse
parser = argparse.ArgumentParser(description="Provides a personal greeting")
parser.add_argument(
    "-n",
    "--name",
    dest="firstname"
    metavar="name",
    required=True,
    help="The name of the person to greet",
)
args = parser.parse_args()
msg = f"Hello {args.firstname}!"


import argparse

parser = argparse.ArgumentParser(description="Provides a personal greeting")

parser.add_argument(
    "-n",
    "--name",
    metavar="name",
    required=True,
    help="The name of the person to greet",
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)



def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
        "French": "Bonjour",
    }
    msg = f"{greetings[lang]}, {name}!"
    return msg

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greeting")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet",
    )

    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "German", "Spanish", "French"],
        help="The language of the greeting",
    )

    args = parser.parse_args()

    print(hello(args.name, args.lang))