#
def mask_pii(record):
    record['FirstName'] = 'XXXXX'
    record['LastName'] = 'XXXXX'
    record['Email'] = 'masked@example.com'
    return record
