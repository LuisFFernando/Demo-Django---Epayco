import pyepayco.epayco as epayco
import json

# xxxx
apiKey = ""
privateKey = ""
lenguage = "ES"
test = False
options = {"apiKey": apiKey, "privateKey": privateKey,
           "test": test, "lenguage": lenguage}

objepayco = epayco.Epayco(options)

#  CREAR TARJETA --------------------------------------------------------------------------


def create_card():
    credit_info = {
        "card[number]": "4575623182290326",
        "card[exp_year]": "2019",
        "card[exp_month]": "12",
        "card[cvc]": "123"
    }

    token = objepayco.token.create(credit_info)
    print(token['data']['id'], token['data']['status'])
    print('----------------------------------------------------')
    # print(token)
    # return token

# create_card()

# CREAR CLIENTE ----------------------------------------------------------------------------
# -----------------------Visa
# Franquicia: Visa
# Numero: 4575623182290326
# Fecha Expiración: 12/19
# card : LdPck67HvqMKRyDby
# cliente : WmrnjKkvCHY5YgMFm
# -----------------------Mastercard
# Franquicia: Mastercard
# Numero: 5170394490379427
# Fecha Expiración: 12/19
# card: PZbNHzsZbySNbpNXY
# customer :WmrnjKkvCHY5YgMFm
#  --------------------- American Express
# Franquicia: American Express
# Numero: 373118856457642
# Fecha Expiración: 12/19
# Cvv: 123
# card: imydM2hbwmXKManZB
# customer:WmrnjKkvCHY5YgMFm


def customer():
    customer_info = {
        "token_card": "imydM2hbwmXKManZB",
        "name": "Demo juan",
        "email": "juan@payco.co",
        "phone": "123456789",
        "default": True
    }
    customer = objepayco.customer.create(customer_info)
    print(customer)

# customer()


# # def listar_customer():
# customer = objepayco.customer.get("q5CRTwbAmk3xFx28D")
# # customers = objepayco.customer.getlist()
# # # cc=json.loads(customer)
# print(customer)
# # print(customers)

# listar_customer()


def pya_card():

    payment_info = {
        "token_card": "imydM2hbwmXKManZB",
        "customer_id": "WmrnjKkvCHY5YgMFm",
        "doc_type": "CC",
        "doc_number": "1000000",
        "name": "Demo juan",
        "last_name": "Demo",
        "email": "demo@email.com",
        "ip": "192.198.2.114",
        "bill": "OR-1234",
        "description": "Test Payment",
        "value": "125000",
        "tax": "7000",
        "tax_base": "100000",
        "currency": "COP",
        "dues": "1"
    }
    pay = objepayco.charge.create(payment_info)
    print(pay)

# pya_card()

#  PAGOS PSE-------------------------------------------------------------------------------


def pse_demo():
    pse_info = {
        "bank": "1007",
        "invoice": "14720780000",
        "description": "xxxx",
        "value": "20000",
        "tax": "0",
        "tax_base": "0",
        "currency": "COP",
        "type_person": "0",
        "doc_type": "CC",
        "doc_number": "1258552",
        "name": "TEST EPAYCO",
        "last_name": "test",
        "email": "epayco@dominio.com",
        "country": "CO",
        "cell_phone": "3010000001",
        "ip": "200.122.254.75",
        "url_response": "https://tudominio.com/respuesta.php",
        "url_confirmation": "https://tudominio.com/confirmacion.php",
        "method_confirmation": "GET",
    }

    pse = objepayco.bank.create(pse_info)
    print(pse)


# pse_demo()


def response_pse():
    pse = objepayco.bank.pseTransaction("459478253")
    print(pse)


# response_pse()

cadena = "LdPck67HvqMKRyDby"
x = cadena[12:17]
# d = len(cadena)
print(x)
# print(d)

# customer=objectoepyaco.customer.get(id del customer)
