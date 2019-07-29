# Demo ETL Tools
This is a demonstration of code that can be used to import different types of files.
It has examples for:
- [x] Fixed Width Text Files (think legacy applications)
- [ ] CSV Delimited (TBD)
- [ ] Excel (TBD)


## Code Layout
There are structured data classes created with the **[attrs](http://www.attrs.org/en/stable/index.html)** package
The benefit of using the **attrs** package is that the Python builtin **dataclasses** is
 not introduced until Python 3.7.  

These structured data classes are used to validate and sanitize data.  One thing I 
like about this approach is that defining important metadata makes it easily 
discoverable by other programmers.

These data classes can also be extended and enriched with other data if you want to
do any transformations before loading.

Also, there have been times in the past where I've used Dictionary objects to 
define parsing rules and that works great, but it makes it harder to remember
what metadata is available to a programmer years later.


The **data/utilities** directory contains code that is used repeatedly.

The **data/entities** directory contains data classes that represent a single record from source data file

The **data/extract** directory contains code to import different file formats.  

### fixedwidth
For this example, we are using the Vehicle Repair fixed format file.

1. Find a **_fixed width_** file
   - Each **_fixed width_** file type has a distinct collection of **ParsingRules**
   - The **ParsingRules** are metadata about the formatting of the text file based on available documentation.
2. Instantiate a **FixedWidthParser** object for parsing the **_fixed width_** file.
   - The **FixedWidthParser** object creates **[struct.Struct](https://docs.python.org/3/library/struct.html#classes)**
 object using the **ParsingRules**
   - Each record in a **_fixed width_** file is passed to the **FixedWidthParser.parse_textdata()** method
   - The struct.Struct object is uses **unpack_from()** to convert the bytestring to a tuple of values
   - This tuple of values is returned by the **parse_textdata()** method
3. If there were no errors, open the **_fixed width_** file and read each row

4. Pass each row from the **_fixed width_** file as byte data to the **FixedWidthParser.parse_textdata()** method
   - This method will return a tuple of values extracted from the row of data
5. Use the extracted tuple to instantiate a structured data class object **VehicleRepairRecord()**
   - This structured data class will validate and sanitize the input data into Pythonic objects
   - Apply **_Transformations_** that need to be done can be done when creating the **VehicleRepairRecord()**
6. Use the instance of **VehicleRepairRecord()** to extract the _transformed_ data elements
7. Load the _transformed_ data elements into the Target data 


Note: It is possible to exercise the code behind steps 2, 4, 5 and 6 by running 
the pytest **`tests/func/test_fixed_width_parser.py`**



## References:

### Data Source
- Vehicle Repair data comes from https://catalog.data.gov/dataset/vehicle-repairs


## Testing
Use pytest to demonstrate the results
- Run the pytest
  ```shell script
   pytest tests/func/test_fixed_width_parser.py
  ```
- Print output to console (-s) and run verbose (-v)  
  ```shell script
  pytest tests/func/test_fixed_width_parser.py -s -v
  ```
