from login import login_sap
from zrwbe import open_transaction, fill_parameters

print("Starting automation...")

login_sap()

session = open_transaction()

fill_parameters(session)

print("Done.")