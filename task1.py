def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                surname, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total += salary
                count += 1

        average = total / count if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print("File not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None



total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Total salary: {total}, Average salary: {average}")
