from passlib.hash import sha256_crypt


class Password:
    @classmethod
    def generate_password(cls, password):
        hash_password = sha256_crypt.encrypt(password)

        return hash_password

    @classmethod
    def check_password(cls, hash_password, password):
        if sha256_crypt.verify(password, hash_password):
            check = 1
            return check
        else:
            check = 0
            return check
