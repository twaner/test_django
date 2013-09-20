#!/bin/bash

MYSQLREPOSITORY="/usr/local/mysql/data"
DB="djdb"
GITREPOSITORY="/Users/taiowawaner/Documents/test_django/booksite/db"

# GO TIME

cp -R  $MYSQLREPOSITORY/$DB.sql $GITREPOSITORY/

