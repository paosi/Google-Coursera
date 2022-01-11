# Course 6 - Automating Real World Tasks with Python


# Week 1 Lab: Scale and Convert Images Using PIL

Problem Statement:

Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll need to use Python to get these images ready for launch.

Requirements:

Use the Python Imaging Library to do the following to a batch of images:
- Open an image
- Rotate an image
- Resize an image
- Save an image in a specific format in a separate directory

Solution:

Download and unzip "images.zip" which should create the "/images" directory. Install the pillow (PIL) module which will be used to modify the image files. Open "py_images.py" file. Create the destination directory "/opt/icons" if it doesn't exist yet. Iterate through each file in the source directory one-by-one and create an Image object. Apply Image methods "rotate()", "resize()", "convert()", and "save()" to each Image object to convert the file and save in the destination directory.


# Week 2 Lab: Process Text Files with Python Dictionaries and Upload to Running Web Service

Problem Statement:

You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company's website (currently using Django).

Requirements:

- Use the Python OS module to process a directory of text files
- Manage information stored in Python dictionaries
- Use the Python requests module to upload content to a running Web service
- Understand basic operations for Python requests like GET and POST methods

Solution:

Create a python script "run.py". Traverse over each file in the source directory and, from the contents of these text files, create a dictionary by keeping "title", "name", "date", and "feedback" as keys for the content value, respectively. Use the "requests.post()" method to make a POST request to the URL endpoint to upload the dictionary's content. Use ".ok" to check if there was an error or if the content was successfully added. The entry should now be viewable on web using the external IP address.


# Week 3 Lab: Automatically Generate a PDF and send it by Email

Problem Statement:

You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

Requirements:

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email 

Solution:

Modify "process_data()" function in "cars.py" in order to sort the data from the "car_sales.json" source file. Sort the data by max sales in order to find the most popular make/model car. Then sort by the most popular year and return the total sales for that year. Import the "reports" module and use "generate_report()" to generate a pdf file with this data. Finally, import the "emails" module and use "generate_email()" to format an email, and "send_email" to send a message and the "cars.pdf" file as an attachment.


# Week 4 Lab (Final):

Problem Statement:

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

Requirements:

- Write a script that summarizes and processes sales data into different categories 
- Generate a PDF using Python
- Automatically send a PDF by email 
- Write a script to check the health status of the system 

Solution:

Download the supplier data file "supplier-data.tar.gz" and extract the contents. This will create "/supplier-data" directory with "/images" and "/descriptions" subdirectories. Write a Python script named "changeImage.py" to process the supplier images. You will be using the PIL library to update all images within "/supplier-data/images" directory.

- Use ".size()" to change image size from 3000x2000 to 600x400 pixel
- Use ".covert()" to change image type to RGB 
- Use ".save()" to format as JPEG

All the image files should now be resized and renamed in the source directory.

Next, write a script named "supplier_image_upload.py" that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog. Iterate through each image file and use "requests.post()" to make a POST request to the web server. Use ".ok" to check if the file was uploaded successfully and return the status code using ".status_code".

The image files should now be visible on the web using the external IP address.

Next, Write a Python script named "run.py" to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, "name", "weight", "description", "image_name". Upload the dictionary to http://[linux-instance-external-IP]/fruits using the Python requests library.

The descriptions and corresponding images should now be visible on the web using the external IP address.

Next, Create a script "reports.py" to generate PDF report to supplier. Using the "reportlab" Python library, define the method "generate_report()" to build the PDF reports. There was a script that was provided in an earlier module that you can modify to accomplish this.

Create "emails.py" in order to generate an email in the proper format. Again, this script was already provided in a previous module. Create a new function, "generate_error_report()" which will be used to generate an email without an attachment. Do this by modifying the "generate_email()" function and removing the "attachment_path" parameter.

Create another script named "report_email.py" to process supplier fruit description data from "supplier-data/descriptions" directory. The script should return the "paragraph" parameter to be used in "reports.generate_report(attachment, title, paragraph)". This will be be used to generate the pdf file that will be sent as an attachment to the supplier using "reports.generate_report()". Now generate and send the email using "emails.generate_email()" and "emails.send_email()".

Finally, write a Python script named "health_check.py" that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Import the "psutil", "shutil", and "socket" modules to return this info. This Python script should send an email if there are problems, such as:

- Report an error if CPU usage is over 80%
- Report an error if available disk space is lower than 20%
- Report an error if available memory is less than 500MB
- Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

I accomplished this using IF statements.

If there is an error message, send an email to the supplier using the "emails.generate_error_report()" function.

If correct, an email should be generated with the following subject: "Error - CPU usage is over 80%".

 






