#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for name in dir(hid):
        if (not name.startswith("__")):
            print(name)
