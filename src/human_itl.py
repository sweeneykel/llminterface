
def human_itl_confirms(confirm_question: str, confirm_info: str):
    print(confirm_question, confirm_info)
    human_confirmation = input("Type CONFIRM to proceed. Any other letter will cancel this process: ").strip()
    if human_confirmation == "CONFIRM":
        return True
    else:

        return False