# 1.0 refactoring
a = 4  # change all variable name by right click one variable and click refactor -> rename
print(a)
print(a - 1)
print(a + 1)


# 1.1 refactor in function
def main():
    test = 0  # can rename at the same time with the rest in function because it is local variable.
    print(test)


# 2.0 shortcuts
# alt shift C: find all recent change
# ctrl D: duplicate current line.
# todo xxx can change the color of comments
# ctrl alt T for one variable can help you select what do you want to write in code.
run = True
run
# search everywhere: shift twice: calculate simple expressions
# drag your mouse while pressing Shift+Alt To select a rectangular piece of code
# next line: shift enter
# high level search: ctrl shift A
# comment or uncomment ctrl slash
# shift up twice to select current and previous line
# ctrl y: delete current line
# switch two line: alt shift up or down/ ctrl shift up or down
# to activate basic completion, press ctrl space
# use \ at the end of first line to link the second line
if 1 == 1 or \
    1 == 2:
    print(1)
# ctrl B to find where you define this function
# ctrl shift L to view json better.



