import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **CREATE**""")
    return


@app.cell(hide_code=True)
def task1(mo):
    mo.md(r"""## **Task 1**: Crie uma nova tabela """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Crie uma nova tabela com as colunas `id`, `person_name`, `birth_date` e `phone`.""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        CREATE TABLE persons (
            id INT NOT NULL,
            person_name VARCHAR(50) NOT NULL,
            birth_date DATE,
            phone VARCHAR(15) NOT NULL,
            CONSTRAINT pk_person PRIMARY KEY (id)
        )
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **ALTER**""")
    return


@app.cell(hide_code=True)
def task2(mo):
    mo.md(r"""## **Task 2**: Adição de coluna""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Adicione uma coluna `email` à tabela `persons`.""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        ALTER TABLE persons
        ADD email VARCHAR(50)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// TIP | DuckDB
    O DuckDB não aceita restrições (`NOT NULL`, etc.) em colunas adicionadas com o `ALTER`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **DROP**""")
    return


@app.cell(hide_code=True)
def task3(mo):
    mo.md(r"""## **Task 3**: Remova a coluna `phone`""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        ALTER TABLE persons
        DROP COLUMN phone
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Task 4**: Remova a tabela `persons`""")
    return


@app.cell
def task4(mo):
    _df = mo.sql(
        f"""
        DROP TABLE persons
        """
    )
    return


if __name__ == "__main__":
    app.run()
