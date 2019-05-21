from unittest import TestCase
from ibancheck import IBANcheck

class TestIBAN(TestCase):

    def test_ibancheckDE(self):
        self.assertTrue(IBANcheck.check("DE89370400440532013000"))

    def test_ibancheckFalseDE(self):
        self.assertFalse(IBANcheck.check("DE84370400440532013000"))

    def test_ibancheckWithSpacesDE(self):
        self.assertTrue(IBANcheck.check(" DE89 3704 0044 0532 0130 00 "))

    def test_ibancheckWithSpacesUK(self):
        self.assertTrue(IBANcheck.check("GB29 NWBK 6016 1331 9268 19"))

    def test_ibancheckABunchOfValidOnes(self):
        #taken from
        #http://www.rbs.co.uk/corporate/international/g0/guide-to-international-business/regulatory-information/iban/iban-example.ashx
        ibans = {
            "Just long enough": "AB451",
            "Albania": "AL47 2121 1009 0000 0002 3569 8741",
            "Austria": "AT61 1904 3002 3457 3201",
            "France": "FR14 2004 1010 0505 0001 3M02 606",
            "Germany": "DE89 3704 0044 0532 0130 00",
                # "United Kingdom": "GB29 RBOS 6016 1331 9268 19" This is actually a false number
            "United Kingdom": "GB29 NWBK 6016 1331 9268 19",
            "Italy": "IT40 S054 2811 1010 0000 0123 456",
            "Liechtenstein": "LI21 0881 0000 2324 013A A",
            "Spain": "ES80 2310 0001 1800 0001 2345",
            "Switzerland": "CH93 0076 2011 6238 5295 7"
        }
        for country, iban in ibans.items():
            self.assertTrue(IBANcheck.check(iban), "Didn't work for " + country)

    def test_ibancheckABunchOfInvalidOnes(self):
        #taken from
        #http://www.rbs.co.uk/corporate/international/g0/guide-to-international-business/regulatory-information/iban/iban-example.ashx
        ibans = {
            "Too Short": "AB12",
            "Long Enough but apha checksum": "ABA51",
            "Albania": "AL47 2121 1009 0000 0002 3560 8741",
            "Austria": "AT61 1904 3002 3757 3201",
            "France" : "FR14 2004 1010 A505 0001 3M02 606",
            "Germany": "DE89 3704 0Ä44 0532 0130 00",
            "United Kingdom": "GB29 RBOS 6016 1331 9268 19", #This is actually a false number
            "United Kingdom2": "GB29 NWKK 6016 1331 9268 19",
            "Italy" : "IT40 S054 281A 1010 0000 0123 456",
            "Liechtenstein" : "LI21 0881 0000 2324 0131 A",
            "Spain" : "ES81 2310 0001 1800 0001 2345",
            "Switzerland" : "CH93 0076 2011 6238 529B 7"
        }
        for country, iban in ibans.items():
            self.assertFalse(IBANcheck.check(iban), "Didn't work for " + country)

    def test_splitiban(self):
        (countrycode, checksum, bban) = IBANcheck.splitiban("DE123456789")
        self.assertEqual("DE", countrycode)
        self.assertEqual("12", checksum)
        self.assertEqual("3456789", bban)

    def test_splitibanWhitespaces(self):
        (countrycode, checksum, bban) = IBANcheck.splitiban(" DE12 34567 89 ")
        self.assertEqual("DE", countrycode)
        self.assertEqual("12", checksum)
        self.assertEqual("3456789", bban)

    def test_splitibanTooShort(self):
        (countrycode, checksum, bban) = IBANcheck.splitiban("DE")
        self.assertEqual("DE", countrycode)
        self.assertEqual("", checksum)
        self.assertEqual("", bban)

    def test_letter2numFound(self):
        self.assertEqual("13", IBANcheck.letter2num("D"))

    def test_letter2numNotFound(self):
        self.assertEqual("", IBANcheck.letter2num("Ä"))

    def test_letter2numEmptyInput(self):
        self.assertEqual("", IBANcheck.letter2num(""))

    def test_letter2numWrongType(self):
        self.assertEqual("", IBANcheck.letter2num(2.2))

    def test_letter2numInputTooLong(self):
        self.assertEqual("", IBANcheck.letter2num("DA"))

    def test_string2numstringNormalOperation(self):
        self.assertEqual("1314", IBANcheck.string2numstring("DE"))

    def test_string2numstringNormalOperationGB(self):
        self.assertEqual("1611", IBANcheck.string2numstring("GB"))

    def test_string2numstringNormalOperationWithNumbers(self):
        self.assertEqual("13140129", IBANcheck.string2numstring("DE0129"))

    def test_string2numstringEmptyInput(self):
        self.assertEqual('', IBANcheck.string2numstring(""))

    def test_string2numstringWrongLetterIgnored(self):
        self.assertEqual("13", IBANcheck.string2numstring("DÄ"))
