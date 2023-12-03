#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        for item in my_list:
            print('{}'.format(item))

    def hello():
        hi = [2, 3  , 3, 6,3]
        print_list_integer(hi)

    hello()
