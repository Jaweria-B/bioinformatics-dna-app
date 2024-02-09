# Import libraries

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import random

# Session states
st.session_state["input"] = False
st.session_state["show_inp"] = True

# Page Title
st.write("""
# :red[DNA] Nucleotide Count Web App
         
This app counts the nucleotide composition of query DNA!
        
***        
""")

image = Image.open('./assets/dna.png')

st.image(image, use_column_width=True)

st.write(
    """Analyze DNA sequences effortlessly with our DNA Nucleotide Count Web App. Get detailed breakdowns and visualizations of nucleotide composition in just a few clicks!"""
)

st.divider()

def generate_input():
    st.session_state["show_inp"] = True

    inputs = [
        'TCAGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC'
        ,
        'ATGCGTACGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG'
        ,
        'GATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nGATCGATCGATCGATCGAT'
        ,
        'CCAGTGTCGACAGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG'
        ,
        'TACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACG\nTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACG\nTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACG\nTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACG\nTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACG\nTACGTACGTACGTACGTACGT'
        ,
        'GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT'
    ]

    input_ind = random.randint(0, 5)
    input = inputs[input_ind]

    # st.write("Random Input: \n", input)

    return input
    

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])

    return d

def main():
    
    st.header('Input')

    sequence_input = ""

    inp_sequence = st.text_area("Enter a DNA Sequence: ", sequence_input, height=200)

    if st.button(label='Want an Input Example!'):
        rand_inp = generate_input()

        if st.session_state["show_inp"]:
            st.write(
                f"""
                #### Don't Know How what kind of input to enter?  
                \n##### **Here is an example test-input:**  \n{rand_inp}
                """
            )
 
    if inp_sequence:
        st.session_state["input"] =  True
        st.session_state["show_inp"] = False

    if st.session_state["input"] and not st.session_state["show_inp"]:
        sequence = inp_sequence.splitlines()
        sequence = ''.join(sequence)

        st.write("""
        ***
        """)

        ## Prints the input DNA sequence
        st.write(
            f"""
            ## DNA Query Entered:  \n
            >DNA Query
            """
        )
        sequence

        st.divider()

        ## DNA nucleotide count
        st.header('OUTPUT')

        st.write(
            f"""
            > ### DNA Nucleotide Count
            """
        )

        # Prints Dictionary
        st.subheader('1. Dictionary')

        X = DNA_nucleotide_count(sequence)

        X_label = list(X)
        X_values = list(X.values())
        X

        ### 2. Print text
        st.subheader('2. Textual Information')
        st.write('- There are  ' + '**' + str(X['A']) + '**' + ' ***adenine*** (A)')
        st.write('- There are  ' + '**' + str(X['T']) + '**' + ' ***thymine*** (T)')
        st.write('- There are  ' + '**' + str(X['G']) + '**' + ' ***guanine*** (G)')
        st.write('- There are  ' + '**' + str(X['C']) + '**' + ' ***cytosine*** (C)')

        ## 3. Display DataFrame
        st.subheader('3. DataFrame')
        df = pd.DataFrame.from_dict(X, orient='index')
        df = df.rename( {0: 'count'}, axis='columns')
        df.reset_index(inplace=True)
        df = df.rename(columns = {'index':'nucleotide'})
        st.write(df)

        ### 4. Display Bar Chart using Altair
        st.subheader('4. Bar chart')
        p = alt.Chart(df).mark_bar().encode(
            x='nucleotide',
            y='count'
        )
        p = p.properties(
            width=alt.Step(80)  # controls width of bar.
        )
        st.write(p)

        st.write("""
        Made By **_Jaweria Batool_**
        """)

if __name__ == "__main__":
    main()