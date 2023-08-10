from classes import People


def main():
    entrada = (input("1.Register\n2.Check?\n"))
    if entrada == "Register":
        People.register_new_user()
        main()
    elif entrada == "Check":
        People.check_user()
        main()
    else:
        print("Sorry I didnt understand")
        main()

main()
