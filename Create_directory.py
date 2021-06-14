import os
from sys import platform

def mkdir_dir(path): #path : 생성할 directory의 path
    if os.path.isdir("{udf}\\Zconverter_TF\\userdata".format(udf = userprofile))== False: #userdata가 존재하는지 확인
        os.mkdir("{udf}\\Zconverter_TF\\userdata".format(udf = userprofile))
    if os.path.isdir(path) == False: #path에 directory가 존재하는지 확인
        os.mkdir(path)
    return
