try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)

try:
    print(1/0)
except:
    print("wyjątek")
finally:
    print("co by się nie działo to ja się uruchamiam")

try:
    print("info")
except ValueError:
    print("wyjątek")
else:
    print("nie bylo wyjatku")


try:
    raise TypeError()
except TypeError:
    print("to było do przewidzenia...")