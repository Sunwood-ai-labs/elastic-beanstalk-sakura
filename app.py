import streamlit as st
import pandas as pd
import numpy as np

# アプリのタイトル
st.title('Streamlit on Elastic Beanstalk')

# サンプルデータの作成
data = pd.DataFrame({
    'Column 1': np.random.randn(100),
    'Column 2': np.random.randn(100)
})

# データフレームの表示
st.write('## サンプルデータ')
st.dataframe(data)

# チャートの表示
st.write('## 散布図')
st.scatter_chart(data)
