import pytest


@pytest.fixture
def required_letters():
    '''Returns a Set containing todays required letters'''
    return set('y')


@pytest.fixture
def optional_letters():
    '''Returns a Set contining todays optional letters'''
    return set('acginr')


@pytest.fixture
def nyt_answers():
    '''Returns a Set containing todays answers'''
    return set([
        'gray',
        'craggy',
        'yarn',
        'carrying',
        'canary',
        'granary',
        'crying',
        'carry',
        'grainy',
        'cranny',
        'cagy',
        'cyan',
        'canny',
        'nary',
        'nanny',
        'cynic',
        'arraying',
        'granny',
        'array',
        'racy',
        'airy',
        'angry',
        'raying',
        'rangy',
    ])


@pytest.fixture
def solver_missed_answers(nyt_answers):
    '''Returns a Set containing todays answers'''
    nyt_answers.remove('gray')
    return nyt_answers


@pytest.fixture
def solver_invalid_answers(nyt_answers):
    '''Returns a Set containing todays answers'''
    nyt_answers.add('graying')
    return nyt_answers


@pytest.fixture
def word_dict_all_answers(nyt_answers):
    '''Returns a Dictionary of all answers with the word as the key
    and a set of the words letters as the value
    '''
    return {x: set(x) for x in nyt_answers}


@pytest.fixture
def word_dict_partial_answers(word_dict_all_answers):
    word_dict_all_answers.pop('gray')
    return word_dict_all_answers
