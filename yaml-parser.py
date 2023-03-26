import yaml


def paths(some_dict, path=()):
    for key, value in some_dict.items():
        if (isinstance(value, dict)):
            key_path = path + (key + '.',)
        else:
            key_path = path + (key,) + (' : ',)
            var = str(key_path)
            for char in var:
                if char in " (),'":
                    var = var.replace(char, '')
            val = str(value)
            for char in val:
                if char in "\n":
                    val = val.replace(char, '')
            with open("D:/Yandex/vars.txt", "a", encoding="utf-8") as file:
                file.write(var + ' ' + val + '\n')
        yield key_path
        if hasattr(value, 'items'):
            yield from paths(value, key_path)


with open('D:/Yandex/key-vars.yaml', encoding='utf8') as f:
    data = yaml.full_load(f)

print(*paths(data['default']))
