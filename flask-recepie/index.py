from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def main():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood")
    meals = response.json()
    return render_template("index.html", meals=meals)

@app.route("/single_meal/<meal_id>")
def single_meal(meal_id):
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}")
    meals = response.json()
    return render_template("single_meal.html", meals=meals) 

if __name__ == "__main__":
    app.run(debug=True)