# Happy Bitcoin Pizza Day

This is an example of blind computation with [Nillion](https://docs.nillion.com/) to figure out how many pizzas to order for [Bitcoin Pizza Day](https://en.wikipedia.org/wiki/History_of_bitcoin). Check out the Nada program in src/determine_pizza_count.py

## Program logic

Alex wants to figure out how many pizzas to order for his 3 friends without revealing how many pieces of pizza each friend plans to eat. Alex also wants to know how many slices will be leftover.

## Run this example

0. Install the [Nillion SDK and Tools](https://docs.nillion.com/nillion-sdk-and-tools#installation)

1. Clone this repo

```bash
git clone <repo>
cd <folder>
```

2. Set up a Python virtual environment following [steps here](https://docs.nillion.com/nada#set-up-virtual-environment)

3. Run Nada program with test values set in tests/\*.yaml files

```bash
nada run order-perfect-amount
nada run order-with-leftovers
```

4. Optional: Create new tests to try different scenarios. Update these tests' yaml values and run the test

Generate test file:

```
nada generate-test --test-name <test-name> determine_pizza_count
```

Run test:

```
nada test <test-name>
```

5. Keep building! Add more programs, compile programs, and test programs following [nada docs](https://docs.nillion.com/nada#add-a-new-nada-program-to-the-project)

6. Get rewarded for building on Nillion. Check out Nillion Builder Bounties, linked in the Build section of the [Nillion docs](https://docs.nillion.com/)
