class TransactionException(Exception):
    def __str__(self):
        return "トランザクション中エラー発生"