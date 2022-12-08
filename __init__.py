# This file is part papyrus module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import test_txn

module = 'test_transaction'

def register():
    Pool.register(      
        test_txn.A,
        test_txn.B,
        module=module, type_='model')
