favoritelanguages={'jen':['python','c','java'],
                   'sarah':['ruby','c++','HTML'],
                   'edward':['go','css','python'],
                   'phil':['python','haskell','ruby']}

for name, languages in favoritelanguages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.title()}")