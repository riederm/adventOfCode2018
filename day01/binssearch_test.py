from binsearch import bin_search

def test_bin_search():
    assert bin_search([1, 2, 3, 4, 5], 1)
    
def test_bin_search_found():
    assert bin_search([1, 6, 8, 11], 8)

def test_bin_search_not_found():
    assert not bin_search([1, 6, 8, 11], 7)

def test_bin_search_not_found1():
    assert not bin_search([1, 6, 8, 11], 1)

def test_bin_empty():
    assert not bin_search([], 1)
