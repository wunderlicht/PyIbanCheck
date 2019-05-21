import string

class IBANcheck:

    @staticmethod
    def check(iban: str) -> bool:
        (countrycode, checksum, bban) = IBANcheck.splitiban(iban)
        countrycode_num = IBANcheck.string2numstring(countrycode)
        checksum_num    = IBANcheck.string2numstring(checksum)
        bban_num        = IBANcheck.string2numstring(bban)
        str_under_check = bban_num + countrycode_num + checksum_num
        return int(str_under_check) % 97 == 1

    @staticmethod
    def splitiban(iban: str) -> (str, str, str):
        strippediban = "".join(iban.split()) #this kills all whitespaces
        countrycode  = strippediban[0:2] #"DE"
        checksum     = strippediban[2:4] #"12"
        bban         = strippediban[4:] #"3456789"
        return (countrycode, checksum, bban)

    @staticmethod
    def letter2num(letter: str) -> str:
        numbers = list(string.digits)
        letters = list(string.ascii_uppercase)
        lookup =  numbers + letters
        try:
            position = str(lookup.index(letter))
        except ValueError:
            position = ""

        return position

    @staticmethod
    def string2numstring(input:str) -> str:
        result = []
        for char in input:
            num4letter = IBANcheck.letter2num(char)
            result.append(num4letter)

        return ''.join(result)
