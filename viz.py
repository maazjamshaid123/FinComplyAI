import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statsmodels.api as sm

def show_viz():
    st.title("_Financial Visualization_ 📊")
    # Create a button to show/hide the code block
    if st.button('Explore'):
        if st.checkbox('Hide', value=False):
            st.empty()
        else:
            # Define the code block
            st.error('Financial Visualization', icon="📊")
            
            # Define the list of items to display
            items = [
                'Files Supported: CSV, XLSX',
                'Scatter Plot',
                'Color-Color Plot',
                'Line Plot',
                'Bar Plot',
                'Horizontal Bar Plot',
                'Histogram',
                'Density Heatmap',
                'PCA Analysis',
                'Contour Plot',
                'Distplot',
                'Residual',
                'Ordinary Least Square (OLS)',
                'Receiver Operating Characteristics (ROC)',
                'Enhanced Prediction Error Analysis',
                '3D Scatter'
            ]
            
            # Calculate the number of rows required to display all the items
            num_rows = len(items) // 3 + 1
            
            # Use a for loop to display each item in a separate column
            for i in range(num_rows):
                col1, col2, col3 = st.columns(3)
                if i*3 < len(items):
                    col1.info(items[i*3])
                if i*3+1 < len(items):
                    col2.info(items[i*3+1])
                if i*3+2 < len(items):
                    col3.info(items[i*3+2])

    st.markdown("---")
 
    # with col2:
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = pd.read_csv("data.csv", index_col=None)
    csv = convert_df(csv)
    st.download_button(
    label="Sample CSV",
    data=csv,
    file_name='data.csv',
    mime='text/csv',)

    def plot_data(data, plot_type, x_col, y_col=None, z_col=None, scatter_matrix_cols=None):
        if plot_type == 'Scatter':
            fig = px.scatter(data, x=x_col, y=y_col, width=1000, height=700)
        elif plot_type == 'Color-Color':
            fig = px.scatter(data, x=x_col, y=y_col, color=z_col,color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == 'Line':
            fig = px.line(data, x=x_col, y=y_col, width=1000, height=700)
        elif plot_type == 'Bar':
            fig = px.bar(data, x=x_col, y=y_col, color=z_col, color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == 'Horizontal Bar':
            fig = px.bar(data, x=x_col, y=y_col, color=z_col, orientation='h',color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == 'Histogram':
            fig = px.histogram(data, x=x_col, width=1000, height=700)
        elif plot_type == 'Density Heatmap':
            fig = px.density_heatmap(data, x=x_col, y=y_col,color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == '3D Scatter':
            fig = px.scatter_3d(data, x=x_col, y=y_col, z=z_col, color=z_col,color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == 'PCA Analysis':
            fig = px.scatter_matrix(data, dimensions=scatter_matrix_cols, color=z_col, color_continuous_scale="Viridis", width=1000, height=700)
        elif plot_type == 'Contour Plot':
            fig = px.density_contour(data, x=x_col, y=y_col, z=z_col, width=1000, height=700)
        elif plot_type == 'Residual':
            fig = px.scatter(data, x=x_col, y=y_col, color=z_col, marginal_y='violin', trendline='ols', trendline_color_override='darkred', width=1000, height=700)
        elif plot_type == 'Receiver Operating Characteristics (ROC)':
            fig = px.area(data, x=x_col, y=y_col,color=z_col, width=1000, height=700)
        elif plot_type == 'Ordinary Least Square (OLS)':
            fig = px.scatter(data, x=x_col, y=y_col,trendline='ols', trendline_color_override='darkred', width=1000, height=700)
        elif plot_type == 'Enhanced Prediction Error Analysis':
            fig = px.scatter(data, x=x_col, y=y_col, color=z_col,marginal_x='histogram', marginal_y='histogram', trendline='ols', trendline_color_override='darkred', width=1000, height=700)
        elif plot_type == 'Distplot':
            fig = px.histogram(data, x=x_col, y=y_col, color=z_col, marginal="rug", width=1000, height=700)
        st.plotly_chart(fig)

    def main():
        file = st.sidebar.file_uploader("Upload a file to get started", type=["csv", "xlsx"])
        if file is not None:
            if file.name.endswith('.csv'):
                data = pd.read_csv(file)
                st.subheader("Data (Editable):")
                st.data_editor(data)
            elif file.name.endswith('.xlsx'):
                data = pd.read_excel(file, engine='openpyxl')
                st.subheader("Data (Editable):")
                st.data_editor(data)


            if file.name.endswith('.csv') or file.name.endswith('.xlsx'):
                plot_type = st.selectbox("Select Plot Type", ["Scatter", "Color-Color", "Line", "Light Curve", "Bar", "Horizontal Bar", "Histogram", "Density Heatmap", "PCA Analysis", "Contour Plot", "Distplot", "Residual", "Ordinary Least Square (OLS)", "Receiver Operating Characteristics (ROC)", "Enhanced Prediction Error Analysis", "3D Scatter"])
                if plot_type == '3D Scatter':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Color-Color':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Light Curve':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Horizontal Bar':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Bar':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)            
                elif plot_type == 'Histogram':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = None
                    z_col = None
                elif plot_type == 'PCA Analysis':
                    features = st.multiselect("Select Features", data.columns)
                    x_col = None
                    y_col = None
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Contour Plot':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)
                elif plot_type == 'Receiver Operating Characteristics (ROC)':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns) 
                elif plot_type == 'Enhanced Prediction Error Analysis':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)      
                elif plot_type == 'Residual':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)   
                elif plot_type == 'Distplot':
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = st.selectbox("Select 3rd Feature", data.columns)   
                else:
                    x_col = st.selectbox("Select 1st Feature", data.columns)
                    y_col = st.selectbox("Select 2nd Feature", data.columns)
                    z_col = None

                if x_col is not None:
                    if data[x_col].dtype in [float, int]:
                        if st.checkbox("Log 1st Feature"):
                            data[x_col] = np.log10(data[x_col]+1)
                if y_col is not None:
                    if data[y_col].dtype in [float, int]:
                        if st.checkbox("Log 2nd Feature"):
                            data[y_col] = np.log10(data[y_col]+1)
                if z_col is not None:
                    if data[z_col].dtype in [float, int]:
                        if st.checkbox("Log 3rd Feature"):
                            data[z_col] = np.log10(data[z_col]+1)

                if plot_type == 'PCA Analysis':
                    if features is not None:
                        scatter_matrix_cols = [col for col in data.columns if col in features]
                        plot_data(data, plot_type, None, None, z_col, scatter_matrix_cols)
                elif plot_type == "Ordinary Least Square (OLS)":
                    try: 
                        data[x_col].dtype or data[y_col].dtype in [float, int]
                        plot_data(data, plot_type, x_col, y_col, z_col)
                    except:
                        st.error("Not a Numeric Type Value", icon="🚨")
                else:
                    plot_data(data, plot_type, x_col, y_col, z_col)
                    
    main()

