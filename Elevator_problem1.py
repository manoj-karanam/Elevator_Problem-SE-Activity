class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.is_door_open = False
        self.destination_floors = []
        self.direction = None  # 'up', 'down', or None

    def move(self):
        if not self.destination_floors:
            return
        target_floor = self.destination_floors[0]
        if self.current_floor < target_floor:
            self.current_floor += 1
            self.direction = 'up'
        elif self.current_floor > target_floor:
            self.current_floor -= 1
            self.direction = 'down'
        if self.current_floor == target_floor:
            self.open_doors()
            self.destination_floors.pop(0)
            if not self.destination_floors:
                self.direction = None
            self.close_doors()

    def request_floor(self, floor):
        if floor not in self.destination_floors:
            self.destination_floors.append(floor)
            self.destination_floors.sort()
        if floor > self.current_floor:
            self.direction = 'up'
        elif floor < self.current_floor:
            self.direction = 'down'

    def open_doors(self):
        self.is_door_open = True
        print(f"Elevator {self.id} at floor {self.current_floor} has opened its doors.")

    def close_doors(self):
        self.is_door_open = False
        print(f"Elevator {self.id} doors are closing.")

class User:
    def __init__(self, id, current_floor):
        self.id = id
        self.current_floor = current_floor
        self.is_inside_elevator = False

    def press_button(self, building, floor):
        print(f"User {self.id} at floor {self.current_floor} presses button for floor {floor}.")
        building.call_elevator(self, floor)

    def enter_elevator(self, elevator):
        if not elevator.is_door_open:
            print("Doors are not open, cannot enter.")
            return
        self.is_inside_elevator = True
        print(f"User {self.id} has entered elevator {elevator.id} at floor {self.current_floor}.")
        elevator.close_doors()

    def exit_elevator(self, elevator):
        if not elevator.is_door_open:
            print("Doors are not open, cannot exit.")
            return
        self.is_inside_elevator = False
        self.current_floor = elevator.current_floor
        print(f"User {self.id} has exited elevator {elevator.id} at floor {self.current_floor}.")
        elevator.close_doors()

class Building:
    def __init__(self, num_floors, num_elevators):
        self.elevators = [Elevator(i) for i in range(num_elevators)]
        self.num_floors = num_floors

    def call_elevator(self, user, destination):
        # Simple strategy for assigning the closest available elevator to the request
        best_choice = None
        for elevator in self.elevators:
            if best_choice is None or abs(elevator.current_floor - user.current_floor) < abs(best_choice.current_floor - user.current_floor):
                best_choice = elevator
        print(f"Elevator {best_choice.id} is called to floor {user.current_floor} for user {user.id}.")
        best_choice.request_floor(user.current_floor)  # Call to the user's floor
        best_choice.request_floor(destination)  # Then request the destination floor
        user.enter_elevator(best_choice)

    def move_elevators(self):
        for elevator in self.elevators:
            elevator.move()


def main():
    building = Building(10, 3)
    users = [User(1, 0), User(2, 3), User(3, 5)]

    # Simulated user interactions
    users[0].press_button(building, 5)
    building.move_elevators()
    users[1].press_button(building, 1)
    building.move_elevators()
    users[2].press_button(building, 8)
    building.move_elevators()

    # Continue moving elevators
    for _ in range(20):
        building.move_elevators()

if __name__ == "__main__":
    main()