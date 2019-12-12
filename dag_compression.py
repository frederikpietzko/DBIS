from string import ascii_uppercase
from collections import defaultdict


non_termanals = iter(ascii_uppercase)


def get_non_terminal(grammar: dict, RHS: str) -> (dict, str):
    nt = next(non_termanals)
    grammar[nt] = RHS
    return grammar, nt


def string_2_grammar(input_str: str) -> dict:
    grammar = {}

    while len(input_str) > 1:
        closing_index = input_str.find(')')
        open_inex = input_str.rfind('(', 0, closing_index) - 1
        sub_tree = input_str[open_inex:closing_index +1 ]
        grammar, nt = get_non_terminal(grammar, sub_tree)
        input_str = input_str.replace(sub_tree, nt)

    return grammar


def compute_calls(grammar: dict) -> dict:
    
    freq = defaultdict(int)
    for rhs in grammar.values():
        nt1 = rhs[2]
        nt2 = rhs[4]
        freq[nt1] += 1
        freq[nt2] += 1
    del freq['-']
    freq[sorted(grammar.keys())[-1]] = 0
    return freq


def prune(grammar: dict, calls:dict) -> dict:
    rules_called_once,_ = zip(*list(filter(lambda x: x[1] == 1, calls.items())))
    rule_calling = lambda: list(filter(lambda x: rule in x[1], grammar.items()))[0]
    for rule in rules_called_once:
        nt_calling, call = rule_calling()
        call = call.replace(rule, grammar[rule])
        grammar[nt_calling] = call
        del grammar[rule]
    return grammar



if __name__ == "__main__":
    test_tree =  "q(r(-,-),r(-,-))"
    grammar = string_2_grammar(test_tree)
    test_grammar = {'A':'r(-,-)', 'B':'q(-,A)', 'D':'p(A,C)', 'C':'f(-,B)'}
    calls = compute_calls(test_grammar)
    print(grammar)
    print(calls)
    print(prune(test_grammar, compute_calls(test_grammar)))
