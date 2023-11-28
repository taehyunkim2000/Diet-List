Goal of the project: 

Purpose is to assist individuals in achieving their desired weight by generating a personalized daily diet plan. 

1. User Input Handling: Create an interface that allows users to input their current weight, sex, current daily calorie intake, and weight-related goal (lose, gain, or maintain)
2. Personalized diet Plan Generation: Calculate the target daily calorie intake based on the user's input. Generate a personalized daily diet plan with three meals (Breakfast, Lunch, Dinner) by randomly selecting foods from a provided nutritional data set. 


Significance of The Project:
1. Health Improvement: By providing personalized diet plans, the application contributes to users' overall health and well-being. Achieving weight-related goals can positively impact physical and mental health, leading to increased happiness.

2. Goal Achievement: The project supports users in setting and achieving weight-related goals. Successfully attaining these goals can instill a sense of accomplishment and satisfaction, thereby contributing to increased happiness.

3. Nutritional Awareness: The application promotes awareness of nutritional values by incorporating a database of food items and their respective nutritional information. This knowledge empowers users to make informed choices about their diet, fostering a healthier and happier lifestyle.

4. User Engagement: The interactive nature of the GUI, coupled with the presentation of a personalized diet plan, enhances user engagement. The element of randomness in food selection adds an element of surprise, making the experience more enjoyable.

5. Simplicity and Accessibility: The user-friendly interface and straightforward functionality make the project accessible to a wide range of individuals. This inclusivity ensures that more people can benefit from the positive effects of a personalized diet plan, contributing to their happiness.

In collaboration with the provided code, this project aims to be a valuable tool in promoting healthier lifestyles and fostering happiness through the achievement of weight-related goals.



Structure of the code:

+---------------------------+
| Import Modules 
    import tkinter as tk
    from tkinter import messagebox
    import json
    import random

+---------------------------+
| Function Definitions      |
|   - load_nutritional_data |
|   - calculate_target...   |
|   - select_foods_for_meal |
+---------------------------+
| GUI Related Functions     |
|   - submit_action         |
+---------------------------+
| GUI Setup                 |
|   - Window and Widgets    |
|   - Submit Button         |
+---------------------------+
| Main Event Loop           |
|   - root.mainloop()       |
+---------------------------+
1. Imports
   tkinter: A standard Python interface to the Tk GUI toolkit.
   messagebox: A Tkinter module used for displaying message boxes.
   json: A module for working with JSON data.
   random: Used for randomizing selections.

   
3. Function Definitions
   load_nutritional_data(file_path): Loads nutritional data from a JSON file. It takes the file path as an argument and   
     returns a list of dictionaries containing the nutritional information.

   calculate_target_calories(current_calories, goal_calories): Calculates the target daily calorie intake based on the   
     user's current calorie intake and their goal (weight loss, gain, or maintenance).

   select_foods_for_meal(foods, used_foods, max_calories, max_items=3): Selects an appropriate number of food items for each 
     meal. It ensures diversity in meal selection and adheres to the calorie limit for the meal.

   
4. GUI Related Functions
    submit_action(): This function is triggered when the user clicks the "Generate Diet Plan" button in the GUI. It fetches       user inputs, processes them through the defined functions, and displays the resulting diet plan in a message box.






Installation and Instruction to use:
1. Install both of the files (SourceCode and Food Data Generator) into one folder and make sure Python is properly installed on your computer
2. Run the Food Data Generator.py first to export out the most updated food nutrition data from USDA Website (The food data base only included 100 common food for diet and the list is malleable to adjust to the users liking, you can do this by changing the list in Food Data Generator.py)
3. After exporting the food data as a JSON file, make sure to change the file pathing (line 46) in the Source code to wherever your JSON file is (usually in your python directory)
4. Run the SourceCode and a window will pop up for the user to enter their infomation and a personalized daily diet list will pop up.


Functionalities and Test Results:

Diet Plan Generator (Code 1):

#### Functionalities:
1. **User Input:**
   - Takes user input for current weight, sex, current daily calorie intake, and goal (lose, gain, maintain).
   
2. **API Integration:**
   - Utilizes the USDA FoodData Central API to fetch nutritional information for a predefined list of foods.
   
3. **Diet Plan Generation:**
   - Calculates target calories based on user input and generates a personalized diet plan.
   - Randomly selects foods for each meal while considering calorie constraints and avoiding repetition.

4. **User Interface:**
   - Provides a basic Tkinter GUI for user interaction.
   - Displays the generated diet plan in a pop-up window.

#### Testing Results:
1. **Input Validation:**
   - Tested with both valid and invalid inputs for weight, sex, current daily calorie intake, and goal.
   - The application correctly handles invalid inputs and provides appropriate feedback.

2. **API Integration:**
   - Successfully retrieves nutritional information from the USDA FoodData Central API.
   - Handles API errors and provides appropriate feedback to the user.

3. **Diet Plan Generation:**
   - Generates a diet plan with randomized food selections for each meal.
   - Ensures that the generated plan adheres to the specified calorie constraints.

4. **User Interface:**
   - The Tkinter GUI displays input fields and a button for generating the diet plan.
   - The generated diet plan is displayed in a pop-up window.

### Nutritional Data Fetcher (Code 2):

#### Functionalities:
1. **API Integration:**
   - Fetches specific nutritional information (Calories, Sugars, Protein, Total Fat) for a predefined list of foods from the USDA FoodData Central API.
   
2. **Data Processing:**
   - Processes the API response to extract and organize relevant nutritional information for each food.

3. **Data Storage:**
   - Saves the processed nutritional data, including food names, in a JSON file (`food_nutrition_data.json`).

#### Testing Results:
1. **API Integration:**
   - Successfully retrieves specific nutritional information for each food from the USDA FoodData Central API.

2. **Data Processing:**
   - Extracts and organizes relevant nutritional information from the API response.

3. **Data Storage:**
   - Saves the processed nutritional data to a JSON file.
   - The saved JSON file (`food_nutrition_data.json`) can be used as input for the Diet Plan Generator.

### Overall Result:
Both functionalities work as intended, and the testing results confirm that the applications successfully fetch nutritional data, generate personalized diet plans, and handle user inputs appropriately. The generated diet plans are based on the nutritional information retrieved from the USDA FoodData Central API.


Discussion and Conclusion:

One of the issues we have encountered during this project was developing a user interface for our software. It was the first time for us to implement tkinter into python to generate a simple user interface for program. However, the UI itself is overly simple and does not have any design to make our software unique, this would be something to improve upon. Futhermore, the food database itself is only limited to 100 foods, this could be further increase at the cost of a long generating time since the file Food Data Generator.py is taking the data from USDA one by one, the entire software would be more efficient if we find a way to extract multiple objects along with their data (calories, fat, carbo, protein) from the website to shorten the run time. The list of foods itself can also be enhanced upon based on categorizing according to which foods are suitable for breakfast, lunch, and dinner, this issue will probably require manual selection of each food and putting them into separate lists, but it will create a diet plan that makes more sense then what we have right now. 






