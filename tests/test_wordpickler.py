from pytest_mock import mocker
from cheatingbee.wordpickler import WordPickler


def test_init(mocker, word_dict_all_answers):
    mocker.patch('pickle.load', return_value=word_dict_all_answers)
    wp = WordPickler()
    assert wp.word_dict == word_dict_all_answers


def test_refine_word_dict_all_answers(
    mocker,
    word_dict_all_answers,
    nyt_answers
):
    mocker.patch('pickle.load', return_value=word_dict_all_answers)
    wp = WordPickler()
    mocker.patch.object(wp, '_WordPickler__save')
    wp.refine_word_dict(nyt_answers, nyt_answers)
    assert wp.word_dict == word_dict_all_answers


def test_refine_word_dict_missed_answers(
    mocker,
    word_dict_all_answers,
    solver_missed_answers,
    nyt_answers
):
    mocker.patch('pickle.load', return_value=word_dict_all_answers)
    wp = WordPickler()
    mocker.patch.object(wp, '_WordPickler__save')
    wp.word_dict.pop('gray')
    assert 'gray' not in wp.word_dict
    wp.refine_word_dict(solver_missed_answers, nyt_answers)
    assert wp.word_dict == word_dict_all_answers


def test_refine_word_dict_invalid_answers(
    mocker,
    word_dict_all_answers,
    solver_invalid_answers,
    nyt_answers
):
    mocker.patch('pickle.load', return_value=word_dict_all_answers)
    wp = WordPickler()
    mocker.patch.object(wp, '_WordPickler__save')
    wp.word_dict['graying'] = set('graying')
    assert wp.word_dict['graying'] == set('graying')
    wp.refine_word_dict(solver_invalid_answers, nyt_answers)
    assert wp.word_dict == word_dict_all_answers
