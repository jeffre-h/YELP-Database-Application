import random
import datetime

def login(userID, cursor):
    cursor.execute('SELECT user_id FROM user_yelp')
    
    row = cursor.fetchone()
    while row:
        if row[0] == userID:
            return True
        row = cursor.fetchone()

    return False


def searchBusiness(cursor):
    query = "SELECT business_id, name, address, city, stars FROM business"
    token = False
    ret = True
    
    # min stars filter
    r = input("would you like to filter by minimum number of stars (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            min = input("min number of stars (1,2,3,4,5): ")
            while (min not in ['1','2','3','4','5']):
                 min = input("    invalid input, try again: ")
            query += " WHERE stars >= " + min
            token = True
        
        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()

    # max stars filter
    r = input("\nwould you like to filter by maximum number of stars (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            max = input("max number of stars (1,2,3,4,5): ")
            while (max not in ['1','2','3','4','5'] or max < min):
                if (max < min):
                    max = input("    max must be greater than min, try again: ")
                else: max = input("    invalid input, try again: ")
            if token == False:
                query += " WHERE stars <= " + max
                token = True
            else:
                query += " AND stars <= " + max
        
        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()
    
    # city filter
    r = input("\nwould you like to filter by city (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':      
            city = input("city name: ").lower()
            
            if token == False:
                query += " WHERE LOWER(city) = '" + city + "'"
                token = True
            else:
                query += " AND LOWER(city) = '" + city + "'"    
        
        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()
   
    # business name filter
    r = input("\nwould you like to filter by business' name (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            bus = input("business name or part of a business name: ").lower()
            
            if token == False:
                query += " WHERE LOWER(name) LIKE '%" + bus + "%'"
                token = True
            else:
                query += "AND LOWER(name) LIKE '%" + bus + "%'"
        
        if r not in ['y', 'n']:
            valid = False
            r = input("    invalid input, try again: ").lower()

    print("\nquery inputted: " + query)
    try:
        cursor.execute(query + " ORDER BY name")
        print("\nresults:")
        for i in cursor: 
            ret = False
            print(i)
    except:
        print("\nerror ...")

    return ret


def searchUser(cursor):
    query = "SELECT user_id, name, useful, funny, cool FROM user_yelp"
    token = False
    ret = True

    # filter by name
    r = input("would you like to filter by user's name (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            query += " WHERE LOWER(name) LIKE '%" + input("    name: ").lower() + "%'"
            token = True

        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()

    # filter by useful
    r = input("\nwould you like to apply the useful filter (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            useful = input("filter by useful (y) or not useful (n): ").lower()
            valid = False
            while (not valid):
                valid = True
                # filter by useful
                if useful == 'y':
                    if (token == False):
                        query += " WHERE useful > 0"
                        token = True
                    else:
                        query += " AND useful > 0"
                # filter by not useful
                elif useful == 'n':
                    if (token == False):
                        query += " WHERE useful = 0"
                        token = True
                    else:
                        query += " AND useful = 0"
                # invalid input
                else:
                    valid = False
                    useful = input("    invalid input, try again: ").lower()

        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()

    # filter by funny
    r = input("\nwould you like to apply the funny filter (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            funny = input("filter by funny (y) or not funny (n): ").lower()
            valid = False
            while (not valid):
                valid = True
                # filter by funny
                if funny == 'y':
                    if (token == False):
                        query += " WHERE funny > 0"
                        token = True
                    else:
                        query += " AND funny > 0"
                # filter by not funny
                elif funny == 'n':
                    if (token == False):
                        query += " WHERE funny = 0"
                        token = True
                    else:
                        query += " AND funny = 0"
                # invalid input
                else:
                    valid = False
                    funny = input("    invalid input, try again: ").lower()

        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()

    # filter by cool
    r = input("\nwould you like to apply the cool filter (y/n): ").lower()
    valid = False
    while (not valid):
        valid = True
        if r == 'y':
            cool = input("filter by cool (y) or not cool (n): ").lower()
            valid = False
            while (not valid):
                valid = True
                # filter by cool
                if cool == 'y':
                    if (token == False):
                        query += " WHERE cool > 0"
                        token = True
                    else:
                        query += " AND cool > 0"
                # filter by not cool
                elif cool == 'n':
                    if (token == False):
                        query += " WHERE cool = 0"
                        token = True
                    else:
                        query += " AND cool = 0"
                # invalid input
                else:
                    valid = False
                    cool = input("    invalid input, try again: ").lower()

        if r not in ['y','n']:
            valid = False
            r = input("    invalid input, try again: ").lower()
    

    print("\nquery inputted: " + query)
    try:
        cursor.execute(query + " ORDER BY name")
        print("\nresults:")
        row = cursor.fetchone()
        while row:
            ret = False
            for i in range(2,5):
                if row[i] > 0:
                    row[i] = "yes"
                else:
                    row[i] = "no"

            print(row)
            row = cursor.fetchone()
    except:
        print("\ninvalid filter input has led to an error, try again ...")

    return ret


def makeFriend(userID, cursor, conn):
    friendID = input("enter a userID for a friend in which you want to create friendship with: ")

    valid = False
    while (not valid):
        valid = True

        if not login(friendID, cursor) or userID == friendID: valid = False # invalid ID -> friendship can't be made
        cursor.execute('SELECT * FROM friendship')

        row = cursor.fetchone()
        while row:
            if (row[0] == userID and row[1] == friendID):
                valid = False    # friendship already exists -> friendship can't be made
            if (row[0] == friendID and row[1] == userID):
                valid = False    # friendship already exists -> friendship can't be made
            row = cursor.fetchone()

        if (not valid): friendID = input("    invalid userID for friend entered, try again: ")

    try:
        cursor.execute("""INSERT INTO friendship(user_id,friend) VALUES(?,?)""", userID, friendID)
        conn.commit()
    except:
        print("\nerror ...")

    return 
  

def writeReview(userID, cursor, conn):
    chars = ['_','-','0','1','2','3','4','5','6','7','8','9',
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # review_id
    duplicate = True
    while (duplicate):
        duplicate = False
        reviewID = ""
        for i in range(0,22): reviewID += random.choice(chars)

        cursor.execute('SELECT review_id FROM review')
        for i in cursor:
            if i[0] == reviewID: duplicate = True

    # business_id
    busID = input("enter businessID you're reviewing: ")
    valid = False
    while (not valid):
        cursor.execute('SELECT business_id FROM business')
        for i in cursor:
            if i[0] == busID: valid = True

        if not valid:
            busID = input("    invalid businessID, try again: ")

    # stars 
    stars = input("\nstar rating of your review (1, 2, 3, 4, or 5): ")
    valid = False
    while (not valid):
        if stars in ['1','2','3','4','5']: 
            valid = True
        else:
            stars = input("    invalid star rating, try again: ")

    # current date
    date = datetime.datetime.now()

    try:
        cursor.execute("""INSERT INTO review(review_id, user_id, business_id, stars, useful, funny, cool, date) VALUES(?,?,?,?,0,0,0,?)""", reviewID, userID, busID, stars, date)
        conn.commit()
    except:
        print("\nerror ...")
    
    return 