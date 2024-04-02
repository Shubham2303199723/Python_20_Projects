email = (input("Enter Your Email :- "))
k=0
d=0
j=0

if len(email) >= 6:
    if email[0].isalpha():
        if email.count("@") == 1:
            if (email[-4] == ".") | (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i == i.isalpha():
                        if  i == i.upper():
                            j=1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d=1
                    if k == 1 or j == 1 or d == 1:
                        print("There Should Be no Space and no Upper charater use in Email")
            else:
                print("please use .com or .in only")
        else:
            print("There Must be @ in The MailID")
    else:
        print("First later of email should be alphabetic")
else:
    print("Email Should have more then 6 character")

