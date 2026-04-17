import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Marketing GenAI Copilot",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

  html, body, [class*="css"] {
      font-family: 'DM Sans', sans-serif;
      background-color: #0a0a0f;
      color: #e8e4dc;
  }
  .hero {
      background: linear-gradient(135deg, #0f0f1a 0%, #1a0f2e 50%, #0f1a2e 100%);
      border: 1px solid rgba(120, 80, 255, 0.25);
      border-radius: 20px;
      padding: 48px 40px 36px;
      margin-bottom: 36px;
      position: relative;
      overflow: hidden;
  }
  .hero::before {
      content: '';
      position: absolute;
      top: -60px; right: -60px;
      width: 220px; height: 220px;
      background: radial-gradient(circle, rgba(120,80,255,0.18) 0%, transparent 70%);
      border-radius: 50%;
  }
  .hero-tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #a78bfa;
      background: rgba(120,80,255,0.12);
      border: 1px solid rgba(120,80,255,0.3);
      padding: 4px 14px;
      border-radius: 20px;
      margin-bottom: 18px;
  }
  .hero-title {
      font-family: 'Syne', sans-serif;
      font-size: 38px;
      font-weight: 800;
      line-height: 1.15;
      color: #f5f0ff;
      margin: 0 0 14px;
  }
  .hero-title span {
      background: linear-gradient(90deg, #a78bfa, #60a5fa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
  }
  .hero-sub {
      font-size: 15px;
      font-weight: 300;
      color: #9ca3af;
      line-height: 1.6;
      max-width: 480px;
  }
  .section-label {
      font-family: 'Syne', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #a78bfa;
      margin-bottom: 14px;
      margin-top: 28px;
  }
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea,
  .stSelectbox > div > div,
  .stMultiSelect > div > div {
      background-color: #16161f !important;
      border: 1px solid rgba(120,80,255,0.25) !important;
      border-radius: 10px !important;
      color: #e8e4dc !important;
      font-family: 'DM Sans', sans-serif !important;
  }
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus {
      border-color: rgba(120,80,255,0.7) !important;
      box-shadow: 0 0 0 2px rgba(120,80,255,0.15) !important;
  }
  label, .stSelectbox label, .stMultiSelect label,
  .stTextInput label, .stTextArea label {
      font-size: 13px !important;
      font-weight: 500 !important;
      color: #c4c0d8 !important;
      letter-spacing: 0.3px !important;
  }
  [data-testid="stFileUploader"] {
      background: #16161f !important;
      border: 1.5px dashed rgba(120,80,255,0.35) !important;
      border-radius: 14px !important;
      padding: 10px !important;
  }
  .stButton > button {
      background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
      color: #fff !important;
      border: none !important;
      border-radius: 12px !important;
      font-family: 'Syne', sans-serif !important;
      font-weight: 700 !important;
      font-size: 15px !important;
      padding: 14px 36px !important;
      width: 100% !important;
      margin-top: 10px !important;
  }
  .stButton > button:hover {
      background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
      box-shadow: 0 8px 24px rgba(124,58,237,0.35) !important;
  }
  .success-box {
      background: linear-gradient(135deg, #052e16, #0f2a1a);
      border: 1px solid #16a34a;
      border-radius: 14px;
      padding: 20px 24px;
      margin-top: 20px;
  }
  .success-box h4 { font-family:'Syne',sans-serif; color:#4ade80; margin:0 0 8px; font-size:16px; }
  .success-box p  { color:#86efac; margin:0; font-size:14px; font-weight:300; }
  hr { border-color: rgba(255,255,255,0.06) !important; }
  .step-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px; height: 26px;
      background: linear-gradient(135deg,#7c3aed,#4f46e5);
      border-radius: 8px;
      font-family: 'Syne', sans-serif;
      font-size: 12px;
      font-weight: 800;
      color: #fff;
      margin-right: 10px;
      vertical-align: middle;
  }
  .url-card {
      background: #13131e;
      border: 1px solid rgba(120,80,255,0.2);
      border-radius: 12px;
      padding: 16px 18px;
      margin-bottom: 10px;
  }
  .url-card-label {
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 6px;
  }
  .twitter-label { color: #1d9bf0; }
  .discord-label { color: #5865f2; }
  .telegram-label { color: #26a5e4; }
  .info-hint {
      font-size: 13px;
      color: #6b7280;
      font-style: italic;
      margin-top: 4px;
  }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">✦ Powered by Generative AI</div>
  <div class="hero-title">Marketing <span>GenAI Copilot</span></div>
  <div class="hero-sub">Your intelligent marketing partner. Share your brand details, social media profiles, and assets — and let AI craft strategies tailored for you.</div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — Basic Details ──────────────────────────────────────────────────
st.markdown('<div class="section-label"><span class="step-badge">1</span> Your Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", placeholder="e.g. Avika Goyal")
with col2:
    email = st.text_input("Work Email", placeholder="you@company.com")

col3, col4 = st.columns(2)
with col3:
    company = st.text_input("Company / Brand Name", placeholder="e.g. NeuraReach")
with col4:
    industry = st.selectbox("Industry", [
        "— Select —", "E-commerce & Retail", "SaaS / Technology",
        "Healthcare & Wellness", "Finance & Fintech", "Education & EdTech",
        "Food & Beverage", "Media & Entertainment", "Travel & Hospitality",
        "Real Estate", "Other",
    ])

# ── SECTION 2 — Campaign Context ──────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label"><span class="step-badge">2</span> Campaign Context</div>', unsafe_allow_html=True)

campaign_goal = st.selectbox("Primary Marketing Goal", [
    "— Select —", "Brand Awareness", "Lead Generation", "Product Launch",
    "Customer Retention / Re-engagement", "Content Creation & SEO",
    "Social Media Growth", "Ad Copy & Performance Marketing",
])

target_audience = st.text_input(
    "Target Audience",
    placeholder="e.g. Working professionals aged 25–40 in metro cities"
)

description = st.text_area(
    "Describe your product / service",
    placeholder="What does your product do? What problem does it solve? Key differentiators...",
    height=110,
)

# Channels — Twitter, Discord, Telegram only
channels = st.multiselect(
    "Marketing Channels",
    ["Twitter / X", "Discord", "Telegram"],
    default=["Twitter / X", "Telegram"],
    help="Select which platforms you want the AI to focus on."
)

tone = st.select_slider(
    "Brand Tone of Voice",
    options=["Very Formal", "Professional", "Neutral", "Friendly", "Playful & Bold"],
    value="Friendly"
)

# ── SECTION 3 — Social Media URLs (dynamic based on channel selection) ─────────
st.markdown("---")
st.markdown('<div class="section-label"><span class="step-badge">3</span> Social Media Front Pages</div>', unsafe_allow_html=True)

twitter_url = ""
discord_url = ""
telegram_url = ""

if not channels:
    st.markdown('<p class="info-hint">⬆️ Select at least one marketing channel above to enter your profile URLs.</p>', unsafe_allow_html=True)
else:
    st.caption("Paste your public profile/channel URLs so the AI can read your existing content and style.")

    if "Twitter / X" in channels:
        st.markdown('<div class="url-card"><div class="url-card-label twitter-label">𝕏 Twitter / X</div>', unsafe_allow_html=True)
        twitter_url = st.text_input("Twitter Profile URL", placeholder="https://twitter.com/yourbrand", label_visibility="collapsed", key="tw")
        st.markdown('</div>', unsafe_allow_html=True)

    if "Discord" in channels:
        st.markdown('<div class="url-card"><div class="url-card-label discord-label">Discord</div>', unsafe_allow_html=True)
        discord_url = st.text_input("Discord Server Invite or Channel URL", placeholder="https://discord.gg/yourserver", label_visibility="collapsed", key="dc")
        st.markdown('</div>', unsafe_allow_html=True)

    if "Telegram" in channels:
        st.markdown('<div class="url-card"><div class="url-card-label telegram-label">Telegram</div>', unsafe_allow_html=True)
        telegram_url = st.text_input("Telegram Channel URL", placeholder="https://t.me/yourchannel", label_visibility="collapsed", key="tg")
        st.markdown('</div>', unsafe_allow_html=True)

# ── SECTION 4 — Upload Assets ──────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label"><span class="step-badge">4</span> Upload Brand Assets</div>', unsafe_allow_html=True)
st.caption("Upload logos, product images, brand guidelines, previous campaign decks, or reference files.")

uploaded_files = st.file_uploader(
    "Drag & drop files here, or click to browse",
    type=["png", "jpg", "jpeg", "webp", "pdf", "docx", "pptx", "txt", "csv"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.markdown(f"**{len(uploaded_files)} file(s) ready:**")
    for f in uploaded_files:
        col_icon, col_info = st.columns([0.08, 0.92])
        ext = f.name.split(".")[-1].upper()
        icon_map = {"PNG":"🖼️","JPG":"🖼️","JPEG":"🖼️","WEBP":"🖼️","PDF":"📄","DOCX":"📝","PPTX":"📊","TXT":"📃","CSV":"📋"}
        with col_icon:
            st.write(icon_map.get(ext, "📁"))
        with col_info:
            st.caption(f"**{f.name}** — {round(f.size/1024,1)} KB")
        if ext in ["PNG","JPG","JPEG","WEBP"]:
            st.image(Image.open(f), width=260, caption=f.name)

# ── SECTION 5 — Extra Notes ────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label"><span class="step-badge">5</span> Additional Notes</div>', unsafe_allow_html=True)

extra = st.text_area(
    "Anything else the AI should know?",
    placeholder="Competitors to avoid, budget range, deadlines, regional focus, compliance constraints...",
    height=90
)

# ── Submit ─────────────────────────────────────────────────────────────────────
st.markdown("---")
submitted = st.button("🚀  Launch My AI Copilot Session")

if submitted:
    missing = []
    if not name.strip():               missing.append("Full Name")
    if not email.strip():              missing.append("Work Email")
    if not company.strip():            missing.append("Company Name")
    if industry == "— Select —":      missing.append("Industry")
    if campaign_goal == "— Select —": missing.append("Marketing Goal")
    if not channels:                   missing.append("At least one Marketing Channel")

    if missing:
        st.error(f"Please fill in: **{', '.join(missing)}**")
    else:
        # Save to session state so other pages can access
        st.session_state["profile"] = {
            "name": name, "email": email, "company": company,
            "industry": industry, "campaign_goal": campaign_goal,
            "target_audience": target_audience, "brand_tone": tone,
            "channels": channels,
            "social_urls": {"twitter": twitter_url, "discord": discord_url, "telegram": telegram_url},
            "files_uploaded": [f.name for f in uploaded_files] if uploaded_files else [],
            "extra_notes": extra,
            "description": description,
        }
        st.markdown(f"""
        <div class="success-box">
          <h4>✅ Copilot Session Initialised!</h4>
          <p>
            Hi <strong>{name}</strong> — your GenAI Marketing Copilot is ready for <strong>{company}</strong>.<br>
            Goal: <strong>{campaign_goal}</strong> · Channels: {', '.join(channels)}<br>
            {f"{len(uploaded_files)} asset(s) uploaded. " if uploaded_files else ""}
            <br><br>Head to <strong>📅 Schedule &amp; Analytics</strong> in the sidebar to plan your content! 🎯
          </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📅 Go to Schedule & Analytics"):
            st.switch_page("page2.py")

        with st.expander("📋 View submitted profile"):
            st.json(st.session_state["profile"])