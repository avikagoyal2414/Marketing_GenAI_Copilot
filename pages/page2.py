import streamlit as st
import datetime
import random

st.set_page_config(
    page_title="Schedule & Analytics — GenAI Copilot",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

  html, body, [class*="css"] {
      font-family: 'DM Sans', sans-serif;
      background-color: #0a0a0f;
      color: #e8e4dc;
  }
  hr { border-color: rgba(255,255,255,0.06) !important; }

  /* Page header */
  .page-header {
      background: linear-gradient(135deg, #0f0f1a, #0f1a2e);
      border: 1px solid rgba(96,165,250,0.2);
      border-radius: 18px;
      padding: 34px 36px 28px;
      margin-bottom: 32px;
  }
  .page-header h1 {
      font-family: 'Syne', sans-serif;
      font-size: 30px;
      font-weight: 800;
      color: #f5f0ff;
      margin: 0 0 8px;
  }
  .page-header h1 span {
      background: linear-gradient(90deg, #60a5fa, #a78bfa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
  }
  .page-header p { color: #9ca3af; font-size:14px; font-weight:300; margin:0; }

  /* Section labels */
  .section-label {
      font-family: 'Syne', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      color: #60a5fa;
      margin-bottom: 14px;
      margin-top: 10px;
  }

  /* AI suggestion cards */
  .ai-card {
      background: #111118;
      border: 1px solid rgba(96,165,250,0.18);
      border-left: 3px solid #60a5fa;
      border-radius: 12px;
      padding: 16px 18px;
      margin-bottom: 12px;
  }
  .ai-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
  }
  .ai-card-platform {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.2px;
      text-transform: uppercase;
  }
  .twitter-col  { color: #1d9bf0; }
  .discord-col  { color: #5865f2; }
  .telegram-col { color: #26a5e4; }

  .ai-card-time {
      font-size: 11px;
      color: #6b7280;
      background: #1a1a28;
      padding: 3px 10px;
      border-radius: 20px;
  }
  .ai-card-content {
      font-size: 14px;
      color: #d1cde8;
      line-height: 1.6;
      margin-bottom: 8px;
  }
  .ai-card-tag {
      display: inline-block;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.8px;
      padding: 2px 10px;
      border-radius: 20px;
      background: rgba(96,165,250,0.1);
      color: #60a5fa;
      border: 1px solid rgba(96,165,250,0.25);
  }

  /* Scheduled post rows */
  .sched-row {
      background: #111118;
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: 10px;
      padding: 12px 16px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 14px;
  }
  .sched-dot {
      width: 10px; height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
  }
  .dot-pending   { background: #f59e0b; }
  .dot-scheduled { background: #60a5fa; }
  .dot-posted    { background: #4ade80; }

  /* Metric cards */
  .metric-card {
      background: #111118;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 14px;
      padding: 22px 20px;
      text-align: center;
  }
  .metric-number {
      font-family: 'Syne', sans-serif;
      font-size: 32px;
      font-weight: 800;
      color: #f5f0ff;
  }
  .metric-label {
      font-size: 12px;
      color: #6b7280;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-top: 4px;
  }
  .metric-delta {
      font-size: 13px;
      font-weight: 600;
      margin-top: 6px;
  }
  .delta-up   { color: #4ade80; }
  .delta-down { color: #f87171; }

  /* Progress bar track */
  .prog-label { font-size: 13px; color: #c4c0d8; margin-bottom: 5px; }
  .prog-track {
      background: #1a1a28;
      border-radius: 20px;
      height: 10px;
      overflow: hidden;
      margin-bottom: 14px;
  }
  .prog-fill {
      height: 100%;
      border-radius: 20px;
  }
  .fill-green    { background: linear-gradient(90deg, #4ade80, #22d3ee); }
  .fill-blue     { background: linear-gradient(90deg, #60a5fa, #a78bfa); }
  .fill-orange   { background: linear-gradient(90deg, #fb923c, #f59e0b); }

  /* AI score badge */
  .score-badge {
      display: inline-block;
      font-family: 'Syne', sans-serif;
      font-size: 13px;
      font-weight: 700;
      padding: 4px 14px;
      border-radius: 20px;
  }
  .score-high { background: rgba(74,222,128,0.12); color:#4ade80; border:1px solid rgba(74,222,128,0.3); }
  .score-mid  { background: rgba(251,146,60,0.12);  color:#fb923c; border:1px solid rgba(251,146,60,0.3); }
  .score-low  { background: rgba(248,113,113,0.12); color:#f87171; border:1px solid rgba(248,113,113,0.3); }

  /* Tabs */
  .stTabs [data-baseweb="tab-list"] {
      background: #111118 !important;
      border-radius: 12px !important;
      padding: 4px !important;
      gap: 2px !important;
  }
  .stTabs [data-baseweb="tab"] {
      background: transparent !important;
      color: #9ca3af !important;
      border-radius: 8px !important;
      font-family: 'Syne', sans-serif !important;
      font-weight: 600 !important;
      font-size: 13px !important;
  }
  .stTabs [aria-selected="true"] {
      background: linear-gradient(135deg,#7c3aed,#4f46e5) !important;
      color: #fff !important;
  }

  /* Buttons */
  .stButton > button {
      background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
      color: #fff !important;
      border: none !important;
      border-radius: 10px !important;
      font-family: 'Syne', sans-serif !important;
      font-weight: 700 !important;
      font-size: 13px !important;
  }
  .stDateInput > div > div > input,
  .stTimeInput > div > div > input,
  .stSelectbox > div > div {
      background-color: #16161f !important;
      border: 1px solid rgba(96,165,250,0.25) !important;
      border-radius: 10px !important;
      color: #e8e4dc !important;
  }
  label {
      font-size: 13px !important;
      font-weight: 500 !important;
      color: #c4c0d8 !important;
  }
  .stTextArea > div > div > textarea {
      background-color: #16161f !important;
      border: 1px solid rgba(96,165,250,0.25) !important;
      border-radius: 10px !important;
      color: #e8e4dc !important;
  }
</style>
""", unsafe_allow_html=True)

# ── Page Header ────────────────────────────────────────────────────────────────
profile = st.session_state.get("profile", {})
company_name = profile.get("company", "Your Brand")

st.markdown(f"""
<div class="page-header">
  <h1>📅 <span>Schedule & Analytics</span></h1>
  <p>{company_name} · AI-powered post scheduling and progress tracking</p>
</div>
""", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🤖  AI Suggestions", "📆  Schedule Posts", "📊  Progress Analytics"])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — AI SUGGESTIONS
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("")
    st.markdown('<div class="section-label">What the AI recommends posting this week</div>', unsafe_allow_html=True)
    st.caption("These suggestions are generated by your backend AI based on your profile, audience, and trending topics. Your dev team will connect the live AI API here.")

    # Placeholder AI suggestions (your backend will replace these)
    suggestions = [
        {
            "platform": "Twitter / X", "cls": "twitter-col",
            "day": "Monday", "time": "9:00 AM",
            "content": "🚀 Did you know 73% of buyers research brands on social before purchasing? Here's how we're making that first impression count 👇 #Marketing #GenAI",
            "tag": "Brand Awareness", "score": 92, "score_cls": "score-high"
        },
        {
            "platform": "Telegram", "cls": "telegram-col",
            "day": "Tuesday", "time": "7:00 PM",
            "content": "Community update 📣 We're building something big. Drop a 🔥 in the comments if you want early access to our AI marketing toolkit launching next month.",
            "tag": "Engagement", "score": 85, "score_cls": "score-high"
        },
        {
            "platform": "Discord", "cls": "discord-col",
            "day": "Wednesday", "time": "6:00 PM",
            "content": "📌 Weekly thread: Share your biggest marketing challenge this week. Our AI will analyse trends and share insights in Friday's digest. Let's go!",
            "tag": "Community", "score": 78, "score_cls": "score-mid"
        },
        {
            "platform": "Twitter / X", "cls": "twitter-col",
            "day": "Thursday", "time": "12:00 PM",
            "content": "The secret to consistent growth? Post when your audience is most active. Our data shows Thursday noon is peak for B2B engagement. Like this post as proof 😄 #SocialMedia",
            "tag": "Educational", "score": 88, "score_cls": "score-high"
        },
        {
            "platform": "Telegram", "cls": "telegram-col",
            "day": "Saturday", "time": "10:00 AM",
            "content": "Weekend read 📖 5 GenAI tools transforming marketing in 2025 — and how you can use them right now. Link in bio!",
            "tag": "Content", "score": 61, "score_cls": "score-low"
        },
    ]

    for s in suggestions:
        score_badge = f'<span class="score-badge {s["score_cls"]}">AI Score: {s["score"]}/100</span>'
        st.markdown(f"""
        <div class="ai-card">
          <div class="ai-card-header">
            <span class="ai-card-platform {s['cls']}">{s['platform']}</span>
            <span class="ai-card-time">{s['day']} · {s['time']}</span>
          </div>
          <div class="ai-card-content">{s['content']}</div>
          <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
            <span class="ai-card-tag">{s['tag']}</span>
            {score_badge}
          </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button(f"✅ Schedule this post", key=f"sched_{s['day']}_{s['platform']}"):
                st.success(f"Added to schedule: {s['day']} at {s['time']}")
        with c2:
            if st.button(f"✏️ Edit before scheduling", key=f"edit_{s['day']}_{s['platform']}"):
                st.info("Edit functionality will be connected to your backend.")
        st.markdown("<div style='margin-bottom:6px'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — SCHEDULE POSTS
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("")

    col_form, col_queue = st.columns([1.1, 0.9], gap="large")

    with col_form:
        st.markdown('<div class="section-label">Create a new scheduled post</div>', unsafe_allow_html=True)

        platform = st.selectbox("Platform", ["Twitter / X", "Discord", "Telegram"])
        post_content = st.text_area(
            "Post Content",
            placeholder="Write your post here. The AI can generate this for you — see the Suggestions tab.",
            height=130
        )

        col_d, col_t = st.columns(2)
        with col_d:
            post_date = st.date_input("Schedule Date", min_value=datetime.date.today())
        with col_t:
            post_time = st.time_input("Schedule Time", value=datetime.time(9, 0))

        post_type = st.selectbox("Content Type", [
            "Brand Awareness", "Engagement / Poll", "Educational",
            "Product Announcement", "Community Update", "Promotional"
        ])

        ai_approved = st.checkbox("✅ Mark as AI-recommended post", value=False,
            help="Toggle this if you're posting content suggested by the AI. This will be tracked in analytics.")

        if st.button("📌 Add to Schedule"):
            if not post_content.strip():
                st.error("Please write your post content first.")
            else:
                if "scheduled_posts" not in st.session_state:
                    st.session_state["scheduled_posts"] = []
                st.session_state["scheduled_posts"].append({
                    "platform": platform,
                    "content": post_content[:80] + ("..." if len(post_content) > 80 else ""),
                    "date": str(post_date),
                    "time": str(post_time.strftime("%I:%M %p")),
                    "type": post_type,
                    "ai_approved": ai_approved,
                    "status": "Scheduled"
                })
                st.success(f"✅ Post scheduled for {post_date} at {post_time.strftime('%I:%M %p')} on {platform}!")

    with col_queue:
        st.markdown('<div class="section-label">Upcoming queue</div>', unsafe_allow_html=True)

        # Seed with some example posts if none exist
        if "scheduled_posts" not in st.session_state:
            st.session_state["scheduled_posts"] = [
                {"platform": "Twitter / X", "content": "🚀 Big announcement coming soon...", "date": str(datetime.date.today()), "time": "9:00 AM", "type": "Brand Awareness", "ai_approved": True, "status": "Scheduled"},
                {"platform": "Telegram", "content": "Community drop this week 🔥", "date": str(datetime.date.today() + datetime.timedelta(days=1)), "time": "7:00 PM", "type": "Engagement / Poll", "ai_approved": True, "status": "Scheduled"},
                {"platform": "Discord", "content": "Weekly thread is live!", "date": str(datetime.date.today() - datetime.timedelta(days=1)), "time": "6:00 PM", "type": "Community Update", "ai_approved": False, "status": "Posted"},
            ]

        posts = st.session_state["scheduled_posts"]
        if not posts:
            st.info("No posts scheduled yet. Add one from the form!")
        else:
            platform_icons = {"Twitter / X": "𝕏", "Discord": "🎮", "Telegram": "✈️"}
            platform_cls   = {"Twitter / X": "twitter-col", "Discord": "discord-col", "Telegram": "telegram-col"}

            for i, p in enumerate(reversed(posts)):
                status_dot = "dot-posted" if p["status"] == "Posted" else "dot-scheduled"
                ai_badge = " · <span style='color:#a78bfa;font-size:11px'>✦ AI Pick</span>" if p["ai_approved"] else ""
                icon = platform_icons.get(p["platform"], "📢")
                pcls = platform_cls.get(p["platform"], "")
                st.markdown(f"""
                <div class="sched-row">
                  <div class="sched-dot {status_dot}"></div>
                  <div style="flex:1; min-width:0;">
                    <div style="font-size:12px;" class="{pcls}"><b>{icon} {p['platform']}</b>{ai_badge}</div>
                    <div style="font-size:13px; color:#d1cde8; margin:3px 0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{p['content']}</div>
                    <div style="font-size:11px; color:#6b7280;">{p['date']} · {p['time']} · {p['type']}</div>
                  </div>
                  <div style="font-size:11px; color:{'#4ade80' if p['status']=='Posted' else '#60a5fa'}; font-weight:600; white-space:nowrap;">{p['status']}</div>
                </div>
                """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — PROGRESS ANALYTICS
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("")
    st.markdown('<div class="section-label">Your progress at a glance</div>', unsafe_allow_html=True)

    # ── KPI Metrics Row ────────────────────────────────────────────────────────
    m1, m2, m3, m4 = st.columns(4)
    metrics = [
        ("847", "Total Reach", "+12.4%", "delta-up"),
        ("63%",  "AI Adoption Rate", "+8%", "delta-up"),
        ("24",   "Posts This Month", "+4", "delta-up"),
        ("3.2×", "Avg Engagement Lift", "+0.4×", "delta-up"),
    ]
    for col, (num, label, delta, delta_cls) in zip([m1,m2,m3,m4], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-number">{num}</div>
              <div class="metric-label">{label}</div>
              <div class="metric-delta {delta_cls}">{delta} this week</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Two column layout ──────────────────────────────────────────────────────
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="section-label">AI vs Manual post performance</div>', unsafe_allow_html=True)

        perf_data = [
            ("AI-Recommended Posts", 78, "fill-green"),
            ("Manual Posts", 42, "fill-orange"),
            ("Scheduled on Time", 91, "fill-blue"),
            ("Audience Target Hit", 65, "fill-green"),
        ]
        for label, pct, cls in perf_data:
            st.markdown(f"""
            <div class="prog-label">{label} &nbsp;<b style="color:#e8e4dc">{pct}%</b></div>
            <div class="prog-track">
              <div class="prog-fill {cls}" style="width:{pct}%"></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:24px">Engagement by platform</div>', unsafe_allow_html=True)

        platform_stats = [
            ("𝕏 Twitter / X", "twitter-col", 48, "fill-blue"),
            ("✈️ Telegram",    "telegram-col", 31, "fill-green"),
            ("🎮 Discord",     "discord-col",  21, "fill-orange"),
        ]
        for name, cls, pct, bar in platform_stats:
            st.markdown(f"""
            <div class="prog-label"><span class="{cls}">{name}</span> &nbsp;<b style="color:#e8e4dc">{pct}%</b></div>
            <div class="prog-track">
              <div class="prog-fill {bar}" style="width:{pct}%"></div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-label">AI content compliance score</div>', unsafe_allow_html=True)
        st.caption("How closely your uploaded content matches what the AI recommends.")

        weeks = ["Week 1", "Week 2", "Week 3", "Week 4 (now)"]
        scores = [55, 68, 74, 83]

        # Simple bar chart using st.bar_chart data
        import pandas as pd
        chart_df = pd.DataFrame({"AI Compliance Score": scores}, index=weeks)
        st.bar_chart(chart_df, color="#7c3aed", height=200)

        st.markdown('<div class="section-label" style="margin-top:20px">Recent posts scored by AI</div>', unsafe_allow_html=True)

        scored_posts = [
            ("Twitter / X", "twitter-col", "🚀 Big announcement coming…", 92, "score-high"),
            ("Telegram",    "telegram-col","Community drop this week 🔥", 85, "score-high"),
            ("Discord",     "discord-col", "Weekly thread is live!",       61, "score-low"),
            ("Twitter / X", "twitter-col", "Custom post (not AI rec.)",    44, "score-low"),
        ]

        for plat, cls, preview, score, sc_cls in scored_posts:
            st.markdown(f"""
            <div class="ai-card" style="margin-bottom:8px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="ai-card-platform {cls}" style="font-size:11px;">{plat}</span>
                <span class="score-badge {sc_cls}">{score}/100</span>
              </div>
              <div style="font-size:13px; color:#9ca3af; margin-top:6px;">{preview}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:20px">Content improvement tips</div>', unsafe_allow_html=True)

        tips = [
            ("📌", "Post on Twitter between 8–10 AM for 2× reach"),
            ("🎯", "Use 2–3 relevant hashtags — not 10+"),
            ("🔥", "Telegram engagement peaks on Tue & Thu evenings"),
            ("💡", "Discord threads with questions get 40% more replies"),
        ]
        for icon, tip in tips:
            st.markdown(f"""
            <div style="background:#111118; border:1px solid rgba(255,255,255,0.07); border-radius:10px; padding:10px 14px; margin-bottom:8px; font-size:13px; color:#c4c0d8;">
              {icon} &nbsp; {tip}
            </div>
            """, unsafe_allow_html=True)