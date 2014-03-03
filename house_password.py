class HousePwd:
    def __init__(self):
        pass

    def checkio(self, data):
        #replace this for solution
        cd = cl = cu = 0
        if len(data) >= 10:
            for iter in range(len(data)):
                if data[iter].isdigit():
                    cd = cd + 1
                if data[iter].isalpha():
                    if data[iter].islower():
                        cl = cl + 1
                    if data[iter].isupper():
                        cu = cu + 1
            if cd >= 1 and cl >= 1 and cu >= 1:
                return True
            else:
                return False
        else:
            return False

#Some hints
#Just check all conditions


#These "asserts" using only for self-checking and not necessary for 
#auto-testing
# if __name__ == '__main__':
#     assert checkio(u'A1213pokl') == False, "1st example"
#     assert checkio(u'bAse730onE4') == True, "2nd example"
#     assert checkio(u'asasasasasasasaas') == False, "3rd example"
#     assert checkio(u'QWERTYqwerty') == False, "4th example"
#     assert checkio(u'123456123456') == False, "5th example"
#     assert checkio(u'QwErTy911poqqqq') == True, "6th example"
