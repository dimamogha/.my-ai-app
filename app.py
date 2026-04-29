import streamlit as st
import time
from PIL import Image, ImageDraw, ImageFont
import io

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ERM Homes | AI House Master Pro",
    layout="wide",
    page_icon="🏠",
    initial_sidebar_state="collapsed"
)

# --- دالة دمج الصور العمودية (Vertical Comparison) ---
def create_comparison(before_img, after_img):
    img1 = Image.open(before_img).convert("RGB")
    img2 = Image.open(after_img).convert("RGB")
    
    w, h = img1.size
    img2 = img2.resize((w, h))
    
    combined = Image.new("RGB", (w, h * 2))
    combined.paste(img1, (0, 0))
    combined.paste(img2, (0, h))
    
    draw = ImageDraw.Draw(combined)
    
    try:
        font_size = int(w * 0.05)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    def draw_styled_text(draw, position, text, font):
        x, y = position
        draw.text((x, y), text, font=font, fill=(0, 100, 0))

    left_margin = 30 
    top_margin = 30

    draw_styled_text(draw, (left_margin, top_margin), "BEFORE", font)
    draw_styled_text(draw, (left_margin, h + top_margin), "AFTER", font)
    
    return combined

# 2. التنسيق الجمالي (CSS)
st.markdown("""
    <style>
        .main-card { background: white; padding: 40px; border-radius: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); max-width: 1100px; margin: auto; margin-bottom: 25px; }
        .inspiration-box { background-color: #f0fbf9; border: 1.5px solid #d1f2eb; border-radius: 20px; padding: 25px; margin-bottom: 25px; }
        .field-label { color: #64748b; font-size: 14px; font-weight: 600; margin-bottom: 8px; }
        .before-tag { color: #e11d48; font-weight: bold; border: 1px solid #e11d48; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
        .after-tag { color: #2f8f83; font-weight: bold; border: 1px solid #2f8f83; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# --- إضافة اللوغو والعنوان الرئيسي ---
col_logo, col_empty = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=150)
    except:
        st.markdown("<h2 style='color: #D4AF37;'>ERM</h2>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#1e293b; margin-top:-70px; margin-bottom:30px;'>ERM Homes Master Pro 🏠✨</h1>", unsafe_allow_html=True)

tab_lab, tab_social = st.tabs(["🧪 Transformation Lab", "📱 Social Media Manager"])

# ---------------------------------------------------------
# Tab 1: Transformation Lab
# ---------------------------------------------------------
with tab_lab:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### ✨ Topic & Inspiration")
    st.markdown('<div class="inspiration-box">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<p class="field-label">Transformation Category</p>', unsafe_allow_html=True)
        selected_cat = st.pills("Cat", ["Interior", "Exterior", "Garden"], default="Interior", label_visibility="collapsed")
    with c2:
        st.markdown('<p class="field-label">Inspiration Image</p>', unsafe_allow_html=True)
        st.file_uploader("Upload Insp", label_visibility="collapsed", key="insp_up")

    st.markdown('<p class="field-label" style="margin-top:15px;">House Type & Topic</p>', unsafe_allow_html=True)
    
    house_types = [
        "All", "Small House", "Medium House", "Large House", "Mansion", 
        "One-Story House", "Two-Story House", "Three-Story House", 
        "Modern Villa", "Traditional Cottage", "Contemporary Residence", 
        "Townhouse", "Bungalow", "Ranch Style House", "Victorian House", "Colonial House"
    ]
    
    c_sel, c_in = st.columns([1.5, 3.5])
    with c_sel:
        selected_house = st.selectbox("House Type", house_types, label_visibility="collapsed")
    with c_in:
        user_topic = st.text_input("Topic", placeholder="e.g., Luxury Industrial Style", label_visibility="collapsed")

    col_empty, col_style, col_btn = st.columns([1, 2, 1.2])
    with col_style:
        selected_style = st.segmented_control("Style", ["Messy & Random", "Organized & Basic"], default="Messy & Random", label_visibility="collapsed")
    with col_btn:
        generate_clicked = st.button("🪄 Generate Realistic Prompts", use_container_width=True)

    if generate_clicked:
        with st.spinner("🤖 Analyzing layout and generating professional styles..."):
            time.sleep(1)
            # Result 1: Original
            st.markdown('**Result 1: <span class="before-tag">ORIGINAL (BEFORE)</span>**', unsafe_allow_html=True)
            st.code(f"A high-quality, realistic RAW photo of a {selected_house} {selected_cat.lower()}, {selected_style.lower()}, unedited, natural lighting, shot on 35mm lens.", language=None)
            
            # الـ 8 اقتراحات الاحترافية
            modern_variants = [
                f"Professional architectural photography of a {selected_house}, modern fresh paint, elegant neutral colors, {user_topic}, soft natural sunlight.",
                f"Modern {selected_house} renovation, luxury industrial style, exposed brick accents, warm accent lighting, photorealistic.",
                f"Contemporary {selected_house} design, Scandinavian aesthetic, light oak textures, bright and airy, architectural digest style.",
                f"Modern farmhouse style for {selected_house}, white siding with black window frames, high-end furniture, realistic morning light.",
                f"Mid-century modern revival of {selected_house}, sophisticated earth tones, plaster finish, realistic textures, 8k resolution.",
                f"Modern Mediterranean style {selected_house}, smooth white stucco, luxury exterior lighting, realistic landscaping.",
                f"Modern Transitional {selected_house} design, navy blue and gold accents, high-quality marble surfaces, luxury lighting.",
                f"Minimalist Zen-inspired {selected_house}, concrete and wood harmony, slate grey palette, clean lines, real estate photography."
            ]

            for i, p in enumerate(modern_variants):
                st.markdown(f'**Result {i+2}: <span class="after-tag">REALISTIC OPTION {i+1}</span>**', unsafe_allow_html=True)
                st.code(p, language=None)

    st.markdown('</div>')
    st.markdown("### 📸 Visual Assets (Vertical Comparison)")
    v1, v2 = st.columns(2)
    with v1: b_f = st.file_uploader("Upload Before", key="b_l")
    with v2: a_f = st.file_uploader("Upload After", key="a_l")
    
    if b_f and a_f:
        if st.button("🖼️ Create Vertical Comparison", type="primary", use_container_width=True):
            res = create_comparison(b_f, a_f)
            st.image(res, use_container_width=True)
            
            buf = io.BytesIO()
            res.save(buf, format="JPEG", quality=95)
            st.download_button(
                label="📥 Download ERM Comparison JPG",
                data=buf.getvalue(),
                file_name="ERM_Comparison.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

with tab_social:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 🚀 Social Media Magic")
    s_img = st.file_uploader("📸 Upload your final result", key="s_up")
    if s_img:
        st.image(s_img, width=400)
        if st.button("🔥 Generate Viral Strategy", type="primary", use_container_width=True):
            st.markdown('<div style="background:#f9fbfd; padding:20px; border-radius:15px; border:1px solid #e2e8f0;">', unsafe_allow_html=True)
            st.code(f"Title: Stunning Transformation by ERM Homes! 💎", language=None)
            st.code(f"Description: Checkout this {selected_house} in {user_topic} style.", language=None)
            st.code("#ERMHomes #LuxuryRealEstate #BeforeAfter", language=None)
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)