from __future__ import annotations

from datetime import time
from typing import NewType


class Schedule:
    pass


class DaySchedule:
    pass


class DayScheduleItem:
    starts_time: time
    ends_time: time
    subject_name: SubjectName
    teacher_name: TeacherName
    room: Room


Room = NewType("Room", str)
TeacherName = NewType("TeacherName", str)
SubjectName = NewType("SubjectName", str)
