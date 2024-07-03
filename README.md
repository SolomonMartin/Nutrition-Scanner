# Nutrition-Scanner

Nutrition-Scanner is an innovative application built using LangChain and Streamlit. This app allows users to upload images of food items and receive detailed nutritional information, including calorie counts and various nutrient values. It leverages advanced machine learning models and image recognition techniques to analyze food items, making it a valuable tool for individuals tracking their dietary intake and nutrition.

## Features

- **Image Upload:** Users can easily upload images of food items directly from their device.
- **Nutritional Analysis:** The app provides a comprehensive analysis of the uploaded food image, detailing calories, macronutrients (proteins, fats, carbohydrates), and other nutritional values.
- **User-Friendly Interface:** Built with Streamlit, the app offers a clean and intuitive interface for a seamless user experience.
- **Real-Time Processing:** Get instant results and feedback on the nutritional content of the food items.
- **Data Privacy:** Ensures that all user data and images are handled securely and privately.

## Technologies Used

- **LangChain:** For integrating advanced language models to enhance data processing and analysis.
- **Streamlit:** To create an interactive and user-friendly web application interface.
- **Google Generative AI:** For implementing the machine learning models used in image recognition and nutritional analysis.
- **Pillow:** For handling image processing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FoodNutritionAnalyzer.git
   cd FoodNutritionAnalyzer

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Set up your Google API key:
   
    Create a .env file in the root directory of the project.
    Add your Google API key to the .env file:

    ```makefile
     GOOGLE_API_KEY=your_api_key_here

4. Run the Streamlit app:

   ```bash
    streamlit run app.py

Usage

    Open the app in your browser.
    Upload an image of a food item.
    View the detailed nutritional analysis provided by the app.
