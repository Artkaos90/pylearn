
if __name__ == '__main__':
    processed_employees = 0
    while processed_employees < 5:
        print("Insert email")
        email = input()
        if email == "":
            print("Insert break")
            break
        print("Insert job")
        job = input()

        system = None
        access_attempts = None

        if job == "Developer":
            system = "GIT"
            access_attempts = 1
        elif job == "Designer":
            system = "Illustrator"
            access_attempts = 3
        else:
            print("You have to go across thee doors at right")
            continue

        for _ in range (access_attempts):
            print(f"{email} was acces in {system}")

        print(f"Was added {processed_employees} people, stay {5 - processed_employees}")
        processed_employees += 1