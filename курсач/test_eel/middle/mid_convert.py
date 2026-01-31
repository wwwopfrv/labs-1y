from back.convert import convert_value
import eel

@eel.expose
def convert_value_py(value:float, from_cur:str, to_cur:str)->float:
    return convert_value(value, from_cur, to_cur)



# функция convert_value_py принимает три аргумента: value (числовое значение), from_cur (исходная валюта) и to_cur (целевая валюта). 
# она вызывает функцию convert_value из модуля convert, которая выполняет конвертацию валюты. 
# декоратор @eel.expose позволяет функции convert_value_py быть доступной для вызова из JavaScript.
# заебись и в чем была праблема па итогу я не сохрнали файл 