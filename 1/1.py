def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    

    if from_scale == 'C':
        celsius = value
    elif from_scale == 'F':
        celsius = (value - 32) * 5/9
    elif from_scale == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Неверная исходная шкала")
    

    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return celsius * 9/5 + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Неверная целевая шкала")


print(convert_temperature(100, 'C', 'F'))  
print(convert_temperature(32, 'F', 'C'))   
print(convert_temperature(0, 'C', 'K'))   
