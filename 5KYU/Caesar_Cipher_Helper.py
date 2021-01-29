class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def checkrange_encode(self, alp):
        self.alp = alp.lower()
        if ord(self.alp) - 96 <= 26 - self.shift:
            return chr(ord(self.alp) + self.shift).upper()
        return chr(self.shift - (26 - ord(self.alp))).upper()

    def checkrange_decode(self, alp):
        self.alp = alp.lower()
        if ord(self.alp) - 96 > self.shift:
            return chr(ord(self.alp) - self.shift).upper()
        return chr(26 - self.shift + ord(self.alp)).upper()

    def encode(self, st):
        return "".join([self.checkrange_encode(i) if i.isalpha() else i for i in st.upper()])
        
    def decode(self, st):
        return "".join([self.checkrange_decode(i) if i.isalpha() else i for i in st])