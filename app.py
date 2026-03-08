import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Asymmetric Leap", layout="wide") 

# 1. 全球化语言配置字典 (已补全所有零散中文)
languages = {
    "中文": {
        "title": "🚀 18岁非对称跨越：财富模拟系统",
        "sidebar_header": "👤 个人及财务设置",
        "name_label": "您的姓名",
        "age_label": "当前年龄",
        "savings_label": "当前储蓄金额 (RM)",
        "invest_label": "计划投资金额 (RM)",
        "rate_label": "预期年化收益率 (%)",
        "years_label": "预测年限",
        "inflation_label": "设定年通胀率 (%)",
        "predict_title": "年后财富预测",
        "final_val": "最终投资价值",
        "hello": "你好",
        "reach_age": "岁时，你的投资资产将增长到极具规模的水平。",
        "chart_growth": "📈 财富增长曲线",
        "guide_msg": "💡 **想知道如何通过 AI Agent 实现非对称收益？** 在 IG 私信我 'START' 获取完整电子书指南。",
        "data_table": "🗃️ 每年详细数据表",
        "inflation_title": "💲 经通胀调整后的财富",
        "inflation_caption": "注：此处的'实际购买力'考虑了通胀影响。",
        "encourage_btn": "给自己一个未来的鼓励",
        "success_msg": "你现在的每一分努力，都是在为未来的自由投票。",
        "resource_title": "📚 专属资源",
        "ebook_msg": "获取完整版《18岁非对称跨越：AI 时代的资产觉醒》电子书。",
        "code_label": "输入激活码 (Activation Code):",
        "verify_success": "验证成功！",
        "download_btn": "📥 点击前往专属下载通道",
        "wrong_pwd": "密码错误！剩余尝试次数: ",
        "locked": "❌ 尝试次数过多，系统已暂时锁定。",
        "col_year": "年份",
        "col_bank": "银行储蓄 (3%)",
        "col_ai": "AI系统投资",
        "col_bank_real": "银行储蓄(实际购买力)",
        "col_ai_real": "AI系统投资(实际购买力)"
    },
    "English": {
        "title": "🚀 Asymmetric Leap: Wealth Simulator",
        "sidebar_header": "👤 Profile & Finance Settings",
        "name_label": "Your Name",
        "age_label": "Current Age",
        "savings_label": "Current Savings (RM)",
        "invest_label": "Planned Investment (RM)",
        "rate_label": "Expected Annual ROI (%)",
        "years_label": "Forecast Years",
        "inflation_label": "Annual Inflation Rate (%)",
        "predict_title": "Years Wealth Forecast",
        "final_val": "Final Investment Value",
        "hello": "Hello",
        "reach_age": "years old, your assets will grow to a significant scale.",
        "chart_growth": "📈 Wealth Growth Curve",
        "guide_msg": "💡 **Want to achieve asymmetric returns via AI Agents?** DM 'START' on IG for the full E-book.",
        "data_table": "🗃️ Detailed Annual Data",
        "inflation_title": "💲 Inflation-Adjusted Wealth",
        "inflation_caption": "Note: 'Real Purchasing Power' considers inflation impacts.",
        "encourage_btn": "Encourage Your Future Self",
        "success_msg": "Every effort you make now is a vote for your future freedom.",
        "resource_title": "📚 Premium Resources",
        "ebook_msg": "Get the full E-book: 'Asymmetric Leap: Asset Awakening in the AI Era'.",
        "code_label": "Activation Code:",
        "verify_success": "Access Granted!",
        "download_btn": "📥 Go to Download Link",
        "wrong_pwd": "Wrong password! Attempts left: ",
        "locked": "❌ Too many attempts. System locked.",
        "col_year": "Year",
        "col_bank": "Bank Savings (3%)",
        "col_ai": "AI System Investment",
        "col_bank_real": "Bank Savings (Real Power)",
        "col_ai_real": "AI Investment (Real Power)"
    },
    "Melayu": {
        "title": "🚀 Lompatan Asimetrik: Simulator Kekayaan",
        "sidebar_header": "👤 Tetapan Profil & Kewangan",
        "name_label": "Nama Anda",
        "age_label": "Umur Sekarang",
        "savings_label": "Simpanan Semasa (RM)",
        "invest_label": "Pelaburan Dirancang (RM)",
        "rate_label": "Pulangan Tahunan (%)",
        "years_label": "Tahun Ramalan",
        "inflation_label": "Kadar Inflasi Tahunan (%)",
        "predict_title": "Ramalan Kekayaan Tahun",
        "final_val": "Nilai Pelaburan Akhir",
        "hello": "Hello",
        "reach_age": "tahun, aset anda akan berkembang ke skala yang besar.",
        "chart_growth": "📈 Kurva Pertumbuhan Kekayaan",
        "guide_msg": "💡 **Nak tahu cara capai pulangan asimetrik guna AI?** DM 'START' di IG untuk E-book penuh.",
        "data_table": "🗃️ Jadual Data Tahunan",
        "inflation_title": "💲 Kekayaan Larasan Inflasi",
        "inflation_caption": "Nota: 'Kuasa Beli Sebenar' mengambil kira kesan inflasi.",
        "encourage_btn": "Beri Semangat Masa Depan",
        "success_msg": "Setiap usaha anda sekarang adalah undi untuk kebebasan masa depan anda.",
        "resource_title": "📚 Sumber Premium",
        "ebook_msg": "Dapatkan E-book penuh: 'Lompatan Asimetrik'.",
        "code_label": "Kod Pengaktifan:",
        "verify_success": "Akses Dibenarkan!",
        "download_btn": "📥 Pergi ke Pautan Muat Turun",
        "wrong_pwd": "Kata laluan salah! Cubaan berbaki: ",
        "locked": "❌ Terlalu banyak cubaan. Sistem dikunci.",
        "col_year": "Tahun",
        "col_bank": "Simpanan Bank (3%)",
        "col_ai": "Pelaburan Sistem AI",
        "col_bank_real": "Simpanan Bank (Kuasa Sebenar)",
        "col_ai_real": "Pelaburan AI (Kuasa Sebenar)"
    },
    "日本語": {
        "title": "🚀 18歳の非対称的な跳躍：資産シミュレーター",
        "sidebar_header": "👤 プロフィールと財務設定",
        "name_label": "お名前",
        "age_label": "現在の年齢",
        "savings_label": "現在の貯蓄 (RM)",
        "invest_label": "投資予定額 (RM)",
        "rate_label": "期待年利 (%)",
        "years_label": "予測期間 (年)",
        "inflation_label": "想定インフレ率 (%)",
        "predict_title": "年後の資産予測",
        "final_val": "最終投資価値",
        "hello": "こんにちは",
        "reach_age": "歳の時、あなたの資産は大きな規模に成長しているでしょう。",
        "chart_growth": "📈 資産成長曲線",
        "guide_msg": "💡 **AIエージェントで非対称な収益を得る方法は？** IGで 'START' とDMして電子書籍を入手。",
        "data_table": "🗃️ 年次詳細データ表",
        "inflation_title": "💲 インフレ調整後の資産",
        "inflation_caption": "注：「実際の購買力」はインフレの影響を考慮しています。",
        "encourage_btn": "未来の自分への励まし",
        "success_msg": "今の努力の積み重ねが、未来の自由への一票となります。",
        "resource_title": "📚 限定リソース",
        "ebook_msg": "フル版電子書籍『18歳の非対称的な跳躍』を入手する。",
        "code_label": "アクティベーションコード:",
        "verify_success": "認証成功！",
        "download_btn": "📥 専用ダウンロードリンクへ",
        "wrong_pwd": "パスワードが違います！残り回数: ",
        "locked": "❌ 試行回数が多すぎます。ロックされました。",
        "col_year": "年",
        "col_bank": "銀行預金 (3%)",
        "col_ai": "AIシステム投資",
        "col_bank_real": "銀行預金 (実質購買力)",
        "col_ai_real": "AI投資 (実質購買力)"
    },
    "Français": {
        "title": "🚀 Le Saut Asymétrique : Simulateur de Richesse",
        "sidebar_header": "👤 Profil et Paramètres Financiers",
        "name_label": "Votre Nom",
        "age_label": "Âge Actuel",
        "savings_label": "Épargne Actuelle (RM)",
        "invest_label": "Investissement Prévu (RM)",
        "rate_label": "Rendement Annuel Espéré (%)",
        "years_label": "Années de Prévision",
        "inflation_label": "Taux d'Inflation Annuel (%)",
        "predict_title": "Ans : Prévision de Richesse",
        "final_val": "Valeur Finale",
        "hello": "Bonjour",
        "reach_age": "ans, vos actifs auront atteint une échelle significative.",
        "chart_growth": "📈 Courbe de Croissance du Patrimoine",
        "guide_msg": "💡 **Comment générer des revenus asymétriques avec l'IA ?** DM 'START' sur IG pour l'E-book.",
        "data_table": "🗃️ Tableau de Données Annuelles",
        "inflation_title": "💲 Richesse Ajustée à l'Inflation",
        "inflation_caption": "Note : Le 'Pouvoir d'Achat Réel' tient compte de l'inflation.",
        "encourage_btn": "Encourager votre futur moi",
        "success_msg": "Chaque effort aujourd'hui est un vote pour votre liberté future.",
        "resource_title": "📚 Ressources Premium",
        "ebook_msg": "Obtenez l'E-book complet : 'Le Saut Asymétrique'.",
        "code_label": "Code d'Activation :",
        "verify_success": "Accès Autorisé !",
        "download_btn": "📥 Aller au lien de téléchargement",
        "wrong_pwd": "Mot de passe incorrect ! Essais restants : ",
        "locked": "❌ Trop de tentatives. Système verrouillé.",
        "col_year": "Année",
        "col_bank": "Épargne Bancaire (3%)",
        "col_ai": "Investissement Système IA",
        "col_bank_real": "Épargne (Pouvoir Réel)",
        "col_ai_real": "Investissement IA (Pouvoir Réel)"
    }
}

# 侧边栏语言选择
sel_lang = st.sidebar.selectbox("🌐 Language / 言語 / Langue", options=list(languages.keys()))
lang = languages[sel_lang]

st.title(lang["title"])

# 侧边栏：输入逻辑
with st.sidebar:
    st.header(lang["sidebar_header"])
    name = st.text_input(lang["name_label"], value="Future Architect")
    age = st.number_input(lang["age_label"], min_value=1, max_value=100, value=18)
    
    st.markdown("---")
    savings = st.number_input(lang["savings_label"], value=1000.0)
    investment = st.number_input(lang["invest_label"], value=5000.0)
    rate = st.slider(lang["rate_label"], 0.0, 50.0, 10.0) / 100
    years = st.slider(lang["years_label"], 1, 40, 20)
    inflation_rate = st.slider(lang["inflation_label"], 0.0, 10.0, 2.0) / 100

# 核心计算逻辑
def calculate_wealth_curve(principal, rate, years):
    data = [principal * ((1 + rate) ** year) for year in range(years + 1)]
    return data

savings_curve = calculate_wealth_curve(savings, 0.03, years) 
investment_curve = calculate_wealth_curve(investment, rate, years)

# 图表 1 数据
chart_data = pd.DataFrame({
    lang["col_year"]: list(range(years + 1)),
    lang["col_bank"]: savings_curve,
    lang["col_ai"]: investment_curve
})

# 布局展示
col1, col2 = st.columns(2)
with col1:
    st.subheader(f"📊 {years} {lang['predict_title']}")
    st.metric(lang["final_val"], f"RM {investment_curve[-1]:,.2f}", delta=f"{rate*100:.1f}%")
    st.write(f"{lang['hello']} {name}, {age + years} {lang['reach_age']}")

with col2:
    st.subheader(lang["chart_growth"])
    st.line_chart(chart_data.set_index(lang["col_year"]))

st.info(lang["guide_msg"])

# 通胀调整计算
def adjust_for_inflation(values, rate):
    return [val / ((1 + rate) ** year) for year, val in enumerate(values)]

savings_real = adjust_for_inflation(savings_curve, inflation_rate)
investment_real = adjust_for_inflation(investment_curve, inflation_rate)

real_chart_data = pd.DataFrame({
    lang["col_year"]: list(range(years + 1)),
    lang["col_bank_real"]: savings_real,
    lang["col_ai_real"]: investment_real
})

st.subheader(lang["inflation_title"])
st.line_chart(real_chart_data.set_index(lang["col_year"]))
st.caption(lang["inflation_caption"])

# 数据表
st.subheader(lang["data_table"])
st.dataframe(chart_data.style.format(precision=2))

# 激励按钮
if st.button(lang["encourage_btn"]):
    st.success(lang["success_msg"])

st.markdown("---")
st.subheader(lang["resource_title"])

# 底部下载区逻辑
col_a, col_b = st.columns([2, 1])
with col_a:
    st.write(lang["ebook_msg"])
with col_b:
    if 'failed_attempts' not in st.session_state:
        st.session_state.failed_attempts = 0

    if st.session_state.failed_attempts >= 5:
        st.error(lang["locked"])
    else:
        password = st.text_input(lang["code_label"], type="password")
        correct_password = st.secrets.get("MY_PASSWORD", "LEAP2026")
        
        if password: 
            if password == correct_password:
                st.session_state.failed_attempts = 0 
                st.success(lang["verify_success"])
                st.link_button(lang["download_btn"], "https://drive.google.com/drive/folders/1c7dcH_jwwLqxMGezPpiUTMKkklm1XXPE")
            else:
                st.session_state.failed_attempts += 1
                st.warning(f"{lang['wrong_pwd']}{5 - st.session_state.failed_attempts}")

