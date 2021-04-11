'use strict'
const AWS = require('aws-sdk');

// AWS.config.update({ region: "us-west-2"});

exports.handler = async (event, context) => {
//  const ddb = new AWS.DynamoDB({ apiVersion: "2012-10-08" });
 const documentClient = new AWS.DynamoDB.DocumentClient({ region: "us-west-2"}); 

 let responseBody = "";
 let statusCode = 0;

const {id} = JSON.parse(event.pathParameters);

 const params = {
	TableName: "Normas",
	Key: {
	    id: id
	    }
    };

      try {
        const data = await documentClient.delete(params).promise();
        responseBody = JSON.stringify(data);
        statusCode = 204;
      } catch (err) {
        responseBody = `Unable to delete normas: ${err}`;
        statusCode = 403;
      }

  const response = {
     statusCode: statusCode,
     headers: {
       "content-type": "application/json",
       "access-control-allow-origin": "*"
     },
     body: responseBody
  };

 return response;
};