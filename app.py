import streamlit as st
from streamlit_condition_tree import condition_tree


def tab1_code():
    code = f"""

from streamlit_condition_tree import condition_tree


config = {{
  'fields': {{
      'firstName': {{
        'label': 'First name',
        'type': 'text',
        'mainWidgetProps': {{
          'valuePlaceholder': 'Enter name',
        }},
      }},
      'age': {{
        'label': 'Age',
        'type': 'number',
        'fieldSettings': {{
          'min': 0,
          'max': 140
        }},
        'preferWidgets': ['slider', 'rangeslider'],
      }},
      'color': {{
        'label': 'Favorite color',
        'type': 'select',
        'fieldSettings': {{
          'listValues': [
              {{'value': 'yellow', 'title': 'Yellow'}},
              {{'value': 'green', 'title': 'Green'}},
              {{'value': 'orange', 'title': 'Orange'}},
          ],
        }},
      }},
      'like_tomatoes': {{
        'label': 'Likes tomatoes',
        'type': 'boolean',
        'operators': ['equal'],
      }},
      'birth_date': {{
        'label': 'Date of birth',
        'type': 'date',
        'operators': ['less', 'equal']
      }}
  }},
}}

condition_tree(
  config,
  return_type='{return_type}',
  placeholder='Empty tree'
)

# This shows the generated code for the query
st.write(condition_tree)

    """
    return code


def tab2_code():
    code = """
from streamlit_condition_tree import condition_tree
import streamlit as st


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

condition_tree(
  config,
  return_type='sql',
  placeholder='Empty tree',
  key='mytree'
)

# This shows the generated sql code
st.write(condition_tree)

# This shows the generated condition tree
st.write(st.session_state['mytree'])

    """

    return code


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

tree = {
    "type": "group",
    "children": [
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "firstName",
                "operator": "equal",
                "value": [
                    "Georges"
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "text"
                ]
            }
        },
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "age",
                "operator": "less_or_equal",
                "value": [
                    75
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "number"
                ]
            }
        },
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "like_tomatoes",
                "operator": "equal",
                "value": [
                    True
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "boolean"
                ]
            }
        },
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "birth_date",
                "operator": "less",
                "value": [
                    "2023-09-18"
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "date"
                ]
            }
        },
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "color",
                "operator": "select_equals",
                "value": [
                    "green"
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "select"
                ]
            }
        }
    ]
}

st.header('Condition Tree Builder')
st.markdown('')

tab1, tab2 = st.tabs(['Return value', 'Output tree'])

with tab1:
    return_type = st.selectbox(
        'Return type',
        ['queryString', 'mongodb', 'sql',
         'spel', 'elasticSearch', 'jsonLogic']
    )

    return_val = condition_tree(
        config,
        tree=tree,
        return_type=return_type,
        placeholder='Empty tree'
    )

    with st.expander('Return value', expanded=True):
        if isinstance(return_val, dict):
            st.write(return_val)
        else:
            st.code(return_val)

    with st.expander('Code'):
        st.code(tab1_code())

with tab2:
    return_val = condition_tree(
        config,
        return_type='sql',
        placeholder='Empty tree',
        tree=tree,
        key='mytree'
    )

    with st.expander('SQL', expanded=True):
        st.code(return_val, 'sql')

    with st.expander('Condition tree'):
        st.write(st.session_state['mytree'])

    with st.expander('Code'):
        st.code(tab2_code())
