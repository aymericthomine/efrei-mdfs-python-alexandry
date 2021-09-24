# BOOK API

Let's talk about book API with **NodeJS** and **React**.

## Utilisation (step by step) 

**To start**:

###### In shell, open the server folder.
> Then, run the command below:
```shell
$ npm install
```

###### In a second shell, open the client folder.
> Then, run the command below:
```shell
$ npm install
```

###### To seed the database :
> In the server folder, run the command below:
```shell
$ npm run seed
```

###### To start the server, open the server folder.
> Then, run the command below:
```shell
$ npm run server <port>
```

###### To start the client, open the client folder.
> Then, run the command below:
```shell
$ npm run client
```
> :warning: **If you have an error like:** ***Module not found: Can't resolve 'react-router-dom'***. 
###### run the command below in your client folder: 
```shell 
npm install -S react-router-dom
```

## Routes utilisation

|Method	|Route	|Description|
|-------|------|-----------|
|GET	| /books | this should respond with a list of all books.|
|POST	| /add-book	| this route should display a single pokemon's found on the daily pokedex.json|
|PUT	| /update-book/:nom | this route should add a new pokemon on the pokedex.|
|DELETE	| /delete-book/:id	| this route should allow you to delete a specific pokemon|

## Demo
![demo](https://i.ibb.co/9wnBcgy/Capture-d-e-cran-2021-09-24-a-15-22-04.png)
![demo](https://i.ibb.co/ChdhYtT/Capture-d-e-cran-2021-09-24-a-15-23-51.png)
![demo](https://i.ibb.co/5nVF1n3/Capture-d-e-cran-2021-09-24-a-15-24-15.png)

