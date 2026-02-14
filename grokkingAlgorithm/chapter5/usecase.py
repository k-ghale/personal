

voters = {}

def check_voter(name):
    if(voters.get(name)):
        print("kick em out")
    else:
        voters[name] = True
        print("let em vote")

check_voter("tom")
check_voter("mike")
check_voter("mike")
