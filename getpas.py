from electrum.crypto import pw_decode
import getpass

password = getpass.getpass()

ctext = "B84+aykdaDMQM2q6UC8VLLnVbqWuy9aHG2ePXuXqdzq43IVwCuvtXemMvBZ0b9ERqWa+RY+Es+QRkSC13i2svGowU3vQHMDjh1GvN+fVMO/901qNLT11btbhH5Bg+9C3"
seed = pw_decode(ctext, password)
print(seed)