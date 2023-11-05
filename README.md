# Recipe Search App

## Introduction

Welcome to the Recipe Search App - a simple yet powerful tool to help you find delicious recipes and identify potential allergens. Whether you're a food lover or have dietary restrictions, our app aims to assist you in discovering new dishes while being mindful of ingredients that might not agree with you.

This app is built using React for the frontend and Flask for the backend, with a CSV database that includes a variety of recipes and associated allergen information.

## Getting Started

To get the app up and running on your local machine, follow these steps after cloning the repository:

### Prerequisites

Make sure you have the following installed before you proceed:

- Node.js and npm (https://nodejs.org/)
- Python (https://www.python.org/)

### Installation

1. **Clone the repository**

   ```sh
   git clone https://your-repository-url.git
   cd your-repository-name
   ```

2. **Set up the Frontend**

   Navigate back to the root directory and install the necessary npm packages:

   ```sh
   cd recipe-search-app  # Adjust this path to where your frontend code is located
   npm install
   ```

3. **Set up the Backend**

   Navigate to the backend directory where `server.py` is located and create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

4. **Start the Application**

   With the setup complete, you can now run the app:

   ```sh
   npm start
   ```

   This command will concurrently launch the Flask server and the React frontend.

### Using the App

Simply enter a keyword into the search bar and press the 'Search' button to find recipes. The app will display a list of recipes along with the potential allergens and the percentage of recipes containing those allergens.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc.