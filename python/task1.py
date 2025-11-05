if __name__ == "__main__":
    hello = "Hello world"
    # Output to term
    print(hello)
    # Write to file
    with open("hello_world.txt", "w", encoding="utf-8") as f:
        f.write(hello)