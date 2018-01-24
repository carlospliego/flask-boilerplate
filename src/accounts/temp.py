>>> import passlib
>>> from passlib.hash import pbkdf2_sha256
>>> hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)
>>> hash
'$pbkdf2-sha256$200000$Vcp5L2Vsbe1da23N2ZuT0g$o2A6u6WLqFCgBEezVNhshTq5wBys6xD8LAnI8VFy3PE'
>>> pbkdf2_sha256.verify("password", hash)
True
>>> 

