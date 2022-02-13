#---Q5 - Part 4(a)
def findDigitSum1(num:int):
    temp_lis = [int(x) for x in str(num)]
    return sum(temp_lis)

# print(findDigitSum1(1071))



#---Q5 - Part 4(b)
def findDigitSum2(num:int):
    total_ans = 0
    ans = sum([int(x) for x in str(num)])
    total_ans += ans
    if len(str(ans)) > 1:
        var = findDigitSum2(ans)
        total_ans += var
    else:
        return total_ans
    return total_ans

# print(findDigitSum2(89))



#---Q5 - Part 5(a)
def findSquareDigitSum1(num:int):
    ans = sum([int(x)**2 for x in str(num)])
    return ans

# print(findSquareDigitSum1(12))



#---Q5 - Part 5(b)
def findSquareDigitSum2(num:int):
    total_ans = 0
    ans = sum([int(x)**2 for x in str(num)])
    total_ans += ans
    if len(str(ans)) > 1:
        var = findSquareDigitSum2(ans)
        total_ans += var
    else:
        return total_ans
    return total_ans

# print(findSquareDigitSum2(89))





#---Q8
class Optimization:
    def __init__(self,c:int,r:int) -> None:
        self.c = c #Initial cost
        self.icfm = c#Initial cost for maintenance
        self.r = r #Depreciation rate
        self.old_maintenance_list = []
        self.depreciation = (c/100)*r
        self.value_per_km_var = 50
        self.km = 6000

    def maintenance_cost(self,year,amount:None):
        initial_cost = self.icfm
        old_maintenance_list = self.old_maintenance_list
        if year == 1:
            return int(initial_cost/100)
        elif year <= 5:
            var = old_maintenance_list[int(year)-1] + int(initial_cost/100)
            return var
        else:
            var = old_maintenance_list[int(year)-1]*1.5
            return var
        
    def value_per_km(self,year):
        value = self.value_per_km_var + (self.value_per_km_var/100)*10
        self.value_per_km_var = value
        return value

    def optimise(self):
        depreciation = self.depreciation
        km = self.km
        self.old_maintenance_list.append(0)
        for i in range(15):
            # print(self.old_maintenance_list)
            # print(i)
            maintenance = self.maintenance_cost(i+1,None)
            self.old_maintenance_list.append(maintenance)
            cost = self.c - (depreciation + maintenance)
            self.c = cost
            value_per_km = self.value_per_km(i)
            value = km*value_per_km

            # print("\n\nYear:",i+1,"\nMaintenance:",maintenance,"\nDepreciation:",depreciation,"\nCost:",cost,"\nValue per km:",value_per_km,"\nValue:",value)

            if cost <= value:
                print(f"Year : {i+1} (You sell the car after {i+1} years)")
                return
        print("You sell the car after 15 years")


def optimise():
    print(
        '''
The following values are taken for the sample test case\n
Initial cost: 1,000,000
Depreciation rate: 5% every year\n
        '''
    )
    opt = Optimization(1000000,5)
    opt.optimise()

optimise()