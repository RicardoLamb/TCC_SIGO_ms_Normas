'use strict'
const AWS = require('aws-sdk');

// AWS.config.update({ region: "us-west-2"});

exports.handler = async (event, context) => {
//  const ddb = new AWS.DynamoDB({ apiVersion: "2012-10-08" });
 const documentClient = new AWS.DynamoDB.DocumentClient({ region: "us-west-2"}); 

 let responseBody = "";
 let statusCode = 0;

const {id, acoes, area, codigo, consequencias, descarte, descricao, fonte, normasobjects, objects, riscos, sigla, situation, titulo, usocorreto, vigencia} = JSON.parse(event.body);

 const params = {
	TableName: "Normas",
	Key: {
	    id: id
    },
    UpdateExpression: "set acoes = :acoes, area = :area, codigo = :codigo, consequencias = :consequencias, descarte = :descarte, descricao = :descricao, fonte = :fonte, normasobjects = :normasobjects, objects = :objects, riscos = :riscos, sigla = :sigla, situation = :situation, titulo = :titulo, usocorreto = :usocorreto, vigencia = :vigencia",
    ExpressionAttributeValues: {
        ":acoes": acoes,
        ":area": area,
        ":codigo": codigo,
        ":consequencias": consequencias,
        ":descarte": descarte,
        ":descricao": descricao,
        ":fonte": fonte,
        ":normasobjects": normasobjects,
        ":objects": objects,
        ":riscos": riscos,
        ":sigla": sigla,
        ":situation": situation,
        ":titulo": titulo,
        ":usocorreto": usocorreto,
        ":vigencia": vigencia        
    },
        ReturnValues: "UPDATED_NEW"
    };

      try {
        const data = await documentClient.update(params).promise();
        responseBody = JSON.stringify(data);
        statusCode = 204;
      } catch (err) {
        responseBody = `Unable to update normas: ${err}`;
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