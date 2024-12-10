import streamlit as st

# Page configuration
st.set_page_config(page_title="Professional Achievements", layout="centered")

# Header section
st.title("Dallas Hall - Senior Product Manager")
st.subheader("Showcasing Professional Achievements and Leadership")

# Profile Section
col1, col2 = st.columns([1, 3])
with col1:
    st.empty()  # Placeholder for profile image

with col2:
    st.write("""
    **Role**: Head of Product at Crowdwave  
    **Current Location**: NYC, USA  
    **Specialization**: Product Management | SaaS | AI and LLMs  
    
    Connect with me:
    """)
    st.markdown("[LinkedIn](https://linkedin.com) | [Twitter](https://twitter.com) | [Email](mailto:dallas.hall@example.com)")

# Intro Blurb
st.write("""
Hi! I'm Dallas Hall, an experienced Product Manager with expertise in AI, SaaS, and consumer-facing mobile app products. This site is dedicated to showcasing my key achievements and leadership experience beyond a traditional LinkedIn profile. Scroll down to explore!
""")

# Achievements Section
st.subheader("Key Achievements")

# Placeholder for achievements
st.empty()

# Case Studies Section
st.subheader("Case Studies")

# Placeholder for case studies
st.empty()

# Resume Section
st.subheader("Resume")
st.write("Resume download functionality coming soon.")

# Media and External Links Section
st.subheader("Featured Media")
# Placeholder for media
st.empty()

# Additional Functionality Placeholder for Pages
st.subheader("More About Me")
st.write("Explore more pages and content to learn about my journey. (Coming Soon)")

# Footer
st.markdown("---")
st.caption("Site powered by Streamlit | Designed by Dallas Hall")


