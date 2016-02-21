import hashlib
import os.path


class HashGen():
    # CLASS CONSTRUCTOR
    def __init__(self):
        pass

    def sha1Encode(self, text):
        if not os.path.isfile(str(text)):  # check if is a file
            if not text:  # check if its a string
                return "No String passed to method"
            else:
                m = hashlib.sha1()  # create new sha1 object
                m.update(text.encode('utf-8'))  # call udate method passing the 'utf-8' as an argument
                return (m.hexdigest())  # return the hash by calling hexdigest Method which returns the hash value
        else:
            BLOCKSIZE = 65536  # set the block size see :
            # http://www.dhillonblog.com/2014/07/understanding-io-request-block-size/
            hasher = hashlib.sha1()
            with open(text, 'rb') as afile:  # open file in read byte mode
                buf = afile.read(BLOCKSIZE)  # create a buffer of size blocksize call the file.read method
                while len(buf) > 0:  # while the length of the buffer is greater then a zero keep iterating
                    hasher.update(buf)  # append buffer to the current value in the hasher object
                    buf = afile.read(BLOCKSIZE)
            return (
            hasher.hexdigest())  # finally return the hash by calling hexdigest Method which returns the hash value

    @staticmethod
    def sha1Encode(text):
        if not os.path.isfile(str(text)):  # check if is a file
            if not text:  # check if its a string
                return "No String passed to method"
            else:
                m = hashlib.sha1()  # create new sha1 object
                m.update(text.encode('utf-8'))  # call udate method passing the 'utf-8' as an argument
                return (m.hexdigest())  # return the hash by calling hexdigest Method which returns the hash value
        else:
            BLOCKSIZE = 65536  # set the block size see :
            # http://www.dhillonblog.com/2014/07/understanding-io-request-block-size/
            hasher = hashlib.sha1()
            with open(text, 'rb') as afile:  # open file in read byte mode
                buf = afile.read(BLOCKSIZE)  # create a buffer of size blocksize call the file.read method
                while len(buf) > 0:  # while the length of the buffer is greater then a zero keep iterating
                    hasher.update(buf)  # append buffer to the current value in the hasher object
                    buf = afile.read(BLOCKSIZE)
            return (
            hasher.hexdigest())  # finally return the hash by calling hexdigest Method which returns the hash value