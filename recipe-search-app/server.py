from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load your CSV data into a DataFrame
df = pd.read_csv('./data/food_ingredients_and_allergens.csv')


@app.route('/search_recipes', methods=['GET'])
def search_recipes():
    query = request.args.get('query', '')
    allergen_to_check = request.args.get('allergen', '')

    # Filter recipes that contain the query in the title
    filtered_recipes = df[df['name'].str.contains(query, case=False, na=False)]

    # Calculate the percentage of products containing the allergen
    total_products = len(filtered_recipes)
    allergen_products_count = len(filtered_recipes[filtered_recipes['Allergens'].str.contains(allergen_to_check, case=False, na=False)])
    percentage = (allergen_products_count / total_products) * 100 if total_products > 0 else 0

    # Get up to 10 non-allergen recipes
    non_allergen_recipes = filtered_recipes[~filtered_recipes['Allergens'].str.contains(allergen_to_check, case=False, na=False)]
    non_allergen_recipes_list = non_allergen_recipes.head(10).to_dict('records')  # Convert to list of dicts

    # Construct response
    response = {
        'query': query,
        'allergen': allergen_to_check,
        'percentage': percentage,
        'non_allergen_recipes': non_allergen_recipes_list
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
