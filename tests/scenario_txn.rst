>>> from proteus import Model
>>> from trytond.tests.tools import activate_modules, set_user


>>> config = activate_modules('test_transaction')

>>> User = Model.get('res.user')
>>> user_admin, = User.find([('login', '=', 'admin')])
>>> set_user(user_admin)

>>> A = Model.get('test.a')
>>> B = Model.get('test.b')
>>> b = B(name="test")
>>> b.save()
>>> b = B(b.id)
>>> B.txn(config.context)
>>> b = B(b.id)
>>> b.ref_a.id > 0
True
