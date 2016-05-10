import requests
from lxml import etree
import uuid


class DataInsertion:
    """A Simple Class to Insert Data into Adobe Analytics using the Data Insertion API"""
    def __init__(self, endpoint, report_suite, visitor_id=None ):
        self.endpoint = endpoint
        self.variables = {}
        self.variables['reportSuiteID'] = report_suite
        if visitor_id:
            self.variables['reportSuiteID'] = visitor_id
        else:
            self.generate_visitor_id()
        
    def add_variable(self, variable, value):
        """Adds a variable to the """
        self.variables[variable] = value
        return self
    
    def generate_visitor_id(self):
        """Creates a random visitor ID with from a UUID"""
        self.set_visitor_id(uuid.uuid4().hex)
        
    def set_visitor_id(self,id):
        self.add_variable("visitorID",id)
        return self
            
    def get_xml(self):
        """Returns the XML of the reqeust"""
        payload = etree.Element("request")
        for v in self.variables:
            child = etree.Element(v)
            if type(self.variables[v]) == dict:
                for item in self.variables[v]:
                    sub_child = etree.Element(item)
                    sub_child.text = str(self.variables[v][item])
                    child.append(sub_child)
            else:
                child.text = str(self.variables[v])
            payload.append(child)
        return etree.tostring(payload, xml_declaration=True, encoding="UTF-8", pretty_print=True)
        
    def send_request(self):
        """Sends the data to Adobe"""  
        xml = self.get_xml()
        self.request = requests.post(self.endpoint, data=xml)
        self.request_data = xml
        return self
