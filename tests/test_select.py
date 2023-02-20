import pytest

from bfprt.algo import insertion_sort, partition, select, select_fast, swap


class TestSelect:

    def test_swap(self):
        items = [4, 1, 2, 5, 9, 8]
        swap(items, 2, 3)
        assert items == [4, 1, 5, 2, 9, 8]

    @pytest.mark.parametrize("items, pivot_index, expected_items, expected_index", [
        ([4, 2, 1, 9, 5, 8], 0, [2, 1, 4, 9, 5, 8], 2),
        ([4, 2, 1, 9, 5, 8], 4, [4, 2, 1, 5, 8, 9], 3),
        ([2, 1], 0, [1, 2], 1),
        ([2, 1], 1, [1, 2], 0),
        ([3, 2, 1], 1, [1, 2, 3], 1),
    ])
    def test_partition(self, items, pivot_index, expected_items, expected_index):
        pivot_index = partition(items, 0, len(items) - 1, pivot_index)
        assert pivot_index == expected_index
        assert items == expected_items

    def test_select(self):
        for i in range(6):
            items = [4, 2, 1, 9, 5, 8]
            selected = select(items, 0, 5, i)
            sorted = [1, 2, 4, 5, 8, 9]
            assert selected == sorted[i]

    def test_insertion_sort(self):
        items = [4, 2, 9, 5, 8]
        insertion_sort(items, 0, 4)
        assert items == [2, 4, 5, 8, 9]

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
