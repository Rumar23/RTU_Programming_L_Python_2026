def greet_user(name: str) -> str:
    name = name.strip()
    if not name:
        name = "Stranger"
    name = name.capitalize()
    return f"Hello, {name}! Welcome to Python!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
