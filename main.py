print "hello world"
print "let's get started!"
print 'What\'s up?'
spy_name = raw_input("What is your name?")
if len(spy_name)>0:
    print " Welcome " + spy_name + " nice to meet you "
    spy_salutation =raw_input("What should we call you (Mr. or Ms.)?")
    print 'welcome' + spy_salutation + " " + spy_name
    print " Alright " + spy_name + " I'd like to know a little bit more about... "
    spy_age = input("what is your age?")
    if spy_age > 12 and spy_age < 50:
        spy_rating = input("What is your spy rating?")
        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
        spy_is_online = True

        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

    else:
        print 'Sorry you are not of the correct age to be a spy'

else:
    print "invalid name"