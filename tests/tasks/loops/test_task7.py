from tasks.loops.task7 import insert_if_absent, merge


def test_insert_if_absent_existing_key_returns_value():
    value, result = insert_if_absent({"x": 2}, "x", 99)
    assert value == 2
    assert result == {"x": 2}


def test_insert_if_absent_missing_key_inserts_default():
    value, result = insert_if_absent({"x": 2}, "y", 99)
    assert value == 99
    assert result == {"x": 2, "y": 99}


def test_insert_if_absent_does_not_mutate_input():
    original = {"x": 2}
    insert_if_absent(original, "y", 99)
    assert original == {"x": 2}


def test_merge_from_dict():
    assert merge({"x": 2}, other={"y": 3}) == {"x": 2, "y": 3}


def test_merge_from_pairs():
    assert merge({"x": 2}, pairs=[("y", 3), ("z", 4)]) == {"x": 2, "y": 3, "z": 4}


def test_merge_from_kwargs():
    assert merge({"x": 2}, y=3) == {"x": 2, "y": 3}


def test_merge_all_sources_later_overrides_earlier():
    result = merge({"x": 0}, other={"x": 1}, pairs=[("x", 2)], x=3)
    assert result == {"x": 3}


def test_merge_does_not_mutate_input():
    original = {"x": 2}
    merge(original, other={"y": 3})
    assert original == {"x": 2}
