
# Image Processing Lambda

Este proyecto tiene como finalidad el procesamiento de la imagen mediante una función lambda en AWS. Una vez almacenada la imagen se almacena en un bucket S3, de tal manera que se pueda obtener en cualquier momento, ademas que separamos el codigo y el servidor de procesamiento con el almacenamiento de archivos.


![Logo](https://github.com/andresnian/image_processing_request/blob/master/Image%20Processing%20Request.jpg)


## Tech Stack

**Microservicio:** Nodejs, Typescript, NestJs, MongoDB

**Lambda:** Python3, AWS, Boto3

## API Reference

#### Crear tarea y almacenamiento de imagen

```http
  POST /image-processing-lambda
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `path` | `string` | **Requerida**. Path del archivo en el bucket S3|
| `width` | `string` | **Requerida**.|
| `height` | `string` | **Requerida**.|

```javascript
curl --location --request POST 'https://hk9vrnhrgg.execute-api.us-east-1.amazonaws.com/default/image-processing-lambda' \
--header 'Content-Type: application/json' \
--data-raw '{
    "path": "images/foto-prueba1.jpg",
    "height": 800,
    "width": 800
}'
```

## Autor

- Eduardo Andres Niño Angarita

