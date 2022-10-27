import json
import sys
import requests

request = requests.get("https://raw.githubusercontent.com/ant1kdream/g42-qa-test-task/main/elastic_data.json")
request_text = request.text
data = json.loads(request_text)

def get_validate ():
    hitsdata = data['hits']['hits']
    for indexdata in hitsdata:
        source = indexdata['_source']

        index_id = indexdata['_id']
        if index_id == '':
            index_id = "No data found"

        category = source['category']
        for category_item in category:

            currency = source['currency']
            if currency == '':
                currency = "No data found"

            c_firstname = source['customer_first_name']
            if c_firstname == '':
                c_firstname = "No data found"

            c_fullname = source['customer_full_name']
            if c_fullname == '':
                c_fullname = "No data found"

            c_gender = source['customer_gender']
            if c_gender == '':
                c_gender = "No data found"

            c_id = source['customer_id']
            if c_id == '':
                c_id = "No data found"

            c_lstname = source['customer_last_name']
            if c_lstname == '':
                c_lstname = "No data found"

            c_phone = source['customer_phone']
            if c_phone == '':
                c_phone = "No data found"

            c_email = source['email']
            if c_email == '':
                c_email = "No data found"

            manufacturer = source['manufacturer']
## Write customer details to a file 'Customer_Detail_File' - here checking if any node value is missing , if yes add the same in customer details .

            Customer_Detail_File = sys.stdout
            sys.stdout = open("Customer_details.txt", 'a')

            print("  Customer Id    :", c_id, '\n'," First Name     :", c_firstname, '\n', " Full Name      :", c_fullname, '\n', " Category       :", category, '\n', " Email          :", c_email, '\n', " Customer Phone :", c_phone, '\n', " Currency       :", currency, '\n', " manufacturer   :", manufacturer, '\n', '\n')
            sys.stdout = Customer_Detail_File

            for manufacturer in manufacturer:
                orderdate = source['order_date']
                orderid = source['order_id']
                products = source['products']
                for pricedetails in products:

                    baseprice = pricedetails['base_price']
                    if baseprice == '':
                        baseprice = "No data found"

                    d_percentage = pricedetails['discount_percentage']
                    if d_percentage == '':
                        d_percentage = "No data found"

                    quantity = pricedetails['quantity']
                    if quantity == '':
                        quantity = "No data found"

                    product_id = pricedetails['product_id']
                    if product_id == '':
                        product_id = "No data found"

                    taxless_price = pricedetails['taxless_price']
                    if taxless_price == '':
                        taxless_price = "No data found"

                    created_on = pricedetails['created_on']
                    if created_on == '':
                        created_on = "No data found"

                    product_name = pricedetails['product_name']
                    if product_name == '':
                        product_name = "No data found"

                    price = pricedetails['price']
                    if price == '':
                        price = "No data found"

                    geoip = source['geoip']
                    if geoip == '':
                        geoip = "No data found"

                    for country_iso_code in geoip:

                        c_iso_code = geoip['country_iso_code']
                        if c_iso_code == '':
                            c_iso_code = "No data found"

                    Product_Detail_File = sys.stdout
                    sys.stdout = open("Product_details.txt", 'a')

                    print( "  Base Price          :", baseprice, '\n', " Discount Percentage :",
        d_percentage, '\n', " Quantity            :", quantity, '\n', " Product Id          :", product_id, '\n',
                          " Tax less Price      :", taxless_price, '\n', " Created on          :", created_on, '\n', " Order Date          :", orderdate, '\n' "  Order Id            :", orderid, '\n' "  Product Name        :",
                          product_name, '\n', " Price               :",
                          price, '\n', " Geoip country code  :",
                          c_iso_code, '\n', '\n')
                    sys.stdout = Product_Detail_File
get_validate()


hitsdata = data['hits']['hits']
Jsonfile = json.dump([data], open('file.json', "w"), indent=4)

def get_validate (values):
    json.dump([values], open('data.json', "w"), indent=4)

for data in hitsdata:
    get_validate(data)

# Function to validate the set of node under index node.

def validatejsontext(jsontext):
    try:
        json.loads(jsontext)
    except ValueError as err:
        print(err)
        return False
    return True
jsondata=open('data.json','r')
jsontext=jsondata.read()
print("Json nodes validation Result :  ", '\n', "         Given Json data of each transactions records are ", validatejsontext(jsontext))


# Function to validate the entite Json data under hits node.

def validateJsonFile(jsonfile):
    try:
        json.load(jsonfile)
    except ValueError as err:
        print(err)
        return False
    return True
jsonfile=open('file.json','r')
jsonfile=jsonfile.read()

print("Json file validation Result :  ", '\n', "         Given Json data file and structure are ", validatejsontext(jsonfile))
