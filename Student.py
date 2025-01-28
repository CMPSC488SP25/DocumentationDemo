import pydoc

class Student:
    """Class to represent a Student object.

    Longer class info
    Longer class info

    Attributes:
        _name (String): The student's name.
        _student_id (String): The student's ID.
    """

    def __init__(self, name):
        """Initializes an instance of a Student.

        Args:
            name (String): The name assigned to this Student object.
        """
        self._name = name
        self._student_id = None

    def set_name(self, name: str):
        """Sets the name of the Student instance.

        Args:
            name: The name to be assigned to this Student instance.
        """
        self._name = name

    def get_name(self) -> str:
        """Gets the name of the Student instance.

        Returns:
            The name of the Student instance.
        """
        return self._name

    def set_id(self, student_id):
        """Sets the ID of the Student instance.

        Args:
            student_id (String): Sets the ID of the Student instance.

        Raises:
            ValueError: A non-numeric character was entered.
        """
        for char in student_id:
            if not char.isdigit():
                raise ValueError("ID cannot contain non-numeric characters.")
        self._student_id = student_id

    def get_id(self):
        """Gets the ID of the Student instance.

        Returns:
            _student_id (String): The ID of the Student instance.
        """
        return self._student_id

try:
    s1 = Student("Jane")
    s1.set_id("12345")
    print(s1.get_name(), s1.get_id())
except ValueError as e:
    print(e)

#pydoc.writedoc('Student')  # Used to generate an HTML documentation page
