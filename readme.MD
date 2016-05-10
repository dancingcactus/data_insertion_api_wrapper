# Purpose
This is a **VERY** light wrapper around the Adobe Analytics Data [Insertion API](https://marketing.adobe.com/developer/documentation/data-insertion/c-data-insertion-api)

# Getting Started
```python
from DataInsertion import DataInsertion


request = DataInsertion("http://justingrover.112.2o7.net/b/ss//6",report_suite="somereportSuiteID")

request.add_variable("pageName","somepagename")

request.send_request()
```

Note that a pagename or page url is required.

# Method Docs

_ **DataInsertion**(endpoint, report_suite,visitor_id=none)_ -- Initializes the object
* **endpoint** -- The endpoint to send the data too. look somethign like this. http://somename.112.2o7.net/b/ss//6
* **report_suite** -- the report suite to send the data to. This is a required field for the API.
* **visitor_id** -- allows you to specify the visitor ID you want to use. If you don't specify one the library will generate one. You can also set the visitor ID to using the `set_visitor_id` method.

_ **add_variable**(variable, value)_ -- This allows you to add a `variable` and give it a `value`. In the case of `contextData` the variable can be a dict of the key value pairs you want to send in. The list of variables is available in the (docmentation)[https://marketing.adobe.com/developer/documentation/data-insertion/r-supported-tags]

_ **set_visitor_id**(id)_ -- Allows you to set a visitor ID. If no id is set one is generated randonmly when the object is initialized. 

_ **generate_visitor_id**()_ -- Generates a new visitor ID. 

_ **get_xml**()_ -- Generates the string representation of the XML for the request. 

_ **send_request**()_ -- Send the request to Adobe using the endpoint specified on initialization
