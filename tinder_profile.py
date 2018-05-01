def gets_user_name():
    """gets the user's name"""
    name = raw_input("What's your name? ")
    return name


def gets_user_age():
    """gets user's age"""
    age = raw_input("What's your age? ")
    while True:
        if age.isdigit():
            return int(age)
        elif not age.isdigit():
            age = raw_input("Please list your age as a number, not a word.")
 

def gets_user_gender():
    """gets user's gender"""
    while True:
        gender = raw_input("What gender do you idenify as? Type: (F) Female, (M) Male, (N) Gender-Neutral/Gender Non-conforming, (T) Trans-gender, (Q) Queer  ").capitalize()
        if gender == "M":
            gender = "male"
            False
            return gender
        elif gender == "F":
            gender = "female"
            False
            return gender
        elif gender == "N":
            gender = "gender-neutral/gender non-conforming"
            False
            return gender
        elif gender == "T":
            gender = "trans-gender"
            False
            return gender
        elif gender == "Q":
            gender = "queer"
            False
            return gender
        else:
            print "I know gender is a spectrum.  Even though it is not perfect- please choose from (F) Female, (M) Male, (N) Gender-Neutral/Gender Non-conforming, (T) Trans-gender, (Q) Queer."
        
    
def gets_user_interests():
    """gets user's interests"""
    interests= raw_input("Tell us about yourself.  List three things you like doing, separated by a comma:  ").lower()
    interests_lst = interests.split(",")
    return interests_lst
    
#Now, we're going to get info about who they want to date

def gets_mate_gender():
    """gets the preferred gender of date"""
    while True:
        mate_gender = raw_input("What gender person do you want to meet? Type: (F) Female, (M) Male, (N) Gender-Neutral/Gender Non-conforming, (T) Trans-gender, (Q) Queer  ").capitalize()
        if mate_gender == "M":
            mate_gender = "male"
            False
            return mate_gender
        elif mate_gender == "F":
            mate_gender = "female"
            False
            return mate_gender
        elif mate_gender == "N":
            mate_gender = "gender-neutral/gender non-conforming"
            False
            return mate_gender
        elif mate_gender == "T":
            mate_gender = "trans-gender"
            False
            return mate_gender
        elif mate_gender == "Q":
            mate_gender = "queer"
            False
            return mate_gender
        else:
            print "I know gender is a spectrum.  Even though it is not perfect- please choose from (F) Female, (M) Male, (N) Gender-Neutral/Gender Non-conforming, (T) Trans-gender, (Q) Queer."

def gets_mate_low_age():
    """gets the lowest preferred age of date"""
    mate_low_age= raw_input("What is the lowest age (youngest) you prefer to date? ")
    while True:
        if mate_low_age.isdigit():
            return int(mate_low_age)
        elif not mate_low_age.isdigit():
            mate_low_age = raw_input("Please list the lowest age as a number, not a word.")

def gets_mate_high_age():
    mate_high_age= raw_input("What is the highest age (oldest) you prefer to date? ")
    while True:
        if mate_high_age.isdigit():
            return int(mate_high_age)
        elif not mate_high_age.isdigit():
            mate_high_age = raw_input("Please list the highest age as a number, not a word.")


def gets_desired_rel():
    """gets desired typle/length of relationship"""
    while True: 
        rel_length= raw_input("What type of relationship are you looking for?  Choose from: (L) long-term, (S) short-term, (P) poly, or (A) alternative.  ").capitalize()
        if rel_length == "L":
            rel_length = "long-term"
            False
            return rel_length
        elif rel_length == "S":
            rel_length = "short-term"
            False
            return rel_length
        elif rel_length == "P":
            rel_length = "polygamous"
            False
            return rel_length
        elif rel_length == "A":
            rel_length = raw_input("Tell me more about the type of relationship you're looking for.  ")
            False
            return rel_length
        else: 
            print "I know, just like gender, relationships and sexuality are a spectrum.  If you don't see your preferred relationship type here- choose A for alternative.  Please type only the letter."
    return rel_length


#continue to add elif combos and profile info... OR set up a dictionary of options so that if they choose M looking for M, long-term, q they get one option- do the various options?



def runs_profile_generator():
    #"""master function that will call on the other functions to create a profile"""
    user_name = gets_user_name()
    user_age = gets_user_age()
    user_gender = gets_user_gender()
    user_interests = gets_user_interests()
    mate_gender = gets_mate_gender()
    mate_low_age = gets_mate_low_age()
    mate_high_age = gets_mate_high_age()
    if user_age - 20 > mate_high_age:
        print "Looks like you like 'em young!"
    if user_age + 20 < mate_low_age:
        print "You like 'em a bit older, huh?!"
    desired_rel = gets_desired_rel()
    if user_gender == "female":
        print "{}, {} and {} :if you like any of these three things, we will get along great. If you like all three, you could just be the love of my life.".format(user_interests[0], user_interests[1], user_interests[2])
        print "If you only like {}, we'll probably still be friends. ".format(user_interests[2])
        print "I am looking for a {} relationship with a {}, aged {} to {}.".format(desired_rel, mate_gender, mate_low_age, mate_high_age)
        if user_age + 20 < mate_low_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
        elif user_age - 20 > mate_high_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
    elif user_gender == "male":
        print "If you like water, you already like 72 percent of me.  Here's me in a nutshell: I'm {}, identify as {} and love {}.  I'm also really excited about {} and {}.".format(user_age, user_gender, user_interests[0], user_interests[1], user_interests[2])
        print "I am looking for a {} relationship with a {} person, aged {} to {}.".format(desired_rel, mate_gender, mate_low_age, mate_high_age)
        if user_age + 20 < mate_low_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
        elif user_age - 20 > mate_high_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
    elif user_gender == "queer":
        print "I love all kinds of things and would love to tell you more about them in person.  I'm {} years old, identify as {} and love {}. ".format(user_age, user_gender, user_interests[0])
        print "Other favorite things include {} and {}.".format(user_interests[1], user_interests[2])
        print "I am looking for a {} relationship with someone who identifies as {}, aged {} to {}".format(desired_rel, mate_gender, mate_low_age, mate_high_age)
        if user_age + 20 < mate_low_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
        elif user_age - 20 > mate_high_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
    elif user_gender == "gender-neutral/gender non-conforming" or "trans-gender":
        print "Bianary gender identities are boring... and I am not.  I'm {}, identify as {} and love {}. ".format(user_age, user_gender, user_interests[0])
        print "Other favorite things include {} and {}.".format(user_interests[1], user_interests[2])
        print "I am looking for a {} relationship with a {} person, aged {} to {}.".format(desired_rel, mate_gender, mate_low_age, mate_high_age)
        if user_age + 20 < mate_low_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
        elif user_age - 20 > mate_high_age:
            print "Age is just a number, but if my preferences offend you- swipe left. "
    return()



print "So you wanna date... or someday stop dating... or date everyone, forever, whenever you want.  You need a Tinder profile." "\n"
runs_profile_generator()