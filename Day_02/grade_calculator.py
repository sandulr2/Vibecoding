while True:

    # Get student details
    name = input("Enter student's name: ")

    if name.lower() == "exit":
        print("Exiting the grade calculator. Goodbye!")
        break

    # Get marks for three subjects
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    # Calculate the average
    average = (mark1 + mark2 + mark3) / 3

    # Determine Grade and Result
    if average >= 75:
        grade = "A"
        result = "Pass"
    elif average >= 60:
        grade = "B"
        result = "Pass"
    elif average >= 40:
        grade = "C"
        result = "Pass"
    else:
        grade = "N/A"
        result = "Fail"

    # Display results
    print("-" * 20)
    print(f"Student: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade:   {grade}")
    print(f"Status:  {result}")
    print("-" * 20)