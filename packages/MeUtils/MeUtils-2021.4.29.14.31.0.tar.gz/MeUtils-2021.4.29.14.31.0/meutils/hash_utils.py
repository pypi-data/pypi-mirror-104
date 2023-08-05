#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : hashtrick
# @Time         : 2020-04-10 16:54
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import hashlib as _hashlib
from sklearn.utils.murmurhash import murmurhash3_32 as _murmurhash3_32

"""Java
import java.nio.charset.StandardCharsets
import com.google.common.hash.Hashing.murmur3_32

def hash(key: String = "key", value: String = "value", bins: Int = 10000): Int = {
    val hashValue: Int = murmur3_32.newHasher.putString(f"{key}:{value}", StandardCharsets.UTF_8).hash.asInt
    Math.abs(hashValue) % bins  
  }
"""


def md5(string: str):
    return _hashlib.md5(string.encode('utf8')).hexdigest()


def murmurhash(key="key", value="value", bins=None, str2md5=True):
    """key:value"""
    string = f"{key}:{value}"
    if str2md5:
        string = md5(string)

    _ = abs(_murmurhash3_32(string, positive=True))  # 与javayi一致
    return _ % bins if bins else _


if __name__ == '__main__':
    print(md5("key:value"))
    print(murmurhash(str2md5=False, bins=10000))  # 3788
    print(murmurhash(str2md5=True, bins=10000))  # 1688 5608
