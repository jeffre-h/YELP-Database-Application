import pyodbc
import functions

conn = pyodbc.connect('driver={ODBC Driver 18 for SQL Server};server=cypress.csil.sfu.ca;uid=s_jwa334;pwd=FRaJby3tj4ntnYQy;Encrypt=yes;TrustServerCertificate=yes')
cursor = conn.cursor()

# run on visual studio code on CSIL machine w/ command: python main.py
print("\n~ run on CSIL machine w/ command: 'python main.py' ")

# Log in
valid = False
while (not valid):
    userID = input("\nenter user ID: ")
    valid = functions.login(userID, cursor)
    if not valid: print("the user ID entered is invalid ...")


# Actions user can perform 
print("\nloading... \n")
print("functions: \n(1) search business\n(2) search user\n(3) make friend\n(4) write review\n(5) log out")
action = input("\nenter 1, 2, 3, 4, or 5 to perform corresponding function: ")

while (action != '5'):
    # search business
    if (action == '1'):
        print("\nsearching for business ...\n")
        empty = functions.searchBusiness(cursor)
        if empty: print("-> no business were found matching this criteria ...")

    # search user
    elif (action == '2'):
        print("\nsearching for user ...\n")
        empty = functions.searchUser(cursor)
        if empty: print("-> no users were found matching this criteria ...")

    # make friend
    elif (action == '3'):
        print("\nmaking friendship ...\n")
        functions.makeFriend(userID, cursor, conn)
    
    # write review
    elif (action == '4'):
        print("\nwriting review ...\n")
        functions.writeReview(userID, cursor, conn)
    
    # invalid input
    else:
        print("\ninput is invalid, try again")

    print("\nnext ...\n")
    print("functions: \n(1) search business\n(2) search user\n(3) make friend\n(4) write review\n(5) log out")
    action = input("enter 1, 2, 3, 4, or 5 to perform corresponding function: ")

print("\nsuccessfully logged out ...\n")

conn.close()