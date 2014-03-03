class MostWanted:
    def __init__(self):
        pass

    def checkio(self, text):
        txt = text.lower()
        dt = {}
        for i in txt:
            if i.isalnum():
                if not i.isdigit():
                    if i in dt:
                        dt[i] = dt[i] + 1
                    else:
                        dt[i] = 1
    
        m = max(dt.values())
        for k in dt:
            if dt[k] == m:
                return k

#These "asserts" using only for self-checking and not necessary for 
#auto-testing
# if __name__ == '__main__':
#     m = MostWanted()
    # print m.checkio(u"Lorem ipsum dolor sit amet")
    # assert m.checkio(u"Lorem ipsum dolor sit amet") == "m", "Lorem test"
#     assert checkio(u"Hello World!") == "l", "Hello test"
#     assert checkio(u"How do you do?") == "o", "O is most wanted"
#     assert checkio(u"One") == "e", "All letter only once."
#     assert checkio(u"Lorem ipsum dolor sit amet 00000000000000000000000")
