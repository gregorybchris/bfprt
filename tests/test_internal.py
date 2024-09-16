import pytest
from bfprt.algo import insertion_sort, partition, select, swap


class TestInternal:
    def test_swap(self) -> None:
        items = [4, 1, 2, 5, 9, 8]
        swap(items, 2, 3)
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
        pivot_index = partition(items, 0, len(items) - 1, pivot_index)
        assert pivot_index == expected_index
        assert items == expected_items

    def test_select(self) -> None:
        for i in range(6):
            items = [4, 2, 1, 9, 5, 8]
            selected = select(items, 0, 5, i)
            sorted_items = [1, 2, 4, 5, 8, 9]
            assert selected == sorted_items[i]

    def test_insertion_sort(self) -> None:
        items = [4, 2, 9, 5, 8]
        insertion_sort(items, 0, 4)
        assert items == [2, 4, 5, 8, 9]
