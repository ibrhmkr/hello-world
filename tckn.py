class TCKN:

    def __init__(self, tckn_str):
        self.tckn_str = tckn_str
        self._haserror = False
        self._initialerrorcheck = True
        self.errors = []
        self.num_errors = 0
        self._validtype = self._isvalidtype()
        self.isvalid = self._istcknvalid()

    def _isvalidtype(self):
        # a string parameter expected
        ret = True
        if not isinstance(self.tckn_str, str):
            self._haserror = True
            self.num_errors += 1
            self.errors.append('invalid type, a string of numerals expected')
            ret = False
        return ret

    def _isvalidnum(self):
        # must be numeric
        if not self.tckn_str.isnumeric():
            self._haserror = True
            self.num_errors += 1
            self.errors.append('all characters must be numeric')

    def _isvalidfirstchar(self):
        # first digit must be non-zero
        if self.tckn_str[0] == '0':
            self._haserror = True
            self.num_errors += 1
            self.errors.append('number must not start with 0')

    def _isvalidlength(self):
        # must be 11 digits in length
        if len(self.tckn_str) != 11:
            self._haserror = True
            self.num_errors += 1
            self.errors.append('number must have 11 digits')

    @property
    def haserror(self):
        if self._initialerrorcheck:
            self._initialerrorcheck = False
            if self._validtype:
                self._isvalidnum()
                self._isvalidfirstchar()
                self._isvalidlength()
        return self._haserror

    @property
    def checkdigit1(self):
        # check digit1 (10th digit) is the remainder in mod 10 of difference between sum of odd digits
        # multiplied by 7 and sum of even digits excluding check digits
        if self.isvalid:
            s1 = sum(int(self.tckn_str[i]) for i in range(0, 9, 2)) * 7
            s2 = sum(int(self.tckn_str[i]) for i in range(1, 8, 2))
            return (s1 - s2) % 10
        else:
            return None

    @property
    def checkdigit2(self):
        # check digit2 (last digit) is the remainder in mod 10 of sum of first 10 digits
        if self.isvalid:
            return (sum(int(self.tckn_str[i]) for i in range(9)) + self.checkdigit1) % 10
        else:
            return None

    def _istcknvalid(self):
        if self._validtype:
            if not self.haserror:
                if int(self.tckn_str[9]) == self.checkdigit1 and int(self.tckn_str[10]) == self.checkdigit2:
                    return True
                else:
                    return False
            else:
                return None
        else:
            return None
