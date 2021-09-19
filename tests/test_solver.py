from cheatingbee.solver import Solver


def test_correct_answers(
    required_letters,
    optional_letters,
    nyt_answers,
    word_dict_all_answers
):
    assert nyt_answers == Solver.solve(
        required_letters, optional_letters, word_dict_all_answers)


def test_partial_answers(
    required_letters,
    optional_letters,
    nyt_answers,
    word_dict_partial_answers
):
    assert nyt_answers != Solver.solve(
        required_letters, optional_letters, word_dict_partial_answers)


def test_empty_params():
    assert not Solver.solve(set(), set(), {})
