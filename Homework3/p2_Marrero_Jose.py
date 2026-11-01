# Problem 2: Parking Permit 
# Jose Marrero Z23816617
# Part (a)

class ParkingPermit:
    """Keeps track of parking permit info"""

    def __init__(self, owner: str, months: int, fees: dict[str, int]) -> None:
        """
        Initializes parking permit

        Parameters:
            owner: Name of owner

            months: # of months purchased.
            
            fees: dictionary containing parking permit prices
        """
        self.owner = owner
        self.months = months
        self.fees = fees

    def __str__(self) -> str:
        """Shows parking permit info into readable format."""
        return f"Parking Permit for {self.owner}: {self.months} months"

    def __repr__(self) -> str:
        """shows parking permit info into readable format (debugging)"""
        return f"ParkingPermit(owner={self.owner!r}, months={self.months}, fees={self.fees!r})"


# Part(b)

class StudentPermit(ParkingPermit):
    """Represents student parking permits that contain registered vehicles."""

    def __init__(self, owner: str, months: int,
                 fees: dict[str, int], vehicles: int) -> None:
        """
        Initializes a student parking permit.

        Parameters:
            owner: Name of the owner.
            months: # of months purchased.
            fees: dictionary containing parking permit prices
            vehicles: # of registered vehicles for the student permit
            
        """
        super().__init__(owner, months, fees)
        self.vehicles = vehicles
    # Jose Marrero ZNUMBER: Z23816617
    # Part (c)
    def cost(self) -> int:
        """Calculate the total cost of a student parking permit."""
        student_price = self.fees['student_monthly']
        extra_vehicle_fee = self.fees['extra_vehicle']
        extra_vehicles = max(0, self.vehicles - 1)

        total_cost = (student_price * self.months) + (extra_vehicle_fee * extra_vehicles)
        return total_cost

    # Part (d)
    def __str__(self) -> str:
        """returns readable description of the student parking permit"""
        return f"Student Parking Permit for {self.owner}: {self.months} months, {self.vehicles} vehicles"

    def __repr__(self) -> str:
        """returns a representation of the student permit for debugging"""
        return f"StudentPermit(owner={self.owner!r}, months={self.months}, fees={self.fees!r}, vehicles={self.vehicles})"


class FacultyPermit(ParkingPermit):
    """Represents a faculty parking permit with optional garage access."""

    def __init__(self, owner: str, months: int,
                 fees: dict[str, int], garage: bool) -> None:
        """
        Initialize a faculty parking permit.

        Parameters:
            owner: the name of the permit owner
            months: number of months purchased
            fees: a dictionary containing parking permit prices
            garage: whether garage access is included.
        """
        super().__init__(owner, months, fees)
        self.garage = garage

    
    def cost(self) -> int:
        """calculates the total cost of a faculty parking permit"""
        faculty_price = self.fees['faculty_monthly']
        garage_fee = self.fees['garage_monthly']

        total_cost = (faculty_price * self.months) + (garage_fee * self.months * self.garage)
        return total_cost

    def __str__(self) -> str:
        """returns description of the faculty parking permit in a readable format"""
        return f"Faculty Parking Permit for {self.owner}: {self.months} months, Garage: {self.garage}"

    def __repr__(self) -> str:
        """returns a representation of the faculty permit for debugging"""
        return f"FacultyPermit(owner={self.owner!r}, months={self.months}, fees={self.fees!r}, garage={self.garage})"

# Jose Marrero ZNUMBER: Z23816617
# Part (e)

def summarize_list(permits: list[ParkingPermit]) -> int:
    """
   prints the name and cost of permit owner
    parameter:
        permits: List containing student and faculty permits

    Return:
        the total revenue generated from all permits in the list.
    """
    total_revenue = 0

    for permit in permits:
        print(permit)
        print(f"{permit.owner}: ${permit.cost()}")
        total_revenue += permit.cost()

    return total_revenue


# Part (f)

def main() -> None:
    """shows parking permit summary and total revenue for a list of permits"""

    fees = {
        'student_monthly': 25,
        'faculty_monthly': 40,
        'extra_vehicle': 10,
        'garage_monthly': 15
    }

    student_permit = StudentPermit("John", 6, fees, 2)
    faculty_permit = FacultyPermit("Smith", 12, fees, True)

    permits = [student_permit, faculty_permit]

    print("Parking Permit Summary")
    total_revenue = summarize_list(permits)

    print(f"Total Revenue: ${total_revenue}")

    print("\nObject Representations:")
    print(repr(student_permit))
    print(repr(faculty_permit))


if __name__ == "__main__":
    main()
print("Jose Marrero ZNUMBER: Z23816617")