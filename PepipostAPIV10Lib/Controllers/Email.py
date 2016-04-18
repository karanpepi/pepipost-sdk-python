# -*- coding: utf-8 -*-

"""
   PepipostAPIV10Lib.Controllers.EmailController

   This file was automatically generated by APIMATIC BETA v2.0 on 04/15/2016
"""
from PepipostAPIV10Lib.APIHelper import APIHelper
from PepipostAPIV10Lib.APIException import APIException
from PepipostAPIV10Lib.Configuration import Configuration
from PepipostAPIV10Lib.Http.HttpRequest import HttpRequest
from PepipostAPIV10Lib.Http.HttpResponse import HttpResponse
from PepipostAPIV10Lib.Http.RequestsClient import RequestsClient
from PepipostAPIV10Lib.Controllers.BaseController import BaseController



class Email(BaseController):

    """A Controller to access Endpoints in the PepipostAPIV10Lib API."""

    def __init__(self, http_client = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client)

    def get_api_web_send_rest(self,
                              api_key,
                              content,
                              mfrom,
                              recipients,
                              subject,
                              att_name=None,
                              attachmentid=None,
                              bcc=None,
                              clicktrack=None,
                              footer=None,
                              fromname=None,
                              opentrack=None,
                              replytoid=None,
                              tags=None,
                              template=None,
                              x_apiheader=None):
        """Does a GET request to /api/web.send.rest.

        `Sending Mails` – This API is used for sending emails. Pepipost
        supports REST as well JSON formats for the input

        Args:
            api_key (string): Your API Key
            content (string): Email body in html (to use attributes to display
                dynamic values such as name, account number, etc. for ex. [%
                NAME %] for ATT_NAME , [% AGE %] for ATT_AGE etc.)
            mfrom (string): From email address
            recipients (string): Email addresses for recipients (multiple
                values allowed)
            subject (string): Subject of the Email
            att_name (string, optional): Specify attributes followed by ATT_
                for recipient to personalized email for ex. ATT_NAME for name,
                ATT_AGE for age etc. (Multiple attributes are allowed)
            attachmentid (string, optional): specify uploaded attachments id
                (Multiple attachments are allowed)
            bcc (string, optional): Email address for bcc
            clicktrack (bool, optional): set ‘0’ or ‘1’ in-order to disable or
                enable the click-track
            footer (bool, optional): Set '0' or '1' in order to include footer
                or not
            fromname (string, optional): Email Sender name
            opentrack (bool, optional): set open-track value to ‘0’ or ‘1’
                in-order to disable or enable
            replytoid (string, optional): Reply to email address
            tags (string, optional): To relate each message. Useful for
                reports.
            template (int, optional): Email template ID
            x_apiheader (string, optional): Your defined unique identifier

        Returns:
            mixed: Response from the API. Success | Failure

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/web.send.rest"

        # Process optional query parameters
        query_parameters = {
            "api_key": api_key,
            "content": content,
            "from": mfrom,
            "recipients": recipients,
            "subject": subject,
            "ATT_NAME": att_name,
            "attachmentid": attachmentid,
            "bcc": bcc,
            "clicktrack": clicktrack,
            "footer": footer,
            "fromname": fromname,
            "opentrack": opentrack,
            "replytoid": replytoid,
            "tags": tags,
            "template": template,
            "X-APIHEADER": x_apiheader
        }
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare the API call.
        http_request = self.http_client.get(query_url, headers=headers, query_parameters=query_parameters)

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body


    def send(self,data):
        return self.create_api_web_send_json(data)

    def create_api_web_send_json(self,
                                 data):
        """Does a POST request to /api/web.send.json.

        `Sending Mails` – This API is used for sending emails. Pepipost
        supports REST as well JSON formats for the input. This is JSON API.

        Args:
            data (Emailv1): Data in JSON format

        Returns:
            mixed: Response from the API. Success | Failure

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/web.send.json"
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8"
        }

        # Prepare the API call.
        http_request = self.http_client.post(query_url, headers=headers, parameters=APIHelper.json_serialize(data))

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body


