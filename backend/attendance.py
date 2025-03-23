from typing import List,Set

class Attendance:
    def __init__(self, name, group):
        self.name:str = name
        self.group:Set[str] = set(group)
        self.group.add(name)

    def __str__(self):
        return f"{self.name} attended with {', '.join(self.others)}"


class Session:
    def __init__(self, name):
        self.name:str = name
        self.attendance:Set[Attendance] = set()
        self.largest_group:Set[str] = set()
        

    def __str__(self):
        return f"Session {self.name} had {len(self.largest_group)} attendances"
    
    def mark_attendances(self) -> Set[str]:
        for attendance in self.attendance:
            if len(attendance.group) > len(self.largest_group):
                self.largest_group = attendance.group
        

    def add_attendance(self, attendance:Attendance):
        if self.attendance:
            for att in attendance.group:
                for att2 in self.attendance:
                    if att in att2.group:
                        att2.group = att2.group.union(attendance.group)
                        return
        self.attendance.add(attendance)


if __name__ == "__main__":
    session = Session("Session 1")
    session.add_attendance(Attendance("John", ["John", "Jane"]))
    session.add_attendance(Attendance("Jane", ["John", "Jane","Doe"]))
    session.add_attendance(Attendance("Doe", ["Doe"]))
    session.add_attendance(Attendance("Alice", ["Alice", "Bob","John"]))
    session.add_attendance(Attendance("Bob", ["Alice", "Bob"]))
    session.add_attendance(Attendance("Charlie", ["Charlie", "Eve","Alice"]))
    session.add_attendance(Attendance("Eve", ["Charlie", "Eve"]))
    print(session)
    session.mark_attendances()
    print(session)
    print(session.largest_group)
