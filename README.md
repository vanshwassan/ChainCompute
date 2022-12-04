<p align="center">
<img align="center" src="logo.png" width="200">
</p>

# ChainCompute

## Introduction

Run expensive computations off-chain and push the result back on-chain
</br>

## Run the API locally

### `python3 api.py`

## Project Structure
- ```backend/AirnodeConfig/config.json``` is the Graph'
s Airnode config file.

- ```/Contracts/``` Will have all the Contracts that the project uses. You can deply them via Remix or can initialize hardhat to deploy and write tests. 

- - The main `GraphQLRequster.sol` takes in the Airnode address of the deployed Graph Airnode, endpointID, encoded GraphQL query and sends the request to trigger the Airnode that will run the computation off-chain and send it back to the Requester through the callback function.

The page will reload when you make changes.\
You may also see errors in the console.