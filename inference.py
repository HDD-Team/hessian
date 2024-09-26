#!/home/user/matan/matan_venv/bin/python
import sympy as sp
import argparse
from sympy.parsing.sympy_parser import parse_expr

def cheat(f_str, symbols_str):
    ret = ""
    f = parse_expr(f_str)
    symbols = sp.symbols(symbols_str)
    diffs = [sp.diff(f, s) for s in symbols]
    for s, df in zip(symbols, diffs):
        ret += (f"Частная производная по {s} = {df}\n")
        

    critical_points = sp.solve(diffs, symbols, dict=True)
    ret += (f"Критические точки: {critical_points}")

    H = sp.Matrix([[sp.diff(df, s2) for s2 in symbols] for df in diffs])
    ret += (f"\nГессиан:\n{H}\n-----------------------------------------\n")
    
    for point in critical_points:
        sed = False
        ret += (f"\nКритическая точка {point}")
        H_num = H.subs(point)
        ret += (f"\nГессиан в точке:\n{H_num}")

        # Определение знаков главных миноров
        is_positive_definite = True
        is_negative_definite = True
        minors = []
        for k in range(1, len(symbols)+1):
            minor = H_num[:len(symbols)+1-k, :len(symbols)+1-k].det()
            ret += (f"\nМинор порядка {len(symbols)+1-k}: {minor}\n {H_num}")
            if minor < 0:
                sed = True
                break
            minors.append(minor)
                

        if sed:
            ret += ("\nседловая(не является экстр)\n-----------------------------------------\n")
        elif all(x > 0 for x in minors):
            ret += ("\nминимум\n-----------------------------------------\n")
        else:
            ret += ("\nмаксисум\n-----------------------------------------\n")
    return ret

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('func', help="Функция, например, 'x**2 + y**2'")
    # parser.add_argument('symbols', help="Переменные, например, 'x y'")
    # args = parser.parse_args()
    # print(args.func, args.symbols)
    #
    # cheat(args.func, args.symbols)
    print(cheat("-3*x**3+y**2+x+3+y+2", "x y"))
