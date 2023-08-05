#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
import os
import re

sys.path.append('/Users/robertoneves/Projetos/bravaorm/')
sys.path.append('/Users/robertoneves/Projetos/dbmodel/')

import bravaorm
from model import *

import time
import json

def main(arg):
    start = time.time()

    conn = bravaorm.Connection(db_user="root", db_password="1234", db_host="127.0.0.1", db_port=3306, db_database="gofans", db_charset="utf8mb4", log_level='debug')

    usuarios = conn.usuarios.include("idolos, fans").inner("idolos", "fans").groupby("usuarios.id").all

    print(json.dumps(usuarios.toJSON(), indent=14))

    conn.close()

if __name__ == "__main__":
    main(sys.argv)
