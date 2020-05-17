# @desc: 将指定目录中，存在重复的文件，予以移除。

import os
import sys
import hashlib
from pathlib import Path

def getmd5(filename):
    file_contnet = open(filename, 'rb').read()
    md5 = hashlib.md5(file_contnet)
    return md5.hexdigest()

def main(path):
    all_size = {}
    total_file = 0
    total_delete = 0
    
    for file in os.listdir(path):
        total_file += 1
        real_path = os.path.join(path, file)
        if os.path.isfile(real_path) == True:
            size = os.stat(real_path).st_size
            name_and_md5 = [real_path, '']
            if size in all_size.keys():
                new_md5 = getmd5(real_path)
                if all_size[size][1] == '':
                    all_size[size][1] = getmd5(all_size[size][0])
                if new_md5 in all_size[size]:
                    file_path = os.path.join(path, file)
                    os.remove(file_path)
                    print('🦑 重复文件，删除 @', file_path)
                    total_delete += 1
                else:
                    all_size[size].append(new_md5)
            else:
                all_size[size] = name_and_md5
    print('📷 文件的总个数：', total_file)
    print('🛠 删除重复个数：', total_delete)

if __name__ == '__main__':
    argvList = sys.argv
    specifiedPath = argvList[1]
    main(specifiedPath)