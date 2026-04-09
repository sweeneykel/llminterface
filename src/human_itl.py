from operator import truediv


# print("This is the SQL command that will be used to create a new table: ", modify_db_sql_command)
# user_choice = input("Do you want to proceed with this command? Type CONFIRM"
#                     " to proceed. Type any other letter to cancel this process:   ").strip()
# if user_choice == "CONFIRM":

def human_itl_confirms(confirm_question: str, confirm_info: str):
    print(confirm_question, confirm_info)
    human_confirmation = input("Type CONFIRM to proceed. Any other letter will cancel this process: ").strip()
    if human_confirmation == "CONFIRM":
        return True
    else:

        return False