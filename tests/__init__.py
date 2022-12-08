# This file is part papyrus module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.test_transaction.tests.test_test_transaction import suite
except ImportError:
    from .test_test_transaction import suite

__all__ = ['suite']
