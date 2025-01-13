from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # load tables
    table1 = pd.read_csv("Table1.csv")
    table2 = pd.read_csv("Table2.csv")

    # table 1
    table1_html = table1.to_html(index=False, classes="table table-bordered", border=0)

    # table 2
    table2_list = table2.values.tolist()

    return render_template("index.html", table1=table1_html, table2=table2_list)


if __name__ == "__main__":
    app.run(debug=True)
