from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import Pool
from trytond.rpc import RPC
from trytond.transaction import Transaction

class A(ModelSQL, ModelView):
    "A"
    __name__ = 'test.a'
    name = fields.Char("Name")

class B(ModelSQL, ModelView):
    "B"
    __name__ = 'test.b'

    name = fields.Char("Name")
    ref_a = fields.Many2One("test.a", "A")

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls.__rpc__.update({'txn': RPC(check_access=False, readonly=False)})

    @classmethod
    def txn(cls):
        B = Pool().get('test.b');
        b, = B.search([])
        with Transaction().new_transaction(autocommit=False, readonly=False) as transaction:
            b1 = B(b.id)
            A = Pool().get("test.a")
            a = A(name=b.name)
            a.save()
            b1.ref_a = a
            b1.save()
            transaction.commit()
        

    
            
        
