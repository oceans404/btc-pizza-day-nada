# Blind Computation on Bitcoin Pizza Day  🍕🙈

This is an example of blind computation with [Nillion](https://docs.nillion.com/) to figure out how many pizzas to order for [Bitcoin Pizza Day](https://en.wikipedia.org/wiki/History_of_bitcoin).

## Program logic

Check out the [determine_pizza_count.py](./nada-pizza-programs/src/determine_pizza_count.py) Nada program.

Alex, the pizza purchaser, needs to figure out how many pizzas to order for his 3 friends without having any of the friends reveal how many pieces of pizza they plan to eat. Alex also wants to know how many slices will be leftover.

## Run this example

0. Install the [Nillion SDK and Tools](https://docs.nillion.com/nillion-sdk-and-tools#installation)

1. Clone this repo

    ```bash
    git clone https://github.com/oceans404/btc-pizza-day-nada.git
    cd btc-pizza-day-nada
    ```

2. Set up a Python virtual environment following [steps here](https://docs.nillion.com/nada#set-up-virtual-environment)

3. Change directory into the nada project folder 

    ```bash
    cd nada-pizza-programs
    ```

4. Build (compile) all Nada programs listed in the `nada-project.toml`

    ```bash
    nada build
    ```

5. Run Nada program with test values set in [tests folder](https://github.com/oceans404/btc-pizza-day-nada/tree/main/nada-pizza-programs/tests) yaml files

    ```bash
    nada run order-perfect-amount
    nada run order-with-leftovers
    ```

6. Optional: Create new tests to try different scenarios. Update these tests' yaml values and run the test

    Generate test file:

    ```bash
    nada generate-test --test-name <test-name> determine_pizza_count
    ```

    Run test:

    ```bash
    nada test <test-name>
    ```

7. Keep building! Add more programs, compile programs, and test programs following [nada docs](https://docs.nillion.com/nada#add-a-new-nada-program-to-the-project)

8. Get rewarded for building on Nillion. Check out Nillion Builder Bounties, linked in the Build section of the [Nillion docs](https://docs.nillion.com/)
