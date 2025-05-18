# Sample data insertion
from model import Inventory, Product, Sale, SessionLocal


def insert_sample_data():
    db = SessionLocal()
    try:
        # Insert sample products
        product1 = Product(name="Laptop", price=1200.00, category="Electronics")
        product2 = Product(name="Sneakers", price=80.00, category="Footwear")
        product3 = Product(name="Coffee Mug", price=12.50, category="Kitchenware")

        db.add_all([product1, product2, product3])
        db.commit()

        # Refresh to get generated product IDs
        db.refresh(product1)
        db.refresh(product2)
        db.refresh(product3)

        # Insert sample sales
        sale1 = Sale(product_id=product1.id, total_amount=1200.00, sale_date='2024-05-01')
        sale2 = Sale(product_id=product2.id, total_amount=160.00, sale_date='2024-05-02')  # bought 2 pairs
        sale3 = Sale(product_id=product3.id, total_amount=25.00, sale_date='2024-05-03')   # bought 2 mugs

        db.add_all([sale1, sale2, sale3])
        db.commit()

        # Insert sample inventory changes
        inventory1 = Inventory(product_id=product1.id, quantity_change=10, quantity=10)
        inventory2 = Inventory(product_id=product2.id, quantity_change=20, quantity=18)  # 2 sold
        inventory3 = Inventory(product_id=product3.id, quantity_change=30, quantity=28)  # 2 sold

        db.add_all([inventory1, inventory2, inventory3])
        db.commit()

        print("Sample data inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error inserting sample data: {e}")
    finally:
        db.close()

# Call the function to insert sample data
insert_sample_data()
