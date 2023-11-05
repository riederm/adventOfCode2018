class BinTree:
    def __init__(self, print_debug = False):
        self.print_debug = print_debug
        self.data = []

    def _print_entries(self):
        for date in self.data:
            print(f"{date}")
        
    def add(self, number):
        if len(self.data) == 0:
            self.data.insert(0, number)
            return
        if len(self.data) == 1:
            if self.data[0] > number:
                self.data.insert(0, number)
            elif self.data[0] < number:
                self.data.append(number)
            return
        
        #at least two elements are in the array
        ret_val = self._binary_search_(number, len(self.data) - 1, 0)
        if ret_val[0] == True:
            if self.print_debug == True:
                print(f"Element {number} is alread at pos {ret_val[1]} in set")
            return #entry is already in set
        elif ret_val[0] == False:
            if self.print_debug == True:
                print(f"Inserted element {number} at position {ret_val[1]}")
            self.data.insert(ret_val[1], number)
            
        
    def __contains__(self, number):
        if len(self.data) > 1:
            return self._binary_search_(number, len(self.data) - 1, 0)[0]
        elif len(self.data) == 1:
            return self.data[0] == number 
        else:
            return False

    def _binary_search_(self, search_value, upper_bound, lower_bound):
        """returns a tuple for the searched object. First entry is if the object is in the set,
        second entry is the point where it was found or where it should be inserted"""
        #cornercase for adjacent objects
        if lower_bound == upper_bound - 1:
            #is in list
            if self.data[lower_bound] == search_value:
                return True, lower_bound
            elif self.data[upper_bound] == search_value:
                return True, upper_bound
            else: #not found, search where it should be inserted
                if search_value > self.data[upper_bound]:
                    return False, upper_bound + 1
                elif search_value < self.data[lower_bound]:
                    return False, lower_bound - 1
                else:
                    return False, upper_bound
                
        #general binary search function
        middle = (int)((upper_bound + lower_bound) / 2)
        middle_data = self.data[middle]
        if middle_data == search_value:
            return True, middle
        elif middle_data < search_value:
            return self._binary_search_(search_value=search_value, upper_bound=upper_bound, lower_bound=middle)
        elif middle_data > search_value:
            return self._binary_search_(search_value=search_value, upper_bound=middle, lower_bound=lower_bound)


if __name__ == "__main__":
    
    bt = BinTree(print_debug=True)

    for i in range(1,35,3):
        bt.add(i)

    bt.add(12)
    bt.add(13)
    bt.add(14)

    bt._print_entries()

    print(f"31? should  be true: {bt.__contains__(31)}")
    print(f"30? should be false: {bt.__contains__(30)}")







        