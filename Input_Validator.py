class UserInputValidator: 
    def __init__(self):
        self.pos_int_list = []

    def validate_positive_integer(self, int_str: list):
        for i in int_str:
            if i.isdigit() and int(i) > 0:
                self.pos_int_list.append(int(i))
        return self.pos_int_list
    
    def msg_validation(self):
        if not self.pos_int_list:
            return "No valid positive integers were given by the user."
        else:
            return f"Valid positive integers are found: {self.pos_int_list}"
