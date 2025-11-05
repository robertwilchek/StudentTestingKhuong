if __name__ == "__main__":

    with open("backup.csv", "r", encoding="utf-8") as f:
        d = dict(f)
        print(d)