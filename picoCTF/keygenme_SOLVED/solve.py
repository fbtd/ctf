import hashlib

username_trial = b"SCHOFIELD"
hased_username = hashlib.sha256(username_trial).hexdigest()


# keygenme-trial.py lines 157 and following
indexes = '4 5 3 6 2 7 1 8'.split()


key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"

key_part_dynamic1_trial = ''.join([
    hased_username[int(i)] for i in indexes
])

key_part_static2_trial = "}"

print(key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial)
