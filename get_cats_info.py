def get_cats_info(path: str) -> list:
    '''

    :param path: path to the text file
    :return: a list of dictionaries where each dictionary contains information about one cat
    '''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            cats_list = []
            for cat in data:
                cats = {}
                cats['id'], cats['name'], cats['age'] = cat.strip().split(',')
                cats_list.append(cats)
        return cats_list

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
