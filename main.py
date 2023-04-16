from functions import load_data, sorted_state_executed, manipulation


def main():
    data = load_data()
    data = sorted_state_executed(data)
    return manipulation(data)


<<<<<<< HEAD

=======
if __name__ == '__main__':
    main()
>>>>>>> parent of d78f21e (Revert "develop project")
