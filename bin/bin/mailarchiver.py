#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mailbox
import dateutil.parser as parser
from datetime import *
from dateutil.relativedelta import *

box = mailbox.Maildir('~/.mail_ufrgs/INBOX')
archive = mailbox.Maildir('~/.mail_ufrgs_archive/INBOX')

now = datetime.now()
limit = now+relativedelta(months=-6)

box.lock()
archive.lock()
for key, msg in box.iteritems():
    try:
        date = parser.parse(msg['date']).replace(tzinfo=None)
        if (date < limit):
            print('Moving', key)
            archive.add(msg)
            box.remove(key)
    except:
        print('Something went wrong', key)

box.flush()
box.close()
archive.flush()
archive.close()
