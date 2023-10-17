from blackjack import calculate_score, compare
from termcolor import colored

def test_calculate_score():
    tests = []
    #Loop
    for element in tests:
        calculate_score(hand)
    hands = []
    expected_values = []
    test_names = []
    test_names.append("Blackjack 1")
    hands.append([11, 10])
    expected_values.append(0)
    test_names.append("Blackjack 2")
    hands.append([10, 11])
    expected_values.append(0)
    test_names.append("1 Ace with value of 11")
    hands.append([11, 9])
    expected_values.append(20)
    test_names.append("1 Ace with value of 1")
    hands.append([1, 9, 10])
    expected_values.append(20)
    test_names.append("Busted version")
    hands.append([1, 9, 10, 5])
    expected_values.append(25)
    test_names.append("2 Aces with value 11 & 1")
    hands.append([1, 9, 11])
    expected_values.append(21)
    test_names.append("2 Aces with values 1")
    hands.append([10, 5, 1, 11])
    expected_values.append(17)
    test_names.append("Busted version")
    hands.append([10, 5, 1, 1, 8])
    expected_values.append(25)
    test_names.append("3 Aces with values 11, 1 & 1")
    hands.append([11, 5, 1, 11])
    expected_values.append(18)
    test_names.append("3 Aces with values 1")
    hands.append([10, 5, 1, 1, 11])
    expected_values.append(18)
    test_names.append("Busted version")
    hands.append([10, 5, 1, 1, 1, 7])
    expected_values.append(25)
    test_names.append("No aces")
    hands.append([10, 5])
    expected_values.append(15)
    test_names.append("Busted version")
    hands.append([10, 5, 10])
    expected_values.append(25)

    for i in range(len(test_names)):
        tests.append([test_names[i], hands[i], expected_values[i], calculate_score(hands[i])])
    for test in tests:
        if test[2] == test[3]:
            result = "PASS"
            color = "green"
        else:
            result = "FAIL"
            color = "red"
        print(colored(f"{test}: {result}", color))

def test_compare():
    tests = []
    test_names = []
    user_scores = []
    computer_scores = []
    expected_values = []

    test_names.append("Same score")
    user_scores.append(10)
    computer_scores.append(10)
    expected_values.append(0)
    test_names.append("Computer blackjack")
    user_scores.append(12)
    computer_scores.append(0)
    expected_values.append(-1)
    test_names.append("User blackjack")
    user_scores.append(0)
    computer_scores.append(20)
    expected_values.append(1)
    test_names.append("Both blackjack")
    user_scores.append(0)
    computer_scores.append(0)
    expected_values.append(-1)
    test_names.append("User busted")
    user_scores.append(24)
    computer_scores.append(20)
    expected_values.append(-1)
    test_names.append("Computer busted")
    user_scores.append(20)
    computer_scores.append(25)
    expected_values.append(1)
    test_names.append("Nobody busted, player wins")
    user_scores.append(19)
    computer_scores.append(17)
    expected_values.append(1)
    test_names.append("Nobody busted, computer wins")
    user_scores.append(19)
    computer_scores.append(20)
    expected_values.append(-1)

    for i in range(len(test_names)):
        tests.append([test_names[i], user_scores[i], computer_scores[i],
                      expected_values[i],
                      compare(user_scores[i], computer_scores[i])])
    for test in tests:
        if test[3] == test[4]:
            result = "PASS"
            color = "green"
        else:
            result = "FAIL"
            color = "red"
        print(colored(f"{test}: {result}", color))

print("Test 1, test_calculate_score")
test_calculate_score()
print("\nTest 2, test_compare")
test_compare()
