import streamlit as st
from streamlit_condition_tree import condition_tree

from config import config


st.set_page_config(
    page_title='Streamlit-condition-tree demo',
    page_icon=':bookmark_tabs:'
)

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

return_type = st.selectbox(
    'Return type',
    ['queryString', 'mongodb', 'sql',
     'spel', 'elasticSearch', 'jsonLogic'],
    index=2
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

    st.code(code, 'python')
