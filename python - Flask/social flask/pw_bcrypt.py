from flask.ext.bcrypt import check_password_hash, generate_password_hash

def set_password(User, password):
    hashed_pw = generate_password_hash(password)
    User.password = hashed_pw
    return User

def validate_password(User, password):
    return check_password_hash(User.password, password)
    