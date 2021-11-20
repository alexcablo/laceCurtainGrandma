from src.my_calculations import my_mean

def test_mean():
    x = 2
    y = 2
    test_mean = my_mean.mean(2, 2)

    assert test_mean == 2

def test_mean_2():
    x = 2
    y = 2
    test_mean_2 = my_mean.mean_2(2, 2)

    assert test_mean_2 == 2