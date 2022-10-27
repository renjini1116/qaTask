Project Title : validating data provided in the file "elastic_data.json" using pytest.


Solution:
1. Read the elastic_data.json file from the path https://raw.githubusercontent.com/ant1kdream/g42-qa-test-task/main/elastic_data.json
2. Fetch the data from main node and again from sub nodes of entire records .
3. Verifying the existence of value in each node and printing 'No data found' if any of the node value is blank.
4. fetching the group of records in readable format and storing Customer_details.txt and Product_details.txt files on each run. 
5. Customer details.txt file returns the all the below details from entire purchase record.

        Customer Id    : 38 
        First Name     : Eddie 
        Full Name      : Eddie Underwood 
        Category       : ["Men's Clothing"] 
        Email          : eddie@underwood-family.zzz 
        Customer Phone : No data found 
        Currency       : EUR 
        manufacturer   : ['Elitelligence', 'Oceanavigations'] 

        
6. Product details.txt file returns all the below details from entire purchase record.
  
        Base Price          : 99.99 
        Discount Percentage : 0
        Quantity            : 1
        Product Id          : 23386
        Tax less Price      : 99.99
        Created on          : 2016-12-25T22:32:10+00:00
        Order Date          : 2022-10-30T22:32:10+00:00
        Order Id            : 584058
        Product Name        : Short coat - white/black 
        Price               : 99.99 
        Geoip country code  : US


7. Fetching each purchace record and save it to 'data.json' file verifying the Json structure and returns True if Verification Pass.

   Json nodes validation Result :   
            Given Json data of each transactions records are  True
   
8. The Json data validation returns False if node structure is wrong.

   Json nodes validation Result :   
            Given Json data of each transactions records are  False
   
9. Fetching entire purchase record and get data under the Hit sub node and verifying the Json Validation and returns Pass if Verification Pass.

Json file validation Result :   
          Given Json data file and structure are  True

10. The Json file validation returns False if node structure is wrong.

Json file validation Result :   
          Given Json data file and structure are  False



        
              
