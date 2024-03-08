# collect email from user
# split the email using the @, the first part as the user name, the second part is gonna be saved as domain name
# split domain using . 


def main():
    print("Welcome to the Email Slicer")
    print("")

    email_input = input("Enter Yor Email Address ")
    (name, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print("Name :- ", name)
    print("Domain :- ", domain)
    print("Extension :- " , extension)

main()
