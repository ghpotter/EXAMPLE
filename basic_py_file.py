def get_hello() -> str:
    return "Hello"

def get_world() -> str:
    return "World"


def main() -> None:
    print("{} {}".format(get_hello(), get_world()))

if __name__ == '__main__':
    main()