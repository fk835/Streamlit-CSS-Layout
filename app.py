import streamlit as st
import numpy as np
import pandas as pd

# set initial page configuration
st.set_page_config(page_title='Template 1', # page title in browser tab
                   page_icon=':bar_chart:', # icon in browser tab
                   layout='wide', # page layout setting
                   initial_sidebar_state='collapsed', # collapse left sidebar by default
                   )

# Embed custom CSS directly
st.markdown("""
<style>
       
</style>
""", unsafe_allow_html=True)


# HTML injection
st.html(
    "<h1><span style='text-decoration: line-through double red;'>Oops</span>!</h1>"
)

# define layout elements
header = st.container(border=False)
sidebar, content = st.columns([0.2, 0.8], border=False)
footer = st.container(border=False)

# Header
with header:
    st.html("""
        <div id="header">
            <h1>We can put a header up here!</h1>
            <p>Appearance leaves something to be desired, but we can use our own CSS.</p>
        </div>
    """)

# Test the built-in sidebar (uses same sidebar as page nav)
with st.sidebar:
    st.write('Built-in sidebar test')

# Test using columns to make my own sidebar
with sidebar:
    with st.form('Sidebar form'):
        st.write('Hello, sidebar!')
        st.write('This is a form. A reload is only triggered when the form is submitted.')
        
        # Checkboxes
        st.checkbox(label='Checkbox 1')
        st.checkbox(label='Checkbox 2')
        st.checkbox(label='Checkbox 3')
        
        # Pills
        st.pills('Pill selection',
                 options=['Option 1', 'Option 2', 'Option 3', 'Option 4'])
        
        # Multiselects
        st.multiselect(label='Multiselect',
                       options=['Option 1', 'Option 2', 'Option 3'])
        
        # Slider
        st.slider(label='Slider',
                  min_value=0,
                  max_value=10,
                  step=1)
        
        # Button to submit sidebar form
        st.form_submit_button('Apply Selection')
    
    with st.container(border=True):
        st.write('The sidebar can have elements outside of the form.')
        st.write('Interacting with these elements immediately triggers a reload.')
        st.button('Button 1')
        st.button('Button 2')

# Page content
with content:     
    # Show some sample content        
    st.markdown('## Example content: table')    
    st.dataframe(pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD')))
    st.markdown("""
                ## More content
                Here are a couple of other dataframes, which are used to illustrate the behavior of the
                footer and sidebar when more content is shown.
                """)
    st.dataframe(pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD')))

# Footer
with footer:
    st.html("""
        <div class="footer">
            <div style="display: flex; justify-content: space-between;">
                <div><input type="checkbox" id="checkbox1"><label for="checkbox1">Checkbox 1</label></div>
                <div><input type="checkbox" id="checkbox2"><label for="checkbox2">Checkbox 2</label></div>
                <div><input type="checkbox" id="checkbox3"><label for="checkbox3">Checkbox 3</label></div>
                <div><input type="checkbox" id="checkbox4"><label for="checkbox4">Checkbox 4</label></div>
            </div>
        </div>
    """)

# footer
# with footer:   
#     st.markdown("""
#                 <div id="footer">
#                     <div style="display: flex; justify-content: space-around;">
#                         <div>
#                             <input type="checkbox" id="scales" name="scales" checked />
#                             <label for="scales">Checkbox 1</label>
#                         </div>
#                         <div>
#                             <input type="checkbox" id="scales" name="scales" checked />
#                             <label for="scales">Checkbox 2</label>
#                         </div>
#                         <div>
#                             <input type="checkbox" id="scales" name="scales" checked />
#                             <label for="scales">Checkbox 3</label>
#                         </div>
#                         <div>
#                             <input type="checkbox" id="scales" name="scales" checked />
#                             <label for="scales">Checkbox 4</label>
#                         </div>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)

