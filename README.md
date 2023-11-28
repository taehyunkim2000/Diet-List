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


Functionalities and Test Results




