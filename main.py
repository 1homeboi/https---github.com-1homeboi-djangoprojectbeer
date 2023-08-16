from db.models import Company, Beer, Sales,SalesBeer,Inventory, Location, Storage,Store,Packaging
import json

def insert_company():
    with open('company.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            Company.objects.create(
                company_title=item['company title'],
                country=item['country']
            )
#insert_company()

def insert_beer():
    with open('beer.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            storage = Storage.objects.get(pk=item['storage_id'])
            company = Company.objects.get(pk=item['company_id'])
            packaging = Packaging.objects.get(pk=item['packaging_id'])
            Beer.objects.create(
                beer_title=item['sku_title'],
                price=item['price'],
                company_id = company,
                expiry_date=item['expiry_date'],
                volume=item['volume'],
                storage_id = storage,
                Packaging_id=packaging
            )

#insert_beer()

def insert_storage():
    with open('storage.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            Storage.objects.create(
                storage_title=item['storage_title'],
                address=item['address']
            )
#insert_storage()

def insert_packaging():
    with open('packaging.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            Packaging.objects.create(
                packaging_title=item['packaging_title'],
                capacity=item['capacity']
            )
#insert_packaging()

def insert_store():
    with open('store.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            location_id = Location.objects.get(pk=item['location_id'])
            Store.objects.create(
                store_title=item['store_title'],
                location_id=location_id
            )
# insert_store ()
def insert_location():
    with open('location.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            Location.objects.create(
                city=item['city'],
                district=item['district']
            )
# insert_location()
def insert_inventory():
    with open('inventory.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            beer_id = Beer.objects.get(pk=item['beer_id'])
            storage_id = Storage.objects.get(pk=item['storage_id'])
            Inventory.objects.create(
                beer_id=beer_id,
                storage_id=storage_id,
                quantity=item['quantity']
            )
# insert_inventory()
def insert_sales():
    with open('sales.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            store_id = Store.objects.get(pk=item['store_id'])
            beer_id = Beer.objects.get(pk=item['beer_id'])
            Sales.objects.create(
                quantity=item['quantity'],
                sales_date=item['sales_date'],
                store_id=store_id,
                beer_id = beer_id,
                total_amount=item['total_amount']
            )
# insert_sales()
def insert_salesbeer():
    with open('salesbeer.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            beer_id = Beer.objects.get(pk=item['beer_id'])
            sales_id = Sales.objects.get(pk=item['sales_id'])
            SalesBeer.objects.create(
                beer_id=beer_id,
                sales_id=sales_id
            )
# insert_salesbeer()

#Select all from Beer
allobjects = Beer.objects.all()
#print(allobjects)
# Пиво сделанное определенной компанией
anheuser_busch_beers = Beer.objects.filter(company_id__company_title='Anheuser-Busch InBev')
#print (anheuser_busch_beers)

#Продажи определенного магазина.
store_name = "The Beer Store"
store_sales = Sales.objects.filter(store_id__store_title=store_name)
#print(store_sales)

#Продажи определенного пива
beer_name = "Sierra Nevada Pale Ale"
beer_sales = Sales.objects.filter(beer_id__beer_title=beer_name)
#print(beer_sales)

#кол-во пива на складе
beer_name = "Bud Light"
storage_title = "Main Warehouse"
inventory = Inventory.objects.filter(beer_id__beer_title=beer_name, storage_id__storage_title=storage_title)
#print(inventory)