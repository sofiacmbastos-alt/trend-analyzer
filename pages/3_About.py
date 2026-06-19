
st.header("Editor's Picks")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        border:1px solid #ddd;
        padding:15px;
        border-radius:10px;
        text-align:center;
        background:white;
    ">
        <img src="https://mymum-madeit.com/cdn/shop/files/000055370013.jpg?v=1760413890&width=1946" width="100%">
        <h4>Monday Mini Dress</h4>
        <a href="https://mymum-madeit.com/products/monday-mini-dress-assembly-check" target="_blank">Shop Now</a>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="
        border:1px solid #ddd;
        padding:15px;
        border-radius:10px;
        text-align:center;
        background:white;
    ">
        <img src="https://repetto.com/cdn/shop/files/preview_images/e9ba1fe4a930498695483fba2d10a4f6.thumbnail.0000000000_960x.jpg?v=1758702806" width="100%">
        <h4>Cendrillon Ballet Flats</h4>
        <a href="https://repetto.com/en/products/ballerines-cendrillon-v4257twp-899-1?variant=50187301093704">Shop Now</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        border:1px solid #ddd;
        padding:15px;
        border-radius:10px;
        text-align:center;
        background:white;
    ">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsoQxcqoyIOlD9Q_sVhCw75Yvenp6H8qxnDA&s" width="100%">
        <h4>Mapo Dress</h4>
        <a href="https://palomawool.com/products/mapo-dress-short-high-neck-dress-fitted-hem-black" target="_blank">Shop Now</a>
    </div>
    """, unsafe_allow_html=True)
