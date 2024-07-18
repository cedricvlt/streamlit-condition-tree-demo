import numpy as np
import pandas as pd
import streamlit as st
from streamlit_condition_tree import condition_tree, config_from_dataframe

st.set_page_config(
    page_title='Streamlit-condition-tree demo',
    page_icon=':bookmark_tabs:'
)


@st.cache_data
def load_data():
    df = pd.read_csv(
        'https://drive.google.com/uc?id=1phaHg9objxK2MwaZmSUZAKQ8kVqlgng4&export=download',
        index_col=0,
        parse_dates=['Date of birth'],
        date_format='%Y-%m-%d')
    df['Age'] = ((pd.Timestamp.today() - df['Date of birth']).dt.days / 365).astype(int)
    df['Sex'] = pd.Categorical(df['Sex'])
    df['Likes tomatoes'] = np.random.randint(2, size=df.shape[0]).astype(bool)
    return df


st.subheader('Initial DataFrame')
df = load_data()
st.dataframe(df)

config = config_from_dataframe(df)

tree = {
    "type": "group",
    "properties": {
        "conjunction": "OR"
    },
    "children": [
        {
            "type": "group",
            "properties": {
                "conjunction": "AND",
                "not": False
            },
            "children": [
                {
                    "type": "rule",
                    "properties": {
                        "fieldSrc": "field",
                        "field": "Age",
                        "operator": "between",
                        "value": [
                            15,
                            70
                        ],
                        "valueSrc": [
                            "value",
                            "value"
                        ],
                        "valueType": [
                            "number",
                            "number"
                        ]
                    }
                },
                {
                    "type": "rule",
                    "properties": {
                        "fieldSrc": "field",
                        "field": "`First Name`",
                        "operator": "like",
                        "value": [
                            "M"
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
                        "field": "`Last Name`",
                        "operator": "not_equal",
                        "value": [
                            "`First Name`"
                        ],
                        "valueSrc": [
                            "field"
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
                        "field": "`Likes tomatoes`",
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
                }
            ]
        },
        {
            "type": "group",
            "properties": {
                "conjunction": "AND",
                "not": False
            },
            "children": [
                {
                    "type": "rule",
                    "properties": {
                        "fieldSrc": "field",
                        "field": "`First Name`",
                        "operator": "not_like",
                        "value": [
                            "Goerges"
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
                        "field": "Sex",
                        "operator": "select_any_in",
                        "value": [
                            [
                                "Female",
                                "Male"
                            ]
                        ],
                        "valueSrc": [
                            "value"
                        ],
                        "valueType": [
                            "multiselect"
                        ]
                    }
                },
                {
                    "type": "rule",
                    "properties": {
                        "fieldSrc": "field",
                        "field": "`Date of birth`",
                        "operator": "between",
                        "value": [
                            "2023-09-19 22:26:16",
                            "2023-09-28 23:26:20"
                        ],
                        "valueSrc": [
                            "value",
                            "value"
                        ],
                        "valueType": [
                            "datetime",
                            "datetime"
                        ]
                    }
                }
            ]
        }
    ]
}

st.subheader('Condition tree')
query_string = condition_tree(
    config,
    tree=tree,
)
st.code(query_string)
st.markdown('')

st.subheader('Filtered DataFrame')
df = df.query(query_string)
st.dataframe(df)


with st.expander('Code'):
    st.code("""
    @st.cache_data
    def load_data():
        df = pd.read_csv(
            'https://drive.google.com/uc?id=1phaHg9objxK2MwaZmSUZAKQ8kVqlgng4&export=download',
            index_col=0,
            parse_dates=['Date of birth'],
            date_format='%Y-%m-%d')
        df['Age'] = ((pd.Timestamp.today() - df['Date of birth']).dt.days / 365).astype(int)
        df['Sex'] = pd.Categorical(df['Sex'])
        df['Likes tomatoes'] = np.random.randint(2, size=df.shape[0]).astype(bool)
        return df
    
    st.subheader('Initial DataFrame')
    st.dataframe(df)
    
    st.subheader('Condition tree')
    
    config = config_from_dataframe(df)
    query_string = condition_tree(config)
    
    st.code(query_string)
    
    st.subheader('Filtered DataFrame')
    df = df.query(query_string)
    st.dataframe(df)
    
    """, 'python')
