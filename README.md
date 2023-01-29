
<H1 align = "center"> Baisakhi AI </H1>

This project aims to assist farmers in selecting the most suitable crop for their land by analyzing soil parameters and providing recommendations. 
By inputting data such as soil pH, nutrient levels, and climate conditions, the project will generate a list of crops that are best suited to those 
conditions, taking into account factors such as water requirements, temperature tolerance, and potential yield. This will help farmers to optimize 
their crop selection and improve the chances of a successful harvest, ultimately increasing their profitability and sustainability.

### `Project Live at:`  [Replit](https://baisakhiai.arnagupta.repl.co/)

## `Tech Stack`
<ul>
  <li>Scikit-learn</li>
  <li>django</li>
  <li>Python</li>
  <li>Python Virtual Env</li>
  <li>Pandas</li>
  <li>Numpy</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>BootStrap</li>
  <li>Tailwind CSS</li>
  <li>Javascript</li>
  <li>ReactJS</li>
  
  
</ul>  


## `Installation`

```console
# Clone the project
$> git clone https://github.com/arnavgupta2003/BaisakhiAI.git

# Deploy a Python virtual Environment
$> virtualenv myEnv
$> myEnv\Scripts\activate

# Install Project Requirements
$> pip install -r requirements.txt

# Migrate the project
$> python manage.py migrate

# Start the Development Server
$> python manage.py runserver
      
      
```

`Check Output`

Access the project on https://127.0.0.1:8000

## `Implementation`

### The implementation of this project using the Django framework and scikit-learn library involved the following steps:
<ol>
  <li>Created a new Django project and built a form in Django that allows farmers to input their soil parameters and submit the data to the application.</li>
  <li>Used scikit-learn to train a machine learning model on a dataset of soil parameters and corresponding crop recommendations imported from Kaggle.</li>
  <li>Created a view in Django that takes the soil parameters from the form and uses the trained model to generate a recommended crops.</li>
  <li>Display the recommended crops to the farmer on a web page, along with information about the suitability of each crop for the given soil conditions with it's yeild given the land under cultivation.</li>
  <li>Used the Django middleware for handling security and authentication for the project.</li>
  <li>Finally Deployed the project on a web server and make it available for farmers to use.</li>
</ol>


<p align=center> --- EOF --- </p>
