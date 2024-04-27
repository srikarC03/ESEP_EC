
class NoOngoingTransactionError(Exception):
    def __init__(self, message="No transaction is currently in progress"):
        self.message = message
        super().__init__(self.message)

class DataBase:
    def __init__(self):
        self.curr_db = dict()
        self.tmp_db = dict()
        self.transaction = False
    
    def put(self,key, val):
        if self.transaction:
            self.tmp_db[key] = val
        else:
            raise NoOngoingTransactionError()

    def get(self,key):
        return self.curr_db.get(key,None)
    
    def begin_transaction(self):
        self.transaction = True
    
    def commit(self):
        if self.transaction:
            self.curr_db = self.tmp_db.copy()
        else:
            raise NoOngoingTransactionError()

    def rollback(self):
        if self.transaction:
            self.tmp_db = self.curr_db.copy()
        else:
            raise NoOngoingTransactionError()