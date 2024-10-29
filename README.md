# Carriers ShipHero Backend Take Home Project

### Before you start working on the project please read these recommendations

- Please read the whole project specification carefully, and ask all the questions you feel would help you to do the most accurate solution you can. There's no such thing as a stupid question!
- You're always welcome to propose and discuss any improvements you find.
- We expect you invest around 4 hours of coding in this project once you have everything setup, if you find yourself investing more than that, consider stopping and we can talk about the general experience. However, it would be great if you can finish it!
- Adding to the previous point, you're still free to invest any time you want, but we'll define a maximum deadline of **3 days** if you are busy with other processes or work and need the extra time.
- Feel free to spend any time you find convenient before starting to code in order to catch up on technologies or details.

## Your Goal

There is a very simplistic model named `Order`. Assume it contains only one item that should
be sent in any box and method to a US domestic destination.

Your first task is to complete a few endpoints like create, list and get a particular Order.

Then, you will need to add two more endpoints in order to return a "quote" for an order, i.e the cost that could take us send the package from our warehouse in NY to the order's address. 

For this you should point to Fedex's REST API Sandbox Server and you can use the following documentation as reference:

- [FedEx API Catalog](https://developer.fedex.com/api/en-us/catalog.html)


Finally, complete the tests that are stubbed and add those you think are missing.

## Tech Stack

In this repo you'll find a simple implementation of a Flask API server. The tech stack we're using is this:

- Database: MongoDB
- Flask
- Docker
- Pytest

## How to install and run tests

To install the project you should just use basic docker-compose commands.

GitHub Actions will be run to validate these checks pass on each PR.

1. Clone this repository
2. Build the container: `docker compose build`
3. Run it: `docker compose up -d`
4. Run the tests (Needs a running container): `docker compose exec app pytest -sv`
5. You can run `docker compose exec app bash` to have a shell inside the container.
6. Example to run a single test: `docker compose exec app pytest -sv tests/test_endpoints.py::test_list_orders`

## How to submit your solution?

Please open a PR with your changes so we can review it and give you some feedback if there's place for it. Your PR must have:

- A description of your solution and design decisions you made, or anything you think it's worthwile to mention. Use the GitHub PR description for this
- The code for your solution
- CI tests and linting passing

## How to communicate with us?

We're going to invite you to our Slack channel as a guest, in this channel, all the people involved in the interviewing process will be present. You can post your questions or anything related to the process in there, and we'll answer as soon as possible.

## What comes after this project?

We'll be scheduling a call to ask questions about the project, your solution and the general experience.

**Good luck!**
