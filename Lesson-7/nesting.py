# json

users= (
    {
        'name': 'Makhmood',
        'lastname': 'Salimov',
        'friends': ['Joshqin', 'Fara'],
        'marks': {
            'math': 5,
            'history': 3,
            'izo': 3,
            'fizra': 4
        }
    },
    {
        'name': 'Faraa',
        'lastname': 'Qadirov',
        'friends': ['FOFO', 'JOJO'],
        'marks': {
            'math': 4,
            'history': 2,
            'izo': 5,
            'fizra': 5
        }
    }
)


math = fizra = 0
for user in users:
        print(user.get('name'))
        print(user.get('marks').get('math'))
        math += user.get('marks').get('math')
        print(user.get('marks').get('fizra',0))
        fizra += user.get('marks').get('fizra', 0)



average_math = round(math / len(users),2)
print(average_math)


print(users)