import pytest
from app.calculator import calculate_macros


@pytest.mark.parametrize(
    ("goal", "expected"),
    [
        ("cut", {"calories": 2459, "protein": 160, "fat": 64, "carbs": 311}),
        ("maintain", {"calories": 2759, "protein": 160, "fat": 64, "carbs": 386}),
        ("bulk", {"calories": 3059, "protein": 160, "fat": 64, "carbs": 461}),
    ],
)
def test_calculate_macros_for_goals(goal, expected):
    result = calculate_macros(
        weight=80,
        height=180,
        age=30,
        activity_level="medium",
        goal=goal,
    )

    assert result == expected


def test_calculate_macros_uses_low_activity_by_default():
    result = calculate_macros(
        weight=80,
        height=180,
        age=30,
        activity_level="unknown",
        goal="maintain",
    )

    assert result == {"calories": 2136, "protein": 160, "fat": 64, "carbs": 230}
