import base64

from PyQt5 import QtCore, QtGui, QtWidgets

dict = {'1': 'e', '2': 'j', '3': 'o', '4': 't', '5': 'y', '6': 'd', '7': 'i', '8': 'n', '9': 's', '10': 'x', '11': 'c',
        '12': 'h', '13': 'm',
        '14': 'r', '15': 'w', '16': 'b', '17': 'g', '18': 'l', '19': 'q', '20': 'v',
        '21': 'a', '22': 'f', '23': 'k', '24': 'p', '25': 'u', '26': 'z'}
dict2 = {'1': 'ae', '2': 'eer', '3': 'irr', '4': 'nq', '5': 'kfr', '6': 'vs', '7': 'zt', '8': 'b', '9': 'fvgd', '10': 'js', '11': 'o',
         '12': 'ss', '13': 'wryh',
         '14': 'l', '15': 'cs', '16': 'gg', '17': 'k', '18': 'prg', '19': 'tc', '20': 'x',
         '21': 'dxf', '22': 'h', '23': 'me', '24': 'qx', '25': 'ub', '26': 'y'}


def encrypted(password):
    if len(password) == 0:
        return 'null'
    if len(password) > 26:
        return 'long'
    a = base64.urlsafe_b64encode(password.encode('utf-8'))
    pw = dict[str(len(password))]+str(len(password)) + str(password[0:len(password) // 2]) + str(a)[2:len(str(a)) - 1] + str(
        password[len(password) // 2:len(password)])
    pw64 = base64.urlsafe_b64encode(pw.encode('utf-8'))
    pw64s = str(pw64)[2:len(str(pw64)) - 1]
    print(pw64s)
    return dict2[str(len(password))].upper() + pw64s + dict[str(len(password))]


def decrypted(strpw):
    pwlengthstr = strpw[len(strpw) - 1:len(strpw)]
    for key, value in dict.items():
        if value == pwlengthstr:
            pwlength = key
    stru = strpw[len(dict2[pwlength]):len(strpw) - 1]
    p = base64.urlsafe_b64decode(stru)
    ee = p[len(str(pwlength))+1:len(p)]
    ss = int(pwlength) - int(pwlength) // 2
    pwb = ee[0:int(pwlength) // 2] + ee[len(ee) - ss:len(ee)]
    pw = str(pwb)[2:len(str(pwb)) - 1]
    print(pw)
