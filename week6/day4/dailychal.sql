-- Instructions
-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
CREATE TABLE product_orders (
    id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    customer_address VARCHAR(100) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    items_id INTEGER REFERENCES items(id)
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- add 5 random intems in the product orders and items table
INSERT INTO
    items (name, price)
VALUES
    ('item1', 10.00),
    ('item2', 20.00),
    ('item3', 30.00),
    ('item4', 40.00),
    ('item5', 50.00);

INSERT INTO
    product_orders (
        order_date,
        customer_name,
        customer_address,
        customer_phone,
        items_id
    )
VALUES
    (
        '2019-01-01',
        'customer1',
        'address1',
        'phone1',
        1
    ),
    (
        '2019-01-02',
        'customer2',
        'address2',
        'phone2',
        2
    ),
    (
        '2019-01-03',
        'customer3',
        'address3',
        'phone3',
        3
    ),
    (
        '2019-01-04',
        'customer4',
        'address4',
        'phone4',
        4
    ),
    (
        '2019-01-05',
        'customer5',
        'address5',
        'phone5',
        5
    );

-- add 3 items in each product order
INSERT INTO
    product_orders (
        order_date,
        customer_name,
        customer_address,
        customer_phone,
        items_id
    )
VALUES
    (
        '2019-01-01',
        'customer1',
        'address1',
        'phone1',
        1
    ),
    (
        '2019-01-01',
        'customer1',
        'address1',
        'phone1',
        2
    ),
    (
        '2019-01-01',
        'customer1',
        'address1',
        'phone1',
        3
    ),
    (
        '2019-01-02',
        'customer2',
        'address2',
        'phone2',
        1
    ),
    (
        '2019-01-02',
        'customer2',
        'address2',
        'phone2',
        2
    ),
    (
        '2019-01-02',
        'customer2',
        'address2',
        'phone2',
        3
    ),
    (
        '2019-01-03',
        'customer3',
        'address3',
        'phone3',
        1
    ),
    (
        '2019-01-03',
        'customer3',
        'address3',
        'phone3',
        2
    ),
    (
        '2019-01-03',
        'customer3',
        'address3',
        'phone3',
        3
    ),
    (
        '2019-01-04',
        'customer4',
        'address4',
        'phone4',
        1
    ),
    (
        '2019-01-04',
        'customer4',
        'address4',
        'phone4',
        2
    ),
    (
        '2019-01-04',
        'customer4',
        'address4',
        'phone4',
        3
    ),
    (
        '2019-01-05',
        'customer5',
        'address5',
        'phone5',
        1
    ),
    (
        '2019-01-05',
        'customer5',
        'address5',
        'phone5',
        2
    ),
    (
        '2019-01-05',
        'customer5',
        'address5',
        'phone5',
        3
    );

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order. 
-- Create a function that returns the total price for a given order.
CREATE FUNCTION total_price (order_id INTEGER) RETURNS DECIMAL(10, 2) AS $ $ DECLARE total DECIMAL(10, 2);

BEGIN
SELECT
    SUM(price) INTO total
FROM
    items
WHERE
    items.id = product_orders.items_id;

RETURN total;

END;

$ $ LANGUAGE plpgsql;

-- run the function to get the total price for order 1
SELECT
    total_price(1);