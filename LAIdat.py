import codecs

class InvoiceHeaderLine(object):

    fields = (('type', 1), # Fixed
              ('customer_no', 8),
              ('customer_name', 50),
              ('address', 50),
              ('post_code', 50),
              ('contact_person', 50),
              ('currency', 3),
              ('invoice_no', 8),
              ('delivery_date', 8),
              ('invoice_date', 8),
              ('placeholder1', 3),
              ('comment', 30), # Not in use
              ('invoice_type', 1), # Fixed
              ('reference_no', 24),
              ('customer_class', 20),
              ('email', 50),
              ('due_date', 8),
              ('iban', 34),
              ('bic', 20),
              ('operator', 20),
              ('invoice_address', 100), # Not in use
              ('ship_name', 50),
              ('ship_address_1', 50), # Not in use
              ('ship_address_2', 100), # Not in use
              ('ship_post_code', 50),
              ('ship_phone', 20),
              ('ship_fax', 20),
              ('ship_contact_person', 20),
              ('ship_mobile_phone', 20),
              ('ship_email', 255),
              ('chn', 20),
              ('net_address', 100),
              ('ovt_code', 50),
              ('contact_email', 255), # Not in use
              ('comments_1', 255),
              ('comments_2', 255),
              ('comments_3', 255),
              ('booking_date', 8),
              ('construction_key', 35),
              )

    def __init__(self):
        for field_name, width in self.fields:
            setattr(self, field_name, '')
        self.type = '8'
        self.invoice_type = '0'

    def __str__(self):
        return ''.join([getattr(self, field_name).ljust(width)[:width]
                        for field_name, width in self.fields])

class InvoiceLine(object):

    fields = (('type', 1),
              ('code', 20),
              ('description', 50),
              ('quantity', 7),
              ('unit_price', 9),
              ('discount_percent', 5),
              ('total', 9),
              ('vat_number', 1),
              ('account', 6),
              ('cost_account_1', 6),
              ('cost_account_2', 6),
              ('vat_sum', 9),
              ('cost_account_3', 10),
              ('construction_key', 35),
              )

    def __init__(self):
        for field_name, width in self.fields:
            setattr(self, field_name, '')
        self.type = '4'

    def __str__(self):
        return ''.join([getattr(self, field_name).ljust(width)[:width]
                        for field_name, width in self.fields])

class InfoLine(object):

    fields = (('type', 1),
              ('text', 80),
              )

    def __init__(self):
        for field_name, width in self.fields:
            setattr(self, field_name, '')
        self.type = '2'

    def __str__(self):
        return ''.join([getattr(self, field_name).ljust(width)[:width]
                        for field_name, width in self.fields])
