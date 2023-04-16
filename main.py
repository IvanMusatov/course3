from functions import load_data, sorted_state_executed, manipulation


def main():
    data = load_data()
    data = sorted_state_executed(data)
    return manipulation(data)

