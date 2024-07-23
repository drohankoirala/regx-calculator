import re

expressions = ["/", "*", "+", "-", "%"]


def get_expression_val(text):
    for lkj in [r"\(-?\d+\.?\d*[--rep--]?(?:-?\d+\.?\d*[--rep--]?)*\)", r"(-?\d+\.?\d*[--rep--]-?\d+\.?\d*)"]:
        for lkg in expressions:
            lkg = lkj.replace("--rep--", lkg)
            jhg = re.search(lkg, text)
            if jhg:
                return jhg.group()


while True:
    inp = input("\n: ").replace(" ", '')
    og = inp
    while True:
        lp = get_expression_val(inp)
        if lp:
            inp = inp.replace(lp, str(eval(lp)))
            continue
        if [_ for _ in expressions if _ in inp]:
            print("Expected a proper Value with Syntax for calculation, Got too unrealistic value!")
            break
        print("~", inp)
        break
