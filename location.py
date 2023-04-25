"""location class.

Represents a GPS location in terms of degrees latitude and longitude.

Author Nancy Harris - Alvin Chao python translation
Version V1 - 11/2011 V2- Python 4/2022
"""


class Location:
    """Location."""

    def __init__(self, latitude, longitude, location=None):
        """Location Constructor.

        Args:
            latitude(float):  The latitude in degrees
            longitude(float):  The longitude in degrees
            location(location): another location.
        """
        if location is not None:
            #  make copy of other
            self.latitude = location.latitude
            self.longitude = location.longitude
        else:
            self.latitude = latitude
            self.longitude = longitude

    def equals(self, other):
        """Check if the two values within .000001 of each other.

        Args:
            other (location): another location

        Returns:
            bool: true if the two values are the same, false otherwise
        """
        return (self.latitude - other.latitude <= .000001
                and self.longitude - other.longitude <= .000001)

    def __str__(self):
        """toString.

        Returns:
            txt (string): text representation.
        """
        txt = "{:.6f}{:6f}"
        return txt.format(self.latitude, self.longitude)


JMU = Location(38.435427, -78.872942)
ISAT = Location(38.434663, -78.863732)

