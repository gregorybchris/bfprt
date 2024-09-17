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

    def test_comparable(self) -> None:
        class Item:
            def __init__(self, value: int) -> None:
                self.value = value

            def __lt__(self, other: "Item") -> bool:
                return self.value < other.value

        items = [Item(4), Item(2), Item(1), Item(9), Item(5), Item(8)]
        k = 3
        selected_index = select_fast(items, k)
        sorted_items = [Item(1), Item(2), Item(4), Item(5), Item(8), Item(9)]
        assert items[selected_index].value == sorted_items[k].value
