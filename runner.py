from DataInsertion import DataInsertion

request = DataInsertion("http://justingrover.112.2o7.net/b/ss//6","somereportsuite")
request.add_variable("pageName","somepagename")
request.send_request()
