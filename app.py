import streamlit as st  
import pandas as pd
import numpy as np

st.set_page_config(page_title="Asymmetric Leap", layout="wide") 

languages = {
    "中文": {
        "title": "🚀 18岁非对称跨越：财富模拟系统",
        "sidebar_header": "👤 个人及财务设置",
        "name_label": "您的姓名",
        "investment_val": "最终投资价值",
        "encourage_btn": "给自己一个未来的鼓励",
        "success_msg": "你现在的每一分努力，都是在为未来的自由投票。"
    },
    "English": {
        "title": "🚀 Asymmetric Leap: Wealth Simulator",
        "sidebar_header": "👤 Profile & Finance Settings",
        "name_label": "Your Name",
        "investment_val": "Final Investment Value",
        "encourage_btn": "Encourage Your Future Self",
        "success_msg": "Every effort you make now is a vote for your future freedom."
    },
    "Melayu": {
        "title": "🚀 Lompatan Asimetrik: Simulator Kekayaan",
        "sidebar_header": "👤 Tetapan Profil & Kewangan",
        "name_label": "Nama Anda",
        "investment_val": "Nilai Pelaburan Akhir",
        "encourage_btn": "Beri Semangat Masa Depan",
        "success_msg": "Setiap usaha anda sekarang adalah undi untuk kebebasan masa depan anda."
    }
}

# 侧边栏语言选择
sel_lang = st.sidebar.selectbox("🌐 Language / 语言", options=["中文", "English", "Melayu"])
lang = languages[sel_lang]


# 将原本的硬编码中文替换为字典变量
st.title(lang["title"])

# 侧边栏：输入个人资料与财务数据
with st.sidebar:
    st.sidebar.header(lang["sidebar_header"])
    name = st.text_input(lang["name_label"], value="Future Architect")
    age = st.number_input("当前年龄", min_value=1, max_value=100, value=18)
    
    st.markdown("---")
    savings = st.number_input("当前储蓄金额 (RM)", value=1000.0)
    investment = st.number_input("计划投资金额 (RM)", value=5000.0)
    rate = st.slider("预期年化收益率 (%)", 0.0, 50.0, 10.0) / 100
    years = st.slider("预测年限", 1, 40, 20)

# 核心计算逻辑
def calculate_wealth_curve(principal, rate, years):
    # 生成每年的财富数据
    data = []
    for year in range(years + 1):
        amount = principal * ((1 + rate) ** year)
        data.append(amount)
    return data

# 执行计算
savings_curve = calculate_wealth_curve(savings, 0.03, years) # 固定储蓄利率 3%
investment_curve = calculate_wealth_curve(investment, rate, years)

# 数据整合用于图表
chart_data = pd.DataFrame({
    '年份': list(range(years + 1)),
    '银行储蓄 (3%)': savings_curve,
    'AI系统投资': investment_curve
})

# 页面布局展示
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📊 {years}年后财富预测")
    st.metric("最终投资价值", f"RM {investment_curve[-1]:,.2f}", delta=f"{rate*100:.1f}% 利率")
    st.write(f"你好 {name}，根据你的设置，到 {age + years} 岁时，你的投资资产将增长到极具规模的水平。")

with col2:
    st.subheader("📈 财富增长曲线")
    st.line_chart(chart_data.set_index('年份'))

# 商业引导 (之前提到的电子书引导)
st.info("💡 **想知道如何通过 AI Agent 实现非对称收益？** 在 IG 私信我 'START' 获取完整电子书指南。")

# 显示详细的每一年财富数据
st.subheader("🗃️ 每年详细数据表")
st.dataframe(chart_data.style.format({"银行储蓄 (3%)": "RM {:,.2f}", "AI系统投资": "RM {:,.2f}"}))

# 计算并显示“经通胀调整后”的实际购买力
inflation_rate = st.sidebar.slider("设定年通胀率 (%)", 0.0, 10.0, 2.0) / 100

def adjust_for_inflation(values, inflation_rate):
    # 返回调整后的每年实际购买力
    adjusted = []
    for year, val in enumerate(values):
        adjusted_val = val / ((1 + inflation_rate) ** year)
        adjusted.append(adjusted_val)
    return adjusted

savings_real = adjust_for_inflation(savings_curve, inflation_rate)
investment_real = adjust_for_inflation(investment_curve, inflation_rate)

real_chart_data = pd.DataFrame({
    '年份': list(range(years + 1)),
    '银行储蓄(实际购买力)': savings_real,
    'AI系统投资(实际购买力)': investment_real
})

st.subheader("💲 经通胀调整后的财富")
st.line_chart(real_chart_data.set_index('年份'))
st.caption("注：此处的'实际购买力'考虑了通胀影响。")

# 页面最后增加激励按钮
if st.button(lang["encourage_btn"]):
    st.success(lang["success_msg"])

st.markdown("---")
st.subheader("📚 " + ("专属资源" if sel_lang=="中文" else "Premium Resources"))


# 底部下载区
col_a, col_b = st.columns([2, 1])
with col_a:
    st.write("获取完整版《18岁非对称跨越：AI 时代的资产觉醒》电子书。")
with col_b:
    # 1. 初始化错误计数器
    if 'failed_attempts' not in st.session_state:
        st.session_state.failed_attempts = 0

    # 2. 如果失败超过 5 次，直接锁定
    if st.session_state.failed_attempts >= 5:
        st.error("❌ 尝试次数过多，系统已暂时锁定。 Please contact admin.")
    else:
        password = st.text_input("Activation Code:", type="password")
        
        # 3. 校验逻辑
        correct_password = st.secrets.get("MY_PASSWORD", "LEAP2026")
        
        if password: 
            if password == correct_password:
                st.session_state.failed_attempts = 0 
                st.success("✅ " + ("验证成功！" if sel_lang=="中文" else "Access Granted!"))
                # 直接在这里显示跳转按钮
                st.link_button(
                    "📥 " + ("点击前往专属下载通道" if sel_lang=="中文" else "Go to Download Link"), 
                    "https://drive.google.com/drive/folders/1c7dcH_jwwLqxMGezPpiUTMKkklm1XXPE"
                )
            else:
                st.session_state.failed_attempts += 1
                st.warning(f"密码错误！剩余尝试次数: {5 - st.session_state.failed_attempts}")

if password == st.secrets.get("MY_PASSWORD", "LEAP2026"):
    st.success("验证成功！")
    # 不用下载按钮，改用链接按钮，链接到你设了密码的 Google Drive
    st.link_button("📥 点击前往专属下载通道", "https://drive.google.com/drive/folders/1c7dcH_jwwLqxMGezPpiUTMKkklm1XXPE")

