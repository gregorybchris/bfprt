from bfprt import select_fast


class TestSelectFast:

    def test_select_fast_small(self):
        for i in range(5):
            items = [4, 2, 1, 9, 8]
            selected_index = select_fast(items, 0, 4, i)
            sorted = [1, 2, 4, 8, 9]
            assert items[selected_index] == sorted[i]

    def test_select_fast(self):
        for i in range(6):
            items = [4, 2, 1, 9, 5, 8]
            selected_index = select_fast(items, 0, 5, i)
            sorted = [1, 2, 4, 5, 8, 9]
            assert items[selected_index] == sorted[i]
