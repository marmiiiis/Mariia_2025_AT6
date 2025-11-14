import Input_Validator

user_input_1 = ["0", "1", "-2", "3.14", "four", "5", "6"]
user_input_2 = ["-1", "-5", "hello", "0", "3.5", "8.0", "-10"]

validator1 = Input_Validator.UserInputValidator()
validator2 = Input_Validator.UserInputValidator()

input1_validation = validator1.validate_positive_integer(user_input_1)
input2_validation = validator2.validate_positive_integer(user_input_2)

result1 = print(validator1.msg_validation())
result2 = print(validator2.msg_validation())    