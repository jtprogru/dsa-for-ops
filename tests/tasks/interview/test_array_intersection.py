import pytest

from tasks.interview.array_intersection import array_intersection


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5], []),
        ([], [1, 2], []),
    ],
)
def test_array_intersection(nums1, nums2, expected):
    # Порядок результата не специфицирован — сравниваем как мультимножества.
    assert sorted(array_intersection(nums1, nums2)) == sorted(expected)
