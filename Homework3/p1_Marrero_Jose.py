# Name Jose Marrero ZNUMBER: Z23816617
# Problem 1

from typing import Any, Union

class NVector:
    """ this class is meant for working with vectors and their values """
    elements: list[Any]

    def __init__(self, *args: Any) -> None:
        """ sets up vector with the given values"""
        if len(args) == 1:
            self.elements = list(args[0])
        elif len(args) >= 2:
            self.elements = list(args)

    def __len__(self) -> int:
        """gets the number of elements in the vector"""
        return len(self.elements)

    def __getitem__(self, index: Union[int, slice]) -> Any:
        """gets value by using the index"""
        return self.elements[index]

    def __setitem__(self, index: Union[int, slice], value: Any) -> None:
        """changes the value of the vector at given index"""
        self.elements[index] = value

    def __str__(self) -> str:
        """ shows the vector as a string"""
        return str(self.elements)

    def __eq__(self, other: Any) -> bool:
        """checks if both vectors are equal"""
        if isinstance(other, NVector):
            return self.elements == other.elements
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        """ checks if both vectors are not equal"""
        return not self.__eq__(other)

    def __add__(self, other: Any) -> "NVector":

        """adds vectors or adds a number to the values"""
        result = []

        if isinstance(other, NVector):
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must have the same dimensions")
            
            for a, b in zip(self.elements, other.elements):
                result.append(a + b)

        elif isinstance(other, (int, float)):
            for x in self.elements:
                result.append(x + other)

        else:
            return NotImplemented

        return NVector(result)
 # Name Jose Marrero ZNUMBER: Z23816617
    def __radd__(self, other: Any) -> "NVector":
        """ handles addition when the number comes first in the operation"""
        return self.__add__(other)

    def __mul__(self, other: Any) -> Union["NVector", int, float]:
        """multiplies either vectors or by a number"""
        if isinstance(other, NVector):
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must have the same dimensions.")

            result = 0
            for a, b in zip(self.elements, other.elements):
                result += a * b

            return result

        elif isinstance(other, (int, float)):
            result = []
            for x in self.elements:
                product = x * other
                result.append(product)

            return NVector(result)

        else:
            return NotImplemented

    def __rmul__(self, other: Any) -> Union["NVector", int, float]:
        """handles multiplication if the number comes first in the operation"""
        return self * other

    @classmethod
    def zeros(cls, n: int) -> "NVector":
        """Create a vector containing n zeros."""
        return cls([0] * n)
# Jose Marrero ZNUMBER: Z23816617
def testif(
    b: bool,
    testname: str,
    msgOK: str = "",
    msgFailed: str = ""
) -> bool:
    """checks if the test passed or failed and prints the result"""
    if b:
        print("Success: " + testname + ": " + msgOK)
    else:
        print("Failed: " + testname + ": " + msgFailed)
    return b


def main() -> None:
    """test NVector class (including indexing, arithemetic, and error handling)"""
    v1 = NVector(1, 2, 3)
    v2 = NVector(4, 5, 6)

    testif(len(v1) == 3, "Vector length")
    testif(v1[0] == 1 and v1[-1] == 3, "Vector indexing")
    v1[0] = 5
    testif(v1[0] == 5, "Vector assignment")
    v1[0] = 1  

    testif(str(v1) == "[1, 2, 3]", "String representation")
    testif(v1 == NVector(1, 2, 3), "Vector equality")
    testif(v1 != v2, "Vector inequality")
    testif(v1 + v2 == NVector(5, 7, 9), "Vector addition")
    testif(v1 + 10 == NVector(11, 12, 13), "Scalar addition (right)")
    testif(10 + v1 == NVector(11, 12, 13), "Scalar addition (left/radd)")
    testif(v1 * v2 == 32, "Vector dot product")
    testif(v1 * 3 == NVector(3, 6, 9), "Scalar multiplication (right)")
    testif(3 * v1 == NVector(3, 6, 9), "Scalar multiplication (left/rmul)")
    testif(NVector.zeros(4) == NVector(0, 0, 0, 0), "Class method zeros()")
    testif(NVector([1, 2, 3]) == v1, "Constructor with list")
    testif(NVector((1, 2, 3)) == v1, "Constructor with tuple")

    v_test = NVector(1, 2, 3)
    v_test[-1] = 99
    testif(v_test.elements == [1, 2, 99], "Negative-index assignment")

    v_short = NVector(1, 2)
    
    try:
        _ = v1 + v_short
        testif(False, "__add__ dimension check", "", "Expected ValueError for mismatched dimensions")
    except ValueError:
        testif(True, "__add__ dimension check", "Correctly raised ValueError")

    try:
        _ = v1 * v_short
        testif(False, "__mul__ dimension check", "", "Expected ValueError for mismatched dimensions")
    except ValueError:
        testif(True, "__mul__ dimension check", "Correctly raised ValueError")


if __name__ == "__main__":
    main()
print("Jose Marrero ZNUMBER: Z23816617")