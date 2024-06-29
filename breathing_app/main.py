def co2_breath_exercise(max_hold_seconds: int):
    if max_hold_seconds < 0:
        raise ValueError("Input can't be negative")
    else:
        hold_duration = max_hold_seconds / 2
        rest_periods = []
        for i in range(8):
            rest_periods.append(max_hold_seconds * (i/12))
            print(rest_periods[i])
    

def main():
    while True:
        try:
            max_hold_input = int(input("Enter your max breath hold in seconds (or type 'exit' to quit): "))
            
            if max_hold_input == 'exit':
                break

            # Convert to binary and print the result
            binary_result = decimal_to_binary(max_hold_input)
            print(f"The binary representation of {decimal_input} is: {binary_result}\n")
        
        except ValueError as ve:
            print(f"Error: {ve}\n. Please enter a valid number or type 'exit' to quit.\n")

if __name__ == "__main__":
    main()