# This file is part papyrus module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import doctest_teardown, doctest_checker

        
def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(doctest.DocFileSuite
                   ("scenario_txn.rst",
                    tearDown= doctest_teardown,
                    encoding= 'utf-8',
                    checker= doctest_checker,
                    optionflags= doctest.REPORT_ONLY_FIRST_FAILURE
                    ))
    return suite
