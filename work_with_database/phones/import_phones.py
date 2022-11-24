import csv
from pprint import pprint


def import_phones(file_path):
    out_dict = []
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=r';')
        for row in reader:
            out_dict.append({
                'id': row['id'],
                'name': row['name'],
                'image': row['image'],
                'price': row['price'],
                'release_date': row['release_date'],
                'lte_exists': row['lte_exists'],
            })

    return out_dict


if __name__ == '__main__':
    pprint(import_phones('D:\Python projects\Django\Django_HW_3\work_with_database\phones.csv'))
