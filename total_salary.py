def total_salary(path: str) -> int:
    '''

    :param path: path to the text file
    :return: total and average amount of salary
    '''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            total = sum(int(line.strip().split(',')[1]) for line in data)
            average = total / len(data)
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None


total, average = total_salary('salary_file.txt')
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
