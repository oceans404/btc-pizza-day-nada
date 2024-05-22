from nada_dsl import *

def nada_main():
    # input parties
    hungry_friend_1 = Party(name="Steph")
    hungry_friend_2 = Party(name="Charlie")
    hungry_friend_3 = Party(name="Lukas")

    # output party
    pizza_purchaser = Party(name="Alex")

    # each hungry friend secretly inputs the number of pieces of pizza they plan to eat
    steph_pieces = SecretInteger(Input(name="steph_pieces", party=hungry_friend_1))
    charlie_pieces = SecretInteger(Input(name="charlie_pieces", party=hungry_friend_2))
    lukas_pieces = SecretInteger(Input(name="lukas_pieces", party=hungry_friend_3))

    slices_per_pizza = Integer(8)
    pieces_for_friends = steph_pieces + charlie_pieces + lukas_pieces
    full_pizzas_needed = pieces_for_friends / slices_per_pizza
    additional_slices_needed = pieces_for_friends % slices_per_pizza

    # if additional slices are needed, order one extra full pizza
    total_pizzas = (additional_slices_needed > Integer(0)).if_else(full_pizzas_needed + Integer(1), full_pizzas_needed)
    leftover_slices = total_pizzas * slices_per_pizza - pieces_for_friends

    # the pizza puchaser knows how many pizzas to order and how many leftover slices to expect
    # without ever knowing how many pieces of pizza each friend plans to eat
    return [
        Output(total_pizzas, "total_pizzas", pizza_purchaser), 
        Output(leftover_slices, "leftover_slices", pizza_purchaser)
    ]