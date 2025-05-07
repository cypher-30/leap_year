class DateCalculator:
    DAYS = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    def __init__(self, year: int, month: int, day: int):
        if not (1 <= month <= 12):
            raise ValueError("Month must be in 1..12")
        if not (1 <= day <= 31):
            raise ValueError("Day must be in 1..31") # Basic check; doesn't validate actual calendar correctness
        self.year = year
        self.month = month
        self.day = day

    def _zeller_weekday(self) -> int:
        m, y = self.month, self.year
        if m < 3:
            m += 12
            y -= 1
        q = self.day
        K = y % 100
        J = y // 100
        return (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    def get_weekday_name(self) -> str:
        return self.DAYS[self._zeller_weekday()]


# Example usage:
if __name__ == "__main__":
    date = DateCalculator(2025, 5, 6)
    print("Weekday:", date.get_weekday_name())
