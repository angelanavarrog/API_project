# Project API

![portada](https://github.com/angelanavarrog/API_project/blob/master/image/API.jpg)

## Ojective

This project was defined during the Ironhack Bootcamp. Here you can find the [given instructions](https://github.com/Ironhack-Data-Madrid-Enero-2021/W6-api-sentiment-project).

The goal of this project is to **create an api** to store conversations that take place in different Whataspp groups. In my case, I based the content in the most typical conversation I have with friends and famly in this media.

## Procedure


For the above mentioned purpose, a **[database](https://github.com/angelanavarrog/API_project/blob/master/Inserting%20data.ipynb)** was created. It contains:
    - User name
    - Whatsapp group
    - Message
By adding it in MongoDB, we obtain an unique ID per user. [Here](https://github.com/angelanavarrog/API_project/tree/master/Files) are colleted the information in .json and .csv formats.

There have been created other **helpful documents** with functions that support the API construction:

- [Checking.py](https://github.com/angelanavarrog/API_project/blob/master/helpers/checking.py)
- [MongoConnection.py](https://github.com/angelanavarrog/API_project/blob/master/helpers/mongoConnection.py)
- [Users.py](https://github.com/angelanavarrog/API_project/blob/master/helpers/users.py)

Finally, an **[api.py](https://github.com/angelanavarrog/API_project/blob/master/api.py)** document has been created. 

With the objeective of testing it, and [.ipynb document](https://github.com/angelanavarrog/API_project/blob/master/testing%20API.ipynb) was created too.

## Resources

Some of the libraries used are:

- Flask
- MongoCollection
- pymongo
- bson