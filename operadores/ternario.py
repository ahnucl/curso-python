lockdown = True
grana = 30
status = 'Em casa' if lockdown and grana <= 100 else 'Batendo perna'

print(status)
