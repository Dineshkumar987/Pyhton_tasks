class Result:
    def calculate(self, *marks):
        # accept variable number of marks and print their total
        if not marks:
            print("No marks provided")
            return
        total = sum(marks)
        print("Total:", total)


r = Result()
r.calculate(80, 90)
r.calculate(80, 90, 85)
r.calculate(80, 90, 85, 70)