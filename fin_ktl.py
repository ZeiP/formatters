import codecs

class ReferenceTransferLine(object):

    fields = (('type', {'width': 1, 'required': True, 'just': 'r', 'filler': '0'}), # 3 = reference payment, 5 = direct withdrawal, 7 = reference withdrawal
              ('account_no', {'width': 14, 'required': True, 'just': 'r', 'filler': '0'}),
              ('booking_date', {'width': 6, 'required': True, 'just': 'r', 'filler': '0'}), # yymmdd
              ('payment_date', {'width': 6, 'required': True, 'just': 'r', 'filler': '0'}), # yymmdd
              ('archive_id', {'width': 16, 'required': True, 'just': 'l', 'filler': ' '}),
              ('reference_no', {'width': 20, 'required': True, 'just': 'r', 'filler': '0'}),
              ('payer', {'width': 12, 'required': True, 'just': 'l', 'filler': ' '}),
              ('currency_code', {'width': 1, 'required': True, 'just': 'l', 'filler': ' '}), # 1 = EUR
              ('name_source', {'width': 1, 'required': False, 'just': 'l', 'filler': ' '}), # A = customer-given, J = bank register based on account no, K = clerk-given
              ('amount', {'width': 10, 'required': True, 'just': 'r', 'filler': '0'}),
              ('event_type', {'width': 1, 'required': True, 'just': 'r', 'filler': '0'}), # 0 = normal, 1 = redress
              ('event_source', {'width': 1, 'required': False, 'just': 'l', 'filler': ' '}), # A = from customer, J = bank system, K = from clerk
              ('return_code', {'width': 1, 'required': False, 'just': 'l', 'filler': ' '}), # Used only for direct withdrawals
              )

    def __init__(self):
        for field_name, width in self.fields:
            setattr(self, field_name, '')
        self.type = '3'
        self.currency_code = '1'
        self.event_type = '0'

    def __str__(self):
        cont = []
        for field_name, opt in self.fields:
            if opt['just'] == 'l':
                cont.append(getattr(self, field_name).ljust(opt['width'], opt['filler'])[:opt['width']])
            elif opt['just'] == 'r':
                cont.append(getattr(self, field_name).rjust(opt['width'], opt['filler'])[:opt['width']])
        return ''.join(cont)

if __name__ == "__main__":
    line = ReferenceTransferLine()
    line.account_no = '112233987654321'
    line.booking_date = '170901'
    line.payment_date = '170901'
    line.archive_id = 'asdfasdfasdfasdf'
    line.reference_no = '5555'
    line.payer = 'ESIMERKKI ESSI'
    amount = 1.5
    line.amount = str(int(amount * 100))

    print(line)
