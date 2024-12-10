import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Professional Achievements", layout="centered")

# Header section
st.title("Dallas Hall - Senior Product Manager")
st.subheader("Showcasing Professional Achievements and Leadership")

# Profile Section
col1, col2 = st.columns([1, 3])
with col1:
    profile_image = Image.open("profile_image.png")  # Replace with your profile image file
    st.image(profile_image, caption="Dallas Hall", use_column_width=True)

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

def show_lightbox(title, content):
    """Helper function to simulate a lightbox experience."""
    with st.expander(title):
        st.write(content)

show_lightbox("Growth Initiatives", "Details about scaling teams, revenue growth, and driving product adoption.")
show_lightbox("Cross-team Collaboration", "Details about leading multi-functional teams and projects.")
show_lightbox("Customer Relations", "Highlights of maintaining key stakeholder relationships and client success stories.")

# Case Studies Section
st.subheader("Case Studies")
show_lightbox("Go-To-Market Strategies", "In-depth look at successful product launches and market entry strategies.")
show_lightbox("Tech Innovations", "Innovative projects leveraging AI and LLMs.")

# Resume Section
st.subheader("Resume")
st.write("Download my resume using the button below:")
st.download_button(label="Download PDF", data=None, file_name="Dallas_Hall_Resume.pdf", mime="application/pdf")

# Media and External Links Section
st.subheader("Featured Media")
# Embedding example video and images
st.video("https://www.youtube.com")  # Replace with actual YouTube link

st.image(["achievement1.jpg", "achievement2.jpg"], caption=["Achievement 1", "Achievement 2"], use_column_width=True)

# Additional Functionality Placeholder for Pages
st.subheader("More About Me")
st.write("Explore more pages and content to learn about my journey. (Coming Soon)")

# Footer
st.markdown("---")
st.caption("Site powered by Streamlit")


