def get_login_name():

    first_name = input("Enter first name: ").upper()
    last_name = input("Enter lastname: ").upper()
    stud_id = input("Enter ID: ")
    if len(stud_id) > 3:
        stud_id = stud_id[0:3]
    login_name = first_name[0:3] + last_name[0:3] + stud_id

    return login_name


if __name__ == "__main__":
    get_login_name()
