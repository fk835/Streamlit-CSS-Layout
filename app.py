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
/* Remove default padding and margin */
body {
    margin: 0;
    padding: 0;
}
.block-container {
    padding: 0 !important;
    margin-top: 35px;
}
            
/* Style the header */
#header {
    background-color: #fcf3fb; /* Pink background */
    color: black; /* Black text */
    padding: 10px;
    width: 100%;
    border: 2px solid #ccc;
    border-bottom: 0;
}

/* Style the sidebar */
.sidebar {
    background-color: #2196F3; /* Blue background */
    color: white; /* White text */
    padding: 10px;
    height: 100vh; /* Full height */
}

/* Style the footer */
#footer {
    background-color: #ffffbd; /* Yellow background */
    color: black; /* Black text */
    padding: 10px;
    width: 100%;
    border: 2px solid #ccc;
    border-top: 0;
}

/* Targeting main-content */
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-of-type(2) {
    border-right: 2px solid #ccc;
    margin: 0;
    padding: 0;
}

/* Targeting side-bar */
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-of-type(1) {
    border-left: 2px solid #ccc;
    margin: 0;
    padding: 0;
    background-color: #f1fbfe;
}

/*all horizontal blocks*/
div[data-testid="stHorizontalBlock"] {
    gap: 0;
    margin-top: 15px;
}

/*all vertical blocks*/            
div[data-testid="stVerticalBlock"]  {
    gap: 0;
            
}            

/*footer*/
div[data-testid="stHorizontalBlock"]:nth-of-type(2) {
    background-color: #ffffbd; 
    margin: 0;
    border: 2px solid #ccc;           
    border-top: none;
}

/*footber checkbox columns*/            
div[data-testid="stHorizontalBlock"]:nth-of-type(2) > div[data-testid="stColumn"] {
    background-color: #ffffbd; 
    border: none;
    padding: 15px;
              
}
/*footber checkbox */             
div[data-testid="stHorizontalBlock"]:nth-of-type(2) > div[data-testid="stColumn"] .stCheckbox {
    justify-content: center;
}   
       
</style>
""", unsafe_allow_html=True)

# define layout elements
header = st.container(border=False)
sidebar, content = st.columns([0.2, 0.8], border=False)
footer = st.container(border=False)

# Header
with header:
    st.markdown("""
                <div id="header">
                    <h1>We can put a header up here!</h1>
                    <p>Appearance leaves something to be desired, but we can use our own CSS.</p>
                </div>
                """, unsafe_allow_html=True)

# test the built-in sidebar (uses same sidebar as page nav)
with st.sidebar:
    st.write('Built-in sidebar test')

# test using columns to make my own sidebar

# define the sidebar content
with sidebar:
    with st.form('Sidebar form'):
        st.write('Hello, sidebar!')
        st.write('This is a form. A reload is only triggered when the form is submitted.')
        
        # checkboxes
        st.checkbox(label='Checkbox 1')
        st.checkbox(label='Checkbox 2')
        st.checkbox(label='Checkbox 3')
        
        # pills
        st.pills('Pill selection',
                 options=['Option 1', 'Option 2', 'Option 3', 'Option 4'])
        
        # multiselects
        st.multiselect(label='Multiselect',
                       options=['Option 1', 'Option 2', 'Option 3'])
        
        # slider
        st.slider(label='Slider',
                  min_value=0,
                  max_value=10,
                  step=1)
        
        # button to submit sidebar form
        st.form_submit_button('Apply Selection')
    with st.container(border=True):
        st.write('The sidebar can have elements outside of the form.')
        st.write('Interacting with these elements immediately triggers a reload.')
        st.button('Button 1')
        st.button('Button 2')

# page content
with content:     

    # show some sample content        
    st.markdown('## Example content: table')    
    st.dataframe(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
    st.markdown("""
                ## More content
                Here are a couple of other dataframes, which are used to illustrate the behavior of the
                footer and sidebar when more content is shown.
                """)
    st.dataframe(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
    

# footer
with footer:
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    footer_columns = st.columns(4)
    for i, col in enumerate(footer_columns):
        with footer_columns[i]:
            st.checkbox(label=f"Checkbox {i+1}")
    st.markdown("</div>", unsafe_allow_html=True)


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

