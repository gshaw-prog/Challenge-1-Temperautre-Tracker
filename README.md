<h1><b> Challenge 1: Temperature Tracker </b></h1>

This challenge focuses on : 
<UL>
<li>B2.5.1 File Processing</li>
<li>B2.1.1 Programming Fundamentals (variables and data types) </li>
<li>B2.3.3 Looping Structures</li>
<li>B2.3.2 Selection Structures</li>
</UL>


<h2>Problem Description: </h2>
<p>You are given a text file named <i>hk-temperatures-2024.txt</i> which contains a list of daily temperature readings, with one reading per line. Your task is to process this file and calculate several statistics about the temperatures.</p>

<p> <b>Your Task: </b>Construct a Python program with a function temperature_tracker() that: </p>

<ul>
<li>Reads the daily temperature readings from the hk-temperatures-2024.txt file.</li>
<li>Calculates the average temperature [B2.4.2].</li>
<li>Identifies the highest and lowest temperatures.</li>
<li>Determines the number of days when the temperature increased compared to the previous day.</li>  
</ul>

<b> Input: </b> hk-temperatures-2024.txt (file containing daily temperature readings)

<b> Function name: </b> temperature_tracker()

<b>Return values : </b> 4 integers:
<ol> 
<li>Average temperature, rounded to the nearest integer.</li>
<li>Highest temperature, rounded to the nearest integer.</li>
<li>Lowest temperature, rounded to the nearest integer.</li>
<li>Number of days when the temperature increased compared to the previous day</li>
</ol>

<h2>Key Concepts to Apply:</h2>
<ul>
<li>File Processing (B2.5.1): You will need to open and read data from a sequential file line by line. Python provides methods to read files, such as readlines() or iterating over the file object.</li>
<li>Variables (B2.1.1): Use variables to store the sum of temperatures, counts of days, the current highest and lowest temperatures, and the count of increasing days. Temperatures will likely be stored as float or int data types.</li>
<li>Data Types (B2.1.1): As temperatures can be decimal, the float data type will be important for accurate calculations before rounding.</li>
<li>Looping Structures (B2.3.3): A for loop or while loop will be necessary to iterate through each line (daily reading) in the file.</li>
<li>Selection Structures (B2.3.2): if statements will be crucial for comparing temperatures to find the highest, lowest, and to check if the temperature increased from the previous day.</li>
<li>Programming Algorithms (B2.4.2): You will implement summing and averaging algorithms, and algorithms to find the maximum or minimum values within a list of data.</li>
<li>Exception Handling (B2.1.3): Consider how your program will handle cases where the input file might not exist or contains non-numeric data. Using try and except blocks can prevent your program from crashing.</li>
</ul>
<h2>Hints and Guidance:</h2>
<ul>
<li>Remember to open the file, read its contents, and close it when you are done.</li>
<li>Each line read from the file will initially be a string. You'll need to convert these strings to numerical data types (e.g., float or int) before performing calculations.</li>
<li>Initialize your highest_temperature to a very low value and lowest_temperature to a very high value before starting to read the data to ensure they are correctly updated by the first actual temperature.</li>
<li>Keep track of the previous_day_temperature in your loop to compare with the current_day_temperature.</li>
 </ul>
