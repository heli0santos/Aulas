lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuu'

print (status)