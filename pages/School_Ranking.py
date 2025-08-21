import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from main import df

st.title("🏫 SCHOOL PERFORMANCE RANKING AND COMPARISION")

st.markdown("""
This page categorizes schools into performance tiers to provide a clear, actionable view of the educational landscape, 
highlighting which schools need immediate intervention and which can serve as models of excellence.
""")

# Create performance categories
def performance_category(row):
    if row['Pass_Rate'] >= 80:
        return 'Excellent (80-100%)'
    elif row['Pass_Rate'] >= 60:
        return 'Good (60-79%)'
    elif row['Pass_Rate'] >= 40:
        return 'Fair (40-59%)'
    else:
        return 'Poor (<40%)'

df['Performance_Category'] = df.apply(performance_category, axis=1)

# Performance category distribution
st.subheader("🏆 School Performance Distribution by District")

performance_counts = df.groupby(['DistrictName', 'Performance_Category']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(10, 6))
performance_counts.plot(kind='bar', stacked=True, ax=ax, 
                        color=['firebrick', 'goldenrod', 'lightgreen', 'darkgreen'])
ax.set_title('School Performance Distribution by District')
ax.set_xlabel('District')
ax.set_ylabel('Number of Schools')
ax.legend(title='Performance Category')
ax.tick_params(axis='x', rotation=0)
st.pyplot(fig)

st.markdown("""
This chart categorizes schools into performance tiers. 
All of Moyo's schools are in the "Good" or "Excellent" categories. 
On the other hand, the majority of Adjumani's schools are in the "Fair" or "Poor" categories, 
with not a single school achieving "Excellent" status. 
This provides a crystal-clear, prioritized list for intervention: 
every school in Adjumani's "Poor" category requires immediate and intensive support.
""")

# Show detailed school rankings
st.subheader("📋 Detailed School Performance Rankings")

# Add filters
col1, col2 = st.columns(2)
with col1:
    district_filter = st.selectbox("Filter by District", 
                                  options=["All"] + list(df['DistrictName'].unique()))
with col2:
    category_filter = st.selectbox("Filter by Performance Category", 
                                  options=["All"] + list(df['Performance_Category'].unique()))

# Apply filters
filtered_df = df.copy()
if district_filter != "All":
    filtered_df = filtered_df[filtered_df['DistrictName'] == district_filter]
if category_filter != "All":
    filtered_df = filtered_df[filtered_df['Performance_Category'] == category_filter]

# Sort by performance
sorted_df = filtered_df.sort_values('Pass_Rate', ascending=False)

# Display the table
st.dataframe(
    sorted_df[['CentreName', 'DistrictName', 'Pass_Rate', 'Performance_Category', 'Total_Students']],
    column_config={
        "CentreName": "School Name",
        "DistrictName": "District",
        "Pass_Rate": st.column_config.ProgressColumn(
            "Pass Rate",
            format="%.1f%%",
            min_value=0,
            max_value=100,
        ),
        "Performance_Category": "Performance Category",
        "Total_Students": "Total Students"
    },
    hide_index=True,
    use_container_width=True
)

# Key insights
st.subheader("💡 Key Insights")
st.info("""
1. **Performance Tier Disparity**: Moyo schools are all in Good or Excellent categories, while Adjumani has mostly Fair and Poor schools
2. **Excellence Gap**: No Adjumani school achieved Excellent status
3. **Intervention Priority**: Schools in the "Poor" category need immediate and intensive support
4. **Best Practices**: Schools in the "Excellent" category should be studied for replicable strategies
""")

# Recommendations
st.subheader("🎯 Recommended Actions")
st.warning("""
1. **Immediate Intervention**: Target schools in the 'Poor' category with comprehensive support programs
2. **Peer Learning**: Establish partnerships between top-performing and struggling schools
3. **Resource Allocation**: Direct additional resources to schools in Adjumani, particularly those in lower performance tiers
4. **Performance Monitoring**: Implement regular tracking of school performance categories to measure improvement
""")