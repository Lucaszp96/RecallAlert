import os

import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Capstone.settings")

django.setup()

df = pd.read_excel("./products_2.xlsx")

cat_names = [
    'Babies and kids',
    'Home and living',
    'Health and lifestyle',
    'Electronics and technology',
    'Outdoor',
    'Clothing and accessories',
    'Transport',
    'Food and groceries',
    'Industrial,  business and building',
    'Agricultural and veterinary',
    'Chemicals',
    'Gas',
]

com_names = [
    "Children",
    "Household",
    "Healthy life & Beauty",
    "Digital products",
    "Adventure & Travel equipment",
    "Clothing",
    "Transportation",
    "Food & Drinks",
    "Industrial products & Office",
    "Agriculture and Livestock",
    "Medicinal & Chemical",
    "Other",
]


def category_sql():

    for idx, name in enumerate(com_names, start=1):
        Category.objects.create(id=idx, title=name)
    print("Category to sql down!")


def product_sql():
    for _, row in df.iterrows():
        cat = row['Product category'].strip()
        cat = com_names[cat_names.index(cat)]
        product_name = row["Product name"]
        img = row["Picture address"]
        sn = row["PRA number"]
        content = row["Product description"]
        defects = row[" Defects"]
        hazards = row["Hazards"]
        consumers = row["Consumers"]
        supplier = row["Supplier"]
        traders = row["Traders "]
        sold_venues = row["Sold venues"]
        avaiable_sale_date = row["Available sale date"]
        category = Category.objects.filter(title=cat).first()
        Product.objects.create(product_name=product_name,
                               img=img,
                               sn=sn,
                               content=content,
                               defects=defects,
                               hazards=hazards,
                               consumers=consumers,
                               supplier=supplier,
                               traders=traders,
                               sold_venues=sold_venues,
                               avaiable_sale_date=avaiable_sale_date,
                               category_name=cat,
                               category_id=category.id)
    print("Product导入成功!")


def main():
    if Category.objects.count() == 0:
        category_sql()
        print("Category导入成功!")
    else:
        print("Category is already in db")


if __name__ == "__main__":
    from login.models import Category, Product
    main()
    product_sql()
