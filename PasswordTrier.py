import win32com.client as win32



class PasswordTrier():

    _wordList = ""
    _fileToCrack = ""

    @property
    def wordList(selfself):
        return PasswordTrier._prop

    @wordList.setter
    def wordList(self, val):
        PasswordTrier._wordList = val

    @property
    def fileToCrac(selfself):
        return PasswordTrier._fileToCrac

    @fileToCrac.setter
    def fileToCrac(self, val):
        PasswordTrier._fileToCrac = val

    def __init__(self):
        pass


    def crackFile(self):
        word = win32.Dispatch("Word.Application")

        password_file = open(self._wordList, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]


        for password in passwords:
            try:
                doc = word.Documents.Open(self._fileToCrack,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""

    @staticmethod
    def crackFile(wordlist,WordDocToCrack):
        word = win32.Dispatch("Word.Application")

        password_file = open(wordlist, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]

        for password in passwords:
            try:
                doc = word.Documents.Open(WordDocToCrack,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""