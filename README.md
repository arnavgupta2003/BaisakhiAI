
<H1 align = "center"> Baisakhi AI </H1>

### `Project Live at:`  [Replit](https://baisakhiai.arnagupta.repl.co/)
#### `Datasets from:`  [fao](http://www.fao.org/statistics/databases/en/) ; [Kaggle](https://www.kaggle.com/)
#### `Demo Video:` [Loom](https://www.loom.com/share/98946fd5124243719aa9855b4cdfb1ac) 

## Team Ctrl Z
<ul>
  <li>
    Divyansh Gaba(CSAM) (2nd Year IIIT-D)
    </l1>
    <li>
    Tanisha Bansal(CSAI) (1st Year IGDTUW)
    </l1>
    <li>
    Arnav Gupta(CSAM) (2nd Year IIIT-D)
    </l1>
    </ul>
    
    
# Problem Statement
<p>
  <h3>Crop Guidance and Farmers Friend - (BioTech)</h3>
  The needs of contemporary agriculture, which demands high-yield, high-quality, and efficient production, cannot be met by conventional agricultural practices. Furthermore, farmers face the main challenge of how to adapt to changing customer preferences. It is critical to modernize existing processes and use data acquired over time to determine the best potential farming practices that should be implemented. Develop a solution that uses the potential of AI to address this problem.</p> 
  
# Our Solution
<p>
As we all know, the population has increased, and so has the need for food. Many people living in small towns and rural areas are turning to farm as a result of the need for more crops. Conventional agricultural methods cannot meet the demands of modern agriculture, which call for high-yield, high-quality, and efficient production. The biggest challenge for farmers is how to adjust to shifting consumer preferences. In order to help farmers choose the best crop for their land, we came up with a better solution: an AI-based website that analyses soil parameters and makes recommendations. The project will produce the  best crop suited to those conditions based on inputs like soil pH, nutrient levels, and climate conditions, taking into account elements like water needs, temperature tolerance, and potential yield. we have trained our AI models to be able to predict the data from the dataset of the past 20 years. This will assist farmers in choosing the best crops and increase the likelihood of a successful harvest, thereby boosting their profitability and sustainability. 
Additionally, We've also included a web-3 based transaction for farmers to buy the seeds for recommended crop using ethereum

</p>

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

## `Key Features`
<ol>
  <li>Soil parameter input: Farmers can input data such as soil pH, nutrient levels, and climate conditions, into a web form, which will be stored in a database.</li>
  <li>Crop recommendations: Using machine learning algorithms, the system analyzes the soil parameters and generate a list of crops that are best suited to those conditions.</li>
  <li>Security and Authentication: The system has built-in security and authentication features to ensure that only authorized users can access the data and the system.</li>
  <li>Easy deployment: The system is easy to deploy on a web server, making it accessible to farmers all over the world.</li>
  <li>Scalability: The system is built in a way that allows for easy scalability, so that it can handle an increasing number of users and data sets.</li>
  <li>Customizable: The system is customizable and can be easily tailored to the specific needs of different regions and farming communities.</li>
  <li>User-friendly: The system is designed with a user-friendly interface, making it easy for farmers to use and navigate.</li>

</ol> 


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
  <li>Javascript</li>
  <li>Polygon</li>
  <li>Ethereum</li>
  
  
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
 

 

## `Upcoming Features`
<ol>
   <li>Data visualization: The system will provide farmers with an easy-to-understand visualization of the crop recommendations and soil parameters, making it easy for them to understand the information.</li>
  <li>Data Management: An admin interface that allows authorized users to add, edit, and delete data from the database, making it easy to maintain and update the system.</li>
  <li>Help Section: The system will connect farmers with other experts in this field which also includes other farming communities across the world.</li>
  <li>
  We have added yet another animal husbandry feature that can be expanded upon in the future. All Challenges faced in Animal husbandary and animal farming will be adressed and best possible solution for different environments will be exported via AI/ML
  </li>
  <li>
  In order to prevent scams and fraud, we will also be developing new features that can record and track Delivery.
  </li>
  
</ol>  

# Conclusion
<p>
  Baisakhi AI is a powerful tool that can help farmers improve their crop selection and increase their chances of a successful harvest. By analyzing soil parameters and providing recommendations based on factors such as water requirements, temperature tolerance, and potential yield, the system can assist farmers in making informed decisions about the crops they choose to grow.

The system's features such as soil parameter input, crop recommendations, crop suitability, data visualization, data management, security and authentication, easy deployment, scalability, customizable and user-friendly interface make it an ideal solution for farmers all over the world.

In conclusion, Baisakhi AI has the potential to revolutionize the way farmers make decisions about their crops, by providing them with accurate and relevant recommendations. By optimizing crop selection, farmers can improve their profitability and sustainability, while reducing costs and labor. This can ultimately contribute to the sustainable development of the agricultural sector, benefiting farmers and society as a whole.
</p>

# Screenshots
![ScreenShot 1](https://github.com/arnavgupta2003/BaisakhiAI/blob/2a52b91d15608cac7fee8e7f9ef8bf009cf6d2ac/s1.jpg)

![ScreenShot 2](https://github.com/arnavgupta2003/BaisakhiAI/blob/2a52b91d15608cac7fee8e7f9ef8bf009cf6d2ac/s2.jpg)

![ScreenShot 3](https://github.com/arnavgupta2003/BaisakhiAI/blob/2a52b91d15608cac7fee8e7f9ef8bf009cf6d2ac/s3.jpg)

![ScreenShot 4](https://github.com/arnavgupta2003/BaisakhiAI/blob/2a52b91d15608cac7fee8e7f9ef8bf009cf6d2ac/s4.jpg)

<p align=center> --- EOF --- </p>
