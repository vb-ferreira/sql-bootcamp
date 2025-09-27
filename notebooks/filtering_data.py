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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Operadores condicionais**""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: Selecione todos os consumidores da Alemanha.""")
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
def _(mo):
    mo.md(r"""# **Operadores Lógicos**""")
    return


@app.cell(hide_code=True)
def task2(mo):
    mo.md(r"""## **Task 2**: Operador `AND`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione todos os consumidores dos Eatdos Unidos com `score` maior que 500.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE country = 'USA' AND score > 500
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 3**: Operador `NOT`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione os consumidores que não têm menos de 500 de `score`.""")
    return


@app.cell
def task3(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE NOT score < 500
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Operador de Intervalo**""")
    return


@app.cell(hide_code=True)
def task4(mo):
    mo.md(r"""## **Task 4**: Operador `BETWEEN`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Selecione os consumidores com `score` entre 100 e 500.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE score BETWEEN 100 AND 500
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Operador de Busca**""")
    return


@app.cell(hide_code=True)
def task5(mo):
    mo.md(r"""## **Task 5**: Operador `LIKE`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Encontre os consumidores cujo primeiro nome começe com "M".""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE first_name LIKE 'M%'
        """
    )
    return


@app.cell(hide_code=True)
def task6(mo):
    mo.md(r"""## **Task 6**: Operador `LIKE` II""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Encontre os consumidores cujo primeiro nome termine com 'n'.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE first_name LIKE '%n'
        """
    )
    return


@app.cell(hide_code=True)
def tesk7(mo):
    mo.md(r"""## **Task 7**: Operador `LIKE` III""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Encontre os consumidores cujo primeiro nome contenha a letra 'r'""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE first_name LIKE '%r%'
        """
    )
    return


@app.cell(hide_code=True)
def task8(mo):
    mo.md(r"""## **Task 8**: Operador `LIKE` IV""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Encontre os consumidores que tenham a letra 'r' na terceira posição de seus nomes.""")
    return


@app.cell
def _(customers, mo):
    _df = mo.sql(
        f"""
        SELECT *
        FROM customers
        WHERE first_name LIKE '__r%'
        """
    )
    return


if __name__ == "__main__":
    app.run()
