class DateCalculator:
    def __init__(self, year: int, month: int, day: int):

        # Initialize the DateCalculator with a given date.
        #
        # Args:
        #     year (int): The year
        #     month (int): The month (1-12)
        #     day (int): The day of the month

        self.original_year = year
        self.original_month = month
        self.day = day
        self._adjust_date()
        
    def _adjust_date(self):
        # Adjust the month and year according to Zeller's Congruence rules.
        self.month = self.original_month
        self.year = self.original_year
        
        # Adjust for January and February
        if self.month < 3:
            self.month += 12
            self.year -= 1
            
    def calculate_weekday(self) -> int:

        # Calculate the day of the week using Zeller's Congruence.
        #
        # Returns:
        #     int: Day of week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)

        q = self.day
        m = self.month
        Y = self.year
        K = Y % 100  # year of century
        J = Y // 100  # zero-based century
        
        h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + (5 * J)) % 7
        return h
    
    def get_weekday_name(self) -> str:

        # Get the name of the weekday for the given date.
        #
        # Returns:
        #     str: Name of the weekday

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 
                'Wednesday', 'Thursday', 'Friday']
        return days[self.calculate_weekday()]