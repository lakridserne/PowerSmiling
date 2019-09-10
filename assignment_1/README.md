# Assignment 1 handin

### Answers:
1. price_list.csv
   price_list.txt
   prices.png
2. It generates a CSV file, a txt file and a png file.
   The files contain information, which is then used to generate the image.
   It gets the csv file from a github folder which it uses to generate the other files.
    * Ved Volden 5, 5. TV; 1425 København K	4000000	91
    * Rådhusstræde 4C, 1; 1466 København K	4895000	105
    * Store Kongensgade 112A, 3; 1264 København K	250000	135
    * Amaliegade 13G, 2; 1256 København K	7375000	98
    * Borgergade 144, 3. TH; 1300 København K	5825000	101
    * Nørre Søgade 9A, 1. TH; 1370 København K	1126250	107
    * Wildersgade 22, ST; 1408 København K	1556700	88
    * Toldbodgade 10A, 1; 1253 København K	3750000	184
    * Andreas Bjørns Gade 4, 3. TH; 1428 København K	1700000	54
    * Sølvgade 15, 4. TH; 1307 København K	4215000	81
    * Linnésgade 16A, 1; 1361 København K	6300000	155
    * Store Kongensgade 63A, ST. 4; 1264 København K	1780000	98
    * Peder Skrams Gade 28, 2. TV; 1054 København K	4080000	76
    * Brobergsgade 14, 1. TV; 1427 København K	2750000	50
    * Sølvgade 13, 2. TV; 1307 København K	3150000	73
    * Ny Adelgade 9, 2. TH; 1104 København K	1950000	70
    * Lavendelstræde 9, 2. TV; 1462 København K	1550000	66
    * Åbenrå 10, 2. 5; 1124 København K	1650000	70
    * Grønnegade 31, 3. TV; 1107 København K	1200000	49
    * Badstuestræde 16, 2; 1209 København K	2700000	97
    * Nørre Voldgade 70, 4; 1358 København K	1870000	99
    * Fredericiagade 25, 5. 1; 1310 København K	3150000	118
    * Sølvgade 19, 2. MF; 1307 København K	2425000	49
    * David Balfours Gade 3, ST. TV; 1402 København K	3100000	83
    * Vimmelskaftet 36A, 3. TH; 1161 København K	3695000	84
    * Store Kongensgade 110C, 3. TV; 1264 København K	3050000	118
    * Andreas Bjørns Gade 10, 3. TV; 1428 København K	2367000	53
    * Grønnegade 31, 4; 1107 København K	3950000	73
    * Peder Skrams Gade 27, 3. TH; 1054 København K	6250000	112
    * Andreas Bjørns Gade 22, 3. TH; 1428 København K	2900000	55
    * Kronprinsessegade 10, 4. TV; 1306 København K	4350000	101
    * Bartholinsgade 11, 1. TV; 1356 København K	841000	52
    * Sankt Peders Stræde 17, 2; 1453 København K	4125000	106
    * Ved Volden 11, 4. TH; 1425 København K	4900000	97
    * Luftmarinegade 38; 1432 København K	2485131	137
    * Gernersgade 5, ST. TV; 1319 København K	1950000	37
    * Ahlefeldtsgade 26, 4. TV; 1359 København K	2115000	82
    * Dronningens Tværgade 36, 4. 1; 1302 København K	1785000	82
    * Nikolajgade 20, 2. TV; 1068 København K	3500000	92
    * Strandgade 12, 3; 1401 København K	7170000	228
    * Store Kongensgade 90, 2. TH; 1264 København K	7500000	158
    * Gothersgade 147, 3. TV; 1123 København K	3622500	68
3. 3307228.119047619, which is the average price.
4. Explain line by line code
  1. First we include some code other people have written so we can be lazy
  2. Include a library more which will allow us to make a text file separated by commas.
  3. Include library to help us handle requests
  4. Import a library more which will help us get more details about the computer
  5. Import statistics library
  6. Import matplotlib. This library has some math functions to produce a plot
  7. Select the backend (some code that helps us) that generate PNG files (for the image)
  8. Import specific function pyplot from matplotlib and we can just use plt to interact with it
  9. empty
  10. empty
  11. A function is some code we can reuse with a single word. Here we make the function download_txt.
      This function has some parameters - or a way to tell the function something. In this case, we
      want to know what URL (website address) and where it should put the downloaded content.
  12. Save what we get out of the request for that URL in a variable. Essentially a box where we can put stuff in.
  13. Try to open the place we got in line 11 with both read and write - and as binary on Windows. Binary means
      that the file is built from only 1's and 0's inside the computer.
  14. Write the content of the request we got in line 12 to the file we opened in line 13.
  15. empty
  16. empty
  17. Function (like in line 11) which will generate CSV. Take in an input path (i.e. what goes in to the function)
      and an output path (where we should put the CSV)
  18. Open the input file. We use what's called UTF-8. This means that we tell the computer what language or alphabet
      the computer should use to read or write to the file. For example we have arabic which is a completely different
      alphabet from English - and in Danish there is for example æ, ø and å that is not in the English alphabet.
  19. We save the contents of the file in the variable.
  20. empty
  21. We make a list - essentially a variable with multiple items in it.
  22. Make a loop. With a loop we can repeat (or iterate) things again and again. Each time the loop runs, we make sure line is the variable that contains the things from txt_content about the current line.
  23. Computers read this from right to left - that's why we can assign a variable to itself. We take the current content from the line, remove spaces and replace * with nothing.
  24. We split the line into 3 variables by tabs. address price and sqm
  25. In the same way as in line 24 we split address by semicolon into street and city.
  26. Now we find the price per square meter (sqm) by dividing the price (as a whole number - not comma number) with the amount of square meters (as a whole number - not comma number)
  27. At last we take the variables and pack into a single row
  28. Here we put the row we made in line 27 into the list we created in line 21.
  29. empty
  30. Detect if our computer run Windows.
  31. Set the variable newline to '' (empty)
  32. If it's not Windows
  33. Set newline to None which is another word for nothing
  34. empty
  35. Open the output path for writing. We set it as UTF-8 (read explanation from line 18 if you don't know what it does.)
  36. Make a variable to manage writing to the output file
  37. Make a loop (as explained in line 22)
  38. write the current row to the csv file
  39. empty
  40. empty
  41. Make a new function (as we tried before) where we will read prices from the CSV file. We will ask for the csv file as input.
  42. We open the file for reading - we do it as UTF-8 (read line 18).
  43. reader should now be used to read from our csv file.
  44. We get the next line from the reader we made above and put into a special variable underscore. It makes it possible for us to store the last thing we did.
  45. empty
  46. make an empty list like in line 21.
  47. Same as above - just wtih prices
  48. Make a loop like in line 22.
  49. We take the row and split into street, city, price, sqm, and price_per_sqm
  50. Append the current line number to the list we made in line 46
  51. Add the price as a whole number to the list we made in 47.
  52. empty
  53. Here we return a list (like in line 46) Where we take the line numbers and add the prices for each line
  54. empty
  55. empty
  56. New function that takes in the data
  57. Here we take the data, strip out the id and take the prices and assign the prices
  58. We get the average price by using the statistics libarys mean function
  59. empty
  60. We open a temporary file for writing in UTF-8 (see line 18).
  61. Write the average price to the file as text
  62. empty
  63. return the average price to the program that called the function. So inside the program we give back the average price.
  64. empty
  65. empty
  66. Function to generate plot. Take in data as input parameter
  67. empty
  68. Assign x values and y values from data
  69. in the fig variable we generate a figure using the plot function
  70. Make a scatter plot of x and y from the data. Specify the size
  71. Save figure to a png file
  72. empty
  73. comment (does nothing)
  74. comment
  75. empty
  76. make run function
  77. Sepcify url to txt file
  78. continuation
  79. continuation
  80. Make sure there is a file in the url we said above
  81. Make a path to the file
  82. Download the file
  83. Make a variable with the csv file name
  84. Make sure we can make a new file there
  85. Generate the CSV (call the function we made above)
  86. Get the prices (function above)
  87. Compute the average price (function above)
  88. Print the average price to the console
  89. Generate the plot (function above)
  90. Comment (does nothing)
  91. empty
  92. If our current module is the main module (if we just started the script)
  93. run the function run() - line 76.
  94. empty
