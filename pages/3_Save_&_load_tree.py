import streamlit as st
from streamlit_condition_tree import condition_tree

from config import config

st.markdown(
    "When the component has a key, its tree is "
    "accessible through *st.session_state[key]*."
    "It can be entered as an input of another "
    "condition tree through the argument *tree*."
)


condition_tree(
    config,
    placeholder="Empty tree",
    key="tree"
)

tree = st.session_state["tree"]

condition_tree(
    config,
    tree=tree,
    placeholder="Empty tree",
)

st.subheader('Tree')
st.write(tree)

st.subheader('Code')
st.code("""
condition_tree(
    config,
    placeholder="Empty tree",
    key="tree"
)

tree = st.session_state["tree"]

condition_tree(
    config,
    tree=tree,
    placeholder="Empty tree",
)
""", "python")