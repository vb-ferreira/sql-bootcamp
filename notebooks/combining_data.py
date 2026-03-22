import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Crate Tables**""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS customers;

        CREATE TABLE customers (
            id INT NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            country VARCHAR(50),
            score INT,
            CONSTRAINT pk_customers PRIMARY KEY (id)
        );

        INSERT INTO customers (id, first_name, country, score) 
        VALUES  (1, 'Maria', 'Germany', 350),
                (2, ' John', 'USA', 900),
                (3, 'Georg', 'UK', 750),
                (4, 'Martin', 'Germany', 500),
                (5, 'Peter', 'USA', 0);
        """
    )
    return (customers,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS orders;

        CREATE TABLE orders (
            order_id INT NOT NULL,
            customer_id INT NOT NULL,
            order_date DATE,
            sales INT,
            CONSTRAINT pk_orders PRIMARY KEY (order_id)
        );

        INSERT INTO orders (order_id, customer_id, order_date, sales) 
        VALUES (1001, 1, '2021-01-11', 35),
               (1002, 2, '2021-04-05', 15),
               (1003, 3, '2021-06-18', 20),
               (1004, 6, '2021-08-31', 10);
        """
    )
    return (orders,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS employees;

        CREATE TABLE employees (
            employeeid INT PRIMARY KEY,
            firstname VARCHAR(50),
            lastname VARCHAR(50),
            department VARCHAR(50),
            birthdate DATE,
            gender CHAR(1),
            salary INT,
            managerid INT
        );

        INSERT INTO employees VALUES
            (1, 'Frank', 'Lee', 'Marketing', '1988-12-05', 'M', 55000, NULL),
            (2, 'Kevin', 'Brown', 'Marketing', '1972-11-25', 'M', 65000, 1),
            (3, 'Mary', NULL, 'Sales', '1986-01-05', 'F', 75000, 1),
            (4, 'Michael', 'Ray', 'Sales', '1977-02-10', 'M', 90000, 2),
            (5, 'Carol', 'Baker', 'Sales', '1982-02-11', 'F', 55000, 3);
        """
    )
    return (employees,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS products;

        CREATE TABLE products (
            productid INT PRIMARY KEY,
            product VARCHAR(50),
            category VARCHAR(50),
            price INT
        );

        INSERT INTO products VALUES
            (101, 'Bottle', 'Accessories', 10),
            (102, 'Tire', 'Accessories', 15),
            (103, 'Socks', 'Clothing', 20),
            (104, 'Caps', 'Clothing', 25),
            (105, 'Gloves', 'Clothing', 30);
        """
    )
    return (products,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS orders_full;

        CREATE TABLE orders_full (
            orderid INT PRIMARY KEY,
            productid INT,
            customerid INT,
            salespersonid INT,
            orderdate DATE,
            shipdate DATE,
            orderstatus VARCHAR(50),
            shipaddress VARCHAR(255),
            billaddress VARCHAR(255),
            quantity INT,
            sales INT,
            creationtime TIMESTAMP
        );

        INSERT INTO orders_full VALUES
            (1, 101, 2, 3, '2025-01-01', '2025-01-05', 'Delivered', '9833 Mt. Dias Blv.', '1226 Shoe St.', 1, 10, '2025-01-01 12:34:56'),
            (2, 102, 3, 3, '2025-01-05', '2025-01-10', 'Shipped', '250 Race Court', NULL, 1, 15, '2025-01-05 23:22:04'),
            (3, 101, 1, 5, '2025-01-10', '2025-01-25', 'Delivered', '8157 W. Book', '8157 W. Book', 2, 20, '2025-01-10 18:24:08'),
            (4, 105, 1, 3, '2025-01-20', '2025-01-25', 'Shipped', '5724 Victory Lane', '', 2, 60, '2025-01-20 05:50:33'),
            (5, 104, 2, 5, '2025-02-01', '2025-02-05', 'Delivered', NULL, NULL, 1, 25, '2025-02-01 14:02:41'),
            (6, 104, 3, 5, '2025-02-05', '2025-02-10', 'Delivered', '1792 Belmont Rd.', NULL, 2, 50, '2025-02-06 15:34:57'),
            (7, 102, 1, 1, '2025-02-15', '2025-02-27', 'Delivered', '136 Balboa Court', '', 2, 30, '2025-02-16 06:22:01'),
            (8, 101, 4, 3, '2025-02-18', '2025-02-27', 'Shipped', '2947 Vine Lane', '4311 Clay Rd', 3, 90, '2025-02-18 10:45:22'),
            (9, 101, 2, 3, '2025-03-10', '2025-03-15', 'Shipped', '3768 Door Way', '', 2, 20, '2025-03-10 12:59:04'),
            (10, 102, 3, 5, '2025-03-15', '2025-03-20', 'Shipped', NULL, NULL, 0, 60, '2025-03-16 23:25:15');
        """
    )
    return (orders_full,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS orders_archive;

        CREATE TABLE ordersarchive (
            orderid INT,
            productid INT,
            customerid INT,
            salespersonid INT,
            orderdate DATE,
            shipdate DATE,
            orderstatus VARCHAR(50),
            shipaddress VARCHAR(255),
            billaddress VARCHAR(255),
            quantity INT,
            sales INT,
            creationtime TIMESTAMP
        );

        INSERT INTO ordersarchive VALUES
            (1, 101, 2, 3, '2024-04-01', '2024-04-05', 'Shipped', '123 Main St', '456 Billing St', 1, 10, '2024-04-01 12:34:56'),
            (2, 102, 3, 3, '2024-04-05', '2024-04-10', 'Shipped', '456 Elm St', '789 Billing St', 1, 15, '2024-04-05 23:22:04'),
            (3, 101, 1, 4, '2024-04-10', '2024-04-25', 'Shipped', '789 Maple St', '789 Maple St', 2, 20, '2024-04-10 18:24:08'),
            (4, 105, 1, 3, '2024-04-20', '2024-04-25', 'Shipped', '987 Victory Lane', '', 2, 60, '2024-04-20 05:50:33'),
            (4, 105, 1, 3, '2024-04-20', '2024-04-25', 'Delivered', '987 Victory Lane', '', 2, 60, '2024-04-20 14:50:33'),
            (5, 104, 2, 5, '2024-05-01', '2024-05-05', 'Shipped', '345 Oak St', '678 Pine St', 1, 25, '2024-05-01 14:02:41'),
            (6, 104, 3, 5, '2024-05-05', '2024-05-10', 'Delivered', '543 Belmont Rd.', NULL, 2, 50, '2024-05-06 15:34:57'),
            (6, 104, 3, 5, '2024-05-05', '2024-05-10', 'Delivered', '543 Belmont Rd.', '3768 Door Way', 2, 50, '2024-05-07 13:22:05'),
            (6, 101, 3, 5, '2024-05-05', '2024-05-10', 'Delivered', '543 Belmont Rd.', '3768 Door Way', 2, 50, '2024-05-12 20:36:55'),
            (7, 102, 3, 5, '2024-06-15', '2024-06-20', 'Shipped', '111 Main St', '222 Billing St', 0, 60, '2024-06-16 23:25:15');
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `INNER JOIN`""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: Seleciona as linhas presentes nas duas tabelas.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione os consumidores que já fizeram algum pedido.""")
    return


@app.cell
def _(customers, mo, orders):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        INNER JOIN orders
        ON customers.id = orders.customer_id
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `LEFT JOIN`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 2**: Todos os consumidores e ordens correspondentes.""")
    return


@app.cell
def _(customers, mo, orders):
    _df = mo.sql(
        f"""
        SELECT 
            c.first_name,
            c.country,
            o.order_date,
            o.order_id
        FROM customers AS c
        LEFT JOIN orders AS o
        ON c.id = o.customer_id
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `LEFT ANTI JOIN`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 3**: retorne os consumidores que não fizeram pedidos.""")
    return


@app.cell
def _(customers, mo, orders):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM customers AS c
        LEFT JOIN orders as o
        ON c.id = o.customer_id
        WHERE o.customer_id IS NULL
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `FULL ANTI JOIN`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 4**: encontre os clientes que não fizeram pedidos e os pedidos sem clientes.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 5**: retorne todos os consumidores que fizeram algum pedido sem usar o `INNER JOIN`.""")
    return


@app.cell
def _(customers, mo, orders):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM customers AS c
        FULL JOIN orders AS o
        ON c.id = o.customer_id
        WHERE c.id IS NULL OR o.customer_id IS NULL
        """
    )
    return


@app.cell
def _(customers, mo, orders):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM customers AS c
        LEFT JOIN orders AS o
        ON c.id = o.customer_id
        WHERE o.customer_id IS NOT NULL
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Join Multiple Tables""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 6**: retorne todas as ordens, com informações do consumidor, produto e funcionário. Para cada pedido, exiba id, nome do cliente, nome do produto, quantidade, preço e nome do empregado.""")
    return


@app.cell
def _(customers, employees, mo, orders_full, products):
    _df = mo.sql(
        f"""
        SELECT
        	o.orderid AS OrderId,
            o.quantity AS QuantityOrdered,
            c.first_name AS CustomerFirstName,
            p.product AS ProductName,
            p.price AS ProductPrice,
            e.firstname AS EmployeeFirstName,
            e.lastname  AS EmployeeLastName
        FROM orders_full o
        LEFT JOIN customers c
            ON o.customerid = c.id
        LEFT JOIN products p
        	ON o.productid = p.productid
        LEFT JOIN employees e
        	ON o.salespersonid = e.employeeid
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
