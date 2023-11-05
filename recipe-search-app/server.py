from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load your CSV data into a DataFrame
df = pd.read_csv('food_ingredients_and_allergens.csv')

@app.route('/search_recipes', methods=['GET'])
def search_recipes():
    query = request.args.get('query', '')  # Get the search query from URL parameters
    # Implement a search functionality based on your CSV structure and the query
    # For now, let's just filter rows that contain the query string in a 'recipe_name' column
    filtered_recipes = df[df['Food Product'].str.contains(query, case=False, na=False)]

    # Calculate allergens and percentages here
    # This is a placeholder example where 'allergens' is a column in your CSV
    allergens_count = filtered_recipes['Allergens'].value_counts(normalize=True) * 100

    # Convert to JSON-friendly format (e.g., a list of dictionaries)
    results = [{
        'recipe_name': row['Food Product'],
        'allergens': row['Allergens'],
        'percentage': allergens_count.get(row['Allergens'], 0)
    } for index, row in filtered_recipes.iterrows()]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
