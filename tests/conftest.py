import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def restore_activity_participants():
    original_participants = {
        activity_name: activity["participants"][:]
        for activity_name, activity in activities.items()
    }

    yield

    for activity_name, participants in original_participants.items():
        activities[activity_name]["participants"] = participants
