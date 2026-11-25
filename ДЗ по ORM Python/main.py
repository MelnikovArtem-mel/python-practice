import json
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from mmodels import create_tables, Publisher, Book, Shop, Stock, Sale
DSN = 'postgresql+psycopg2://postgres@localhost:5432/DZ_ORM'
engine = create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

user_input = input('Введите имя или ID издателя: ')

if user_input.isdigit():
    publisher_filter = Publisher.id == int(user_input)
else:
    publisher_filter = Publisher.name == user_input

stmt = (
    select(Book.title, Shop.name, Sale.price, Sale.date_sale)
    .select_from(Sale)
    .join(Sale.stock)
    .join(Stock.book)
    .join(Stock.shop)
    .join(Book.publisher)
    .where(publisher_filter)
    .order_by(Sale.date_sale.desc())
)

results = session.execute(stmt).all()
for title, shop_name, price, date_sale in results:
    print(f"{title} | {shop_name} | {price} | {date_sale.strftime('%d-%m-%Y')}")



session.close()