
def increment_string(strng):
    a = list(strng)
    if a[(len(a)-1)].isdigit == True:
         print("it is true")
    else:
        print("false")
        print(a[(len(a)-1)])

    #return strng





increment_string("foo")
increment_string("foobar001")
increment_string("foobar1")
increment_string("foobar00")
increment_string("foobar99")
increment_string("foobar099")
