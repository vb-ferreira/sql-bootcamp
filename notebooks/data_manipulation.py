import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Create Tables**""")
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
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS persons;

        CREATE TABLE persons (
            id INT NOT NULL,
            person_name VARCHAR(50) NOT NULL,
            birth_date DATE,
            phone VARCHAR(15) NOT NULL,
            CONSTRAINT pk_person PRIMARY KEY (id)
        )
        """
    )
    return (persons,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `INSERT`""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: Insira novas linhas passando os valores""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        INSERT INTO customers (id, first_name, country, score)
        VALUES 
            (6, 'Anna', 'USA', NULL),
            (7, 'Sam', NULL, 100)
        """
    )
    return


@app.cell(hide_code=True)
def task2(mo):
    mo.md(r"""## **Task 2**: Insira dados usando o `SELECT`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Copie dados da tabela `customers` para a tabela `persons`.""")
    return


@app.cell
def _(customers, mo, persons):
    _df = mo.sql(
        f"""
        INSERT INTO persons (id, person_name, birth_date, phone)
        SELECT
            id,
            first_name,
            NULL,
            'Unknow'
        FROM customers

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `UPDATE`""")
    return


@app.cell(hide_code=True)
def task3(mo):
    mo.md(r"""## **Task 3**: Alterando valores em uma linha""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Altere o `score` do consumidor com `id` 6 para zero.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        UPDATE customers
        SET score = 0
        WHERE id = 6;
        """
    )
    return


@app.cell(hide_code=True)
def task4(mo):
    mo.md(r"""## **Task 4**: Alterando mais de um valor """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Atualize o país do consumidor com `id` 7 para `UK` e seu `score` para zero.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        UPDATE customers
        SET country = 'UK',
        	score = 0
        WHERE id = 7
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `DELETE`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 5**: Excluindo registros""")
    return


@app.cell(hide_code=True)
def task5(mo):
    mo.md(r"""Apague os registros com `id > 5`.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        DELETE FROM customers
        WHERE id > 5
        """
    )
    return


if __name__ == "__main__":
    app.run()
