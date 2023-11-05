import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [recipes, setRecipes] = useState([]);

  const searchRecipes = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/search_recipes?query=${query}`);
      setRecipes(response.data);
    } catch (error) {
      console.error('Error fetching data: ', error);
    }
  };

  return (
    <div className="App">
      <h1>Food Recipe Search</h1>
      <input
        type="text"
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Search for a recipe"
      />
      <button onClick={searchRecipes}>Search</button>

      <div>
        {recipes.map((recipe, index) => (
          <div key={index} className="recipe">
            <h2>{recipe.recipe_name}</h2>
            <p>Possible allergens: {recipe.allergens}</p>
            <p>Percentage in recipes: {recipe.percentage.toFixed(2)}%</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
