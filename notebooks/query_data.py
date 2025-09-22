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

        -- Insert customers data
        INSERT INTO customers (id, first_name, country, score) VALUES
            (1, 'Maria', 'Germany', 350),
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

        -- Insert orders data
        INSERT INTO orders (order_id, customer_id, order_date, sales) VALUES
            (1001, 1, '2021-01-11', 35),
            (1002, 2, '2021-04-05', 15),
            (1003, 3, '2021-06-18', 20),
            (1004, 6, '2021-08-31', 10);
        """
    )
    return (orders,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **SELECT**""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: Selecione todas as colunas""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione todos os dados das tabelas customers e orders.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM customers
        """
    )
    return


@app.cell
def _(mo, orders):
    _df = mo.sql(
        f"""
        SELECT * FROM orders
        """
    )
    return


@app.cell(hide_code=True)
def task2(mo):
    mo.md(r"""## **Task 2**: Selecione algumas colunas""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione as colunas `first_name`, `country` e `score` da tabela `customers`.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT first_name, country, score FROM customers
        """
    )
    return


@app.cell(hide_code=True)
def task3(mo):
    mo.md(r"""## **Task 3**: Retorne `customers` (consumidor) com `score` diferente de zero """)
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
            first_name
        FROM customers
        WHERE score != 0
        """
    )
    return


@app.cell(hide_code=True)
def task4(mo):
    mo.md(r"""## **Task 4**: Retorne os consumidores da Alemanha""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE country = 'Germany'
        """
    )
    return


@app.cell(hide_code=True)
def task5(mo):
    mo.md(r"""## **Task 5**: Ordenação por atributo""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM customers
        ORDER BY score DESC
        """
    )
    return


@app.cell(hide_code=True)
def task6(mo):
    mo.md(r"""## **Task 6**: Ordenando por mais de um atributo""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        ORDER BY country ASC, score DESC
        """
    )
    return


@app.cell(hide_code=True)
def task7(mo):
    mo.md(r"""## **Task 7**: Retorne o `score` total por país""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
            country, 
            SUM(score) AS total_score
        FROM customers
        GROUP BY country
        """
    )
    return


@app.cell(hide_code=True)
def task8(mo):
    mo.md(r"""## **Task 8**: Contando número de registros""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Retorne o número total de consumidores e o `score` total por país.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT 
            country, 
            SUM(score) AS total_score,
            COUNT(id) AS qt_customers
        FROM customers
        GROUP BY country
        """
    )
    return


@app.cell(hide_code=True)
def task9(mo):
    mo.md(r"""## **Task 9**: Prática com `WHERE` e `HAVING`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Encontre o `score` médio de cada país, considerando apenas consumidores com `score` DIFERENTE DE ZERO.

    Retorne apenas os países com pontuação média acima de 430.
    """
    )
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT
            country,
            AVG(score) AS avg_score
        FROM customers
        WHERE score != 0
        GROUP BY country
        HAVING avg_score > 430
    
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 10**: Retorne uma lista única de países""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT DISTINCT country
        FROM customers
        """
    )
    return


@app.cell(hide_code=True)
def task11(mo):
    mo.md(r"""## **Task 11**: Quais os 3 consumidores com maior `score`?""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM customers
        ORDER BY score DESC
        LIMIT 3
        """
    )
    return


if __name__ == "__main__":
    app.run()
