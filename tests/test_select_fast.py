from bfprt import select_fast


class TestSelectFast:
    def test_select_fast_small(self) -> None:
        n_items = 5
        for k in range(n_items):
            items = [4, 2, 1, 9, 8]
            selected_index = select_fast(items, k)
            sorted_items = [1, 2, 4, 8, 9]
            assert items[selected_index] == sorted_items[k]

    def test_select_fast(self) -> None:
        n_items = 6
        for k in range(n_items):
            items = [4, 2, 1, 9, 5, 8]
            selected_index = select_fast(items, k)
            sorted_items = [1, 2, 4, 5, 8, 9]
            assert items[selected_index] == sorted_items[k]
