from DataInsertion import DataInsertion


request = DataInsertion("http://justingrover.112.2o7.net/b/ss//6","blogdev")
request.add_variable("pageName","Analytics Launch eVent v1.1")
request.add_variable("contextData",{"a.LaunchEvent":1})
print request.variables
request.send_request()
print request.request_data