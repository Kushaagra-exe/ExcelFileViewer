import streamlit as st
import pandas as pd


def main():
    st.title('Excel File viewer')
    st.write("Often we Dont have Excel file viewer apps in our phones or we dont want to install app to save some space or keep our phones clean ")
    st.write("Here is the Solution.")
    st.write("Say Bye Bye to your phone apps just upload the excel file here and you can easily view and search the file in the website itself")
    uploaded_file = st.file_uploader("Choose a (.xlsx) file", type=["xlsx"])

    if uploaded_file is not None:
        dfs = pd.read_excel(uploaded_file, sheet_name=None)

        sheet_names = dfs.keys()
        selected_sheet = st.selectbox("Select a sheet", options=sheet_names)

        st.write(f"Displaying contents of sheet: {selected_sheet}")
        df = dfs[selected_sheet]
        st.dataframe(df)

        search_terms_input = st.text_input("Enter single or multiple words to search")

        if search_terms_input:
            search_terms = [term.strip() for term in search_terms_input.split(',')]

            combined_results = pd.DataFrame()
            for term in search_terms:
                results = df.apply(lambda row: row.astype(str).str.contains(term, case=False, na=False)).any(axis=1)
                filtered_df = df[results]

                if not filtered_df.empty:
                    combined_results = pd.concat([combined_results, filtered_df], ignore_index=True).drop_duplicates()

            if not combined_results.empty:
                st.write(f"Lines containing any of the search terms: {', '.join(search_terms)}")
                st.dataframe(combined_results)
            else:
                st.write(f"No occurrences of the search terms found.")
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #555;
    }
    </style>
    <div class="footer">
        <p>Created by Kushaagra</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



