config = {
    'fields': {
        'firstName': {
            'label': 'First name',
            'type': 'text',
            'mainWidgetProps': {
                'valuePlaceholder': 'Enter name',
            },
        },
        'age': {
            'label': 'Age',
            'type': 'number',
            'fieldSettings': {
                'min': 0,
                'max': 140
            },
            'preferWidgets': ['slider', 'rangeslider'],
        },
        'color': {
            'label': 'Favorite color',
            'type': 'select',
            'fieldSettings': {
                'listValues': [
                    {'value': 'yellow', 'title': 'Yellow'},
                    {'value': 'green', 'title': 'Green'},
                    {'value': 'orange', 'title': 'Orange'},
                ],
            },
        },
        'like_tomatoes': {
            'label': 'Likes tomatoes',
            'type': 'boolean',
            'operators': ['equal'],
        },
        'birth_date': {
            'label': 'Date of birth',
            'type': 'date',
            'operators': ['less', 'equal']
        }
    },
}