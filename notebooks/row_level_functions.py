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
                (5, 'Peter', 'USA', 0),
                (6, 'Jessica', 'USA', 1000);
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
    return


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
            (5, 'Carol', 'Baker', 'Sales', '1982-02-11', 'F', 55000, 3),
            (6, 'Jessica', 'Pegula', 'Marketing', '1981-09-16', 'F', 60000, 3);
        """
    )
    return


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
    return


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
    mo.md(r"""# `CONCAT`""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: concatene as colunas `first_name` e `country` em uma única coluna.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
        	id AS customerId,
            CONCAT(first_name, ' | ',country) AS nameAndCountry,
            score
        FROM customers;
        """
    )
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT
        	id AS customerId,
            CONCAT_WS(' | ', first_name, country, score) AS nameCountryAndScore
        FROM customers;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `UPPER` & `LOWER`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 2**: converta `first_name` para minúsculas.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT
            id,
            LOWER (first_name)
        FROM customers;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `TRIM`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 3**: encontre consumidores com espaços a mais no nome.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT
            first_name,
            (LEN(first_name) - LEN(TRIM(first_name))) AS has_spaces,
        FROM customers;
        """
    )
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
            first_name AS firstName,
            (LEN(first_name) - LEN(TRIM(first_name))) AS numberOfSpaces
        FROM customers
        WHERE first_name != TRIM(first_name)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `LEFT` & `RIGHT`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 4**: retorne os dois primeiros caracteres do país.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
            first_name AS nome, 
            LEFT(country, 2) AS pais 
        FROM customers;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `SUBSTRING`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 5**: remova a primeira letra dos primeiros nomes.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT
            SUBSTRING(first_name, 2, LEN(first_name))
        FROM customers;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Funções de Extração""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 6**: quantas ordens foram feitas por ano?""")
    return


@app.cell
def _(mo, orders_full):
    _df = mo.sql(
        f"""
        SELECT 
            YEAR(orderdate) AS ano,
            COUNT(*) AS n_of_orders 
        FROM orders_full
        GROUP BY ano;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 7**: quais pedidos foram feitos em fevereiro? """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DESCRIBE orders_full;
        """
    )
    return


@app.cell
def _(mo, orders_full):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM orders_full
        WHERE MONTH(orderdate) = 2;
        """
    )
    return


if __name__ == "__main__":
    app.run()
