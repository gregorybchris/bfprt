import pytest
from bfprt.algo import _insertion_sort, _partition, _select, _swap


class TestInternal:
    def test_swap(self) -> None:
        items = [4, 1, 2, 5, 9, 8]
        _swap(items, 2, 3)
        assert items == [4, 1, 5, 2, 9, 8]

    @pytest.mark.parametrize(
        ("items", "pivot_index", "expected_items", "expected_index"),
        [
            ([4, 2, 1, 9, 5, 8], 0, [2, 1, 4, 9, 5, 8], 2),
            ([4, 2, 1, 9, 5, 8], 4, [4, 2, 1, 5, 8, 9], 3),
            ([2, 1], 0, [1, 2], 1),
            ([2, 1], 1, [1, 2], 0),
            ([3, 2, 1], 1, [1, 2, 3], 1),
        ],
    )
    def test_partition(self, items: list[int], pivot_index: int, expected_items: list[int], expected_index: int):
        pivot_index = _partition(items, 0, len(items) - 1, pivot_index)
        assert pivot_index == expected_index
        assert items == expected_items

    def test_select(self) -> None:
        n_items = 6
        for k in range(n_items):
            items = [4, 2, 1, 9, 5, 8]
            selected = _select(items, 0, 5, k)
            sorted_items = [1, 2, 4, 5, 8, 9]
            assert selected == sorted_items[k]

    def test_insertion_sort(self) -> None:
        items = [4, 2, 9, 5, 8]
        _insertion_sort(items, 0, 4)
        assert items == [2, 4, 5, 8, 9]
