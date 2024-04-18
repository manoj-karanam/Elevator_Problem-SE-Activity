class ElevatorController:
    def __init__(self, num_elevators, num_floors):
        """Initializes the controller with a given number of elevators and floors."""
    
    def call_elevator(self, floor, direction):
        """Requests an elevator to come to a specified floor. 
        Direction can be 'up' or 'down' indicating the passenger's desired direction."""
    
    def move_elevators(self):
        """Moves all elevators one step based on their current requests and directions."""
    
    def status(self):
        """Prints the status of all elevators (current floor, direction, and requests)."""
    
    def _assign_elevator(self, request):
        """Internal method to decide which elevator to send to a call request. 
        This might consider distance, direction, and current load."""
