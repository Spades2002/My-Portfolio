import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(page_title="Staines's Portfolio", page_icon=":copyright:", layout="wide")

# Function to convert image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Load and convert the image to Base64 (Background image for the whole page)
background_image_url = "https://raw.githubusercontent.com/Spades2002/assets/refs/heads/main/Black%20background.jpg"

# Custom CSS to modify title, header, and footer
css = f"""
<style>
    /* Set full-page background image */
    .stApp {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-position: center;
    }}

    /* Hide Streamlit's top bar (header with logo and menu) */
    header {{
        visibility: hidden;
        display: none;
    }}

    /* Remove the background from the project headers */
    .project-header {{
        text-align: center;
        padding: 50px;
        color: white;
        font-size: 36px;
        font-weight: bold;
        background: none;  /* Remove background */
    }}

    /* Remove the box/borders for the project sections, similar to home section header */
    .css-1d391kg, .css-1aumxhk {{
        border: none !important;
        background-color: transparent !important;
    }}

    /* Reduce sidebar width and change background colour */
    [data-testid="stSidebar"] {{
        width: 200px !important;  /* Change width as needed */
        background-color: #09090b !important;  /* Dark background for sidebar */
        padding: 10px 5px;
    }}

    /* Ensure content area adjusts properly */
    [data-testid="stSidebarContent"] {{
        width: 100%;
    }}

    /* Change sidebar text colour for better contrast */
    .css-1d391kg, .css-1aumxhk {{
        color: #f1f1f1 !important;  /* Light grey text for readability */
    }}

    /* Footer styling */
    .footer {{
        width: 100%;
        margin: 20px auto 0 auto;
        padding: 10px 0;
        background-color: transparent;
        text-align: center;
        font-size: 14px;
        color: #f1f1f1;
    }}

    .footer-content {{
        display: flex;
        justify-content: space-evenly;
        width: 100%;
    }}

    .footer-item {{
        text-align: center;
    }}

    .footer a {{
        text-decoration: none;
        color: #f1f1f1;
    }}
</style>
"""

# Apply the CSS using st.markdown
st.markdown(css, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Other Projects"])

# Home Section
if page == "Home":
    st.title("Staines Rajith")
    st.write("Graduate Robotics, Mechatronics and Control Engineer")
    
    st.header("About Me")
    st.write(
        """
        As a graduate in Robotics, Mechatronics, and Control Engineering from Loughborough University, I am passionate about solving complex technical challenges and driving innovation across diverse industries. My academic background has provided me with a solid foundation in control systems, automation, and artificial intelligence, while also equipping me with analytical skills that enable me to optimise processes and enhance system performance.

        During my internship at First Quantum Minerals, I gained valuable hands-on experience managing automation systems and optimising PLCs in a dynamic industrial environment. This practical exposure deepened my understanding of real-world applications of automation and control, enhancing my problem-solving abilities and adaptability.

        Beyond my academic and professional experiences, I am deeply fascinated by the transformative potential of emerging technologies, particularly in robotics and autonomous systems. From my early interest in self-driving cars and precision rocket landings to my undergraduate projects, such as designing a control system for an autonomous drone used in infrastructure inspection, I have been driven to explore how these technologies can address real-world challenges.

        My ambition extends beyond control systems—I am eager to contribute to sectors where automation, artificial intelligence, and data-driven solutions can improve efficiency, reliability, and sustainability. Whether optimising trading operations or enhancing infrastructure reliability, I am committed to applying my technical expertise to develop innovative solutions that make a tangible impact.

        I thrive in collaborative environments where continuous learning and growth are encouraged. My ability to approach challenges with analytical rigour, combined with a passion for leveraging technology to solve real-world problems, positions me well to contribute meaningfully in dynamic and fast-paced industries. I am excited about the opportunities ahead and look forward to applying my skills to drive innovation and operational excellence.
        """
    )

    # Footer section (only appears on the About Me page)
    st.markdown(
        """
        <div class="footer">
            <p><strong>Get in Touch</strong></p>
            <p>Feel free to reach out for collaboration or to discuss my work!</p>
            <div class="footer-content">
                <div class="footer-item">
                    📧 <a href="mailto:stainesr.27@gmail.com">stainesr.27@gmail.com</a>
                </div>
                <div class="footer-item">
                    📱 +44 7880804552
                </div>
                <div class="footer-item">
                    🔗 <a href="https://www.linkedin.com/in/stainesrajith" target="_blank">LinkedIn</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Projects Section
elif page == "Projects":
    project_page = st.sidebar.selectbox(
        "Select a Project",
        ["Campus Transport System", "Gymnastics Robot", "Roll-angle measurement device"],
    )
    
    # Set the header text dynamically based on the selected project
    st.markdown(f"""
        <div class="project-header">
            {project_page}  <!-- Display the selected project as the header -->
        </div>
    """, unsafe_allow_html=True)

    # Project Content (No sub-header or borders)
    if project_page == "Campus Transport System":
        st.write(
            """
            ### **Eco-Friendly Intra-Campus Monorail System Design:**  
            This project focused on the conceptual design of an eco-friendly intra-campus monorail system for WSP, aimed at enhancing transport efficiency and sustainability. As the project lead, I conducted a comprehensive route analysis to determine the most effective layout, prioritising accessibility, environmental impact, and integration with existing campus infrastructure.

            A key aspect of the design process involved engineering high-capacity carriages tailored for optimal passenger experience. This included advanced HVAC systems to ensure energy-efficient climate control and specialised accommodations for elderly passengers, improving accessibility and inclusivity. Additionally, sustainability was at the forefront of the project, with careful material selection and energy-efficient propulsion methods incorporated into the design.

            While the system remained at the design stage, the project provided valuable insights into sustainable transport solutions and the complexities of large-scale infrastructure planning. Through extensive research, modelling, and iterative refinement, I developed a concept that balanced efficiency, environmental responsibility, and user comfort. This experience reinforced my expertise in transport design, sustainable engineering, and strategic planning for future mobility solutions.
            """
        )
        st.write("**Skills Gained**:")
        st.write(
            """
            - **Programming Languages:** Python
            - **Robotics Platforms:** Arduino
            - **Soft Skills:** Project Management, Communication & Collaboration, Leadership
            - **Software Tools:** AutoCAD, MATLAB/Simulink
            """
        )

    elif project_page == "Gymnastics Robot":
        st.write(
            """
            ### **Stamp-bug and Rover for Gymnastics:** 
            In this project, I led a team of engineers in the development of an innovative gymnastics stamp bug and rover, designed to merge engineering with artistic performance. This unique system aimed to enhance gymnastic routines through synchronised movement and visual effects. To achieve this, I designed and programmed LED arrays that operated in perfect synchrony with music, creating dynamic light displays that complemented the choreography.

            A key technical challenge involved ensuring precise timing and responsiveness of the LEDs to the audio input. This required extensive testing and refinement of control algorithms to achieve a seamless visual effect. Additionally, I leveraged Siemens NX to introduce eco-friendly and sustainable modifications, ensuring that the final design adhered to environmentally conscious engineering principles.

            The project resulted in a novel robotic system capable of augmenting gymnastic performances through intelligent visual synchronisation. While the system successfully enhanced the aesthetic appeal of performances, ongoing development could further optimise power efficiency and expand its range of interactive features. This project not only strengthened my expertise in robotics, embedded systems, and sustainable design but also provided me with valuable leadership experience in multidisciplinary engineering.
            """
        )
        st.write("**Skills Gained**:")
        st.write(
            """
            - **Programming Languages:** Python, C++
            - **Robotics Platforms:** Raspberry Pi, Arduino
            - **Soft Skills:** Problem Solving, Time Management, Leadership
            - **Software Tools:** MATLAB, Siemens NX
            """
        )

    elif project_page == "Roll-angle measurement device":
        st.write(
            """
            ### **Project Overview: Fibre Optic Sagnac Interferometer for High-Precision Rotation Measurement:**  
            In this project, I developed a system based on a fibre optic Sagnac interferometer, designed to measure axial rotation with exceptional precision. Rotation sensors are becoming increasingly integral to many of the technologies we rely on in our daily lives, and this project aimed to enhance the accuracy of such measurements. To achieve this, I conducted a comprehensive review of existing sensors and literature related to interferometers. I also utilised an oscilloscope to capture and analyse data, which was then used to validate the system’s performance and ensure the project’s objectives were met.  
            
            A critical aspect of this project involved the precise setup of the interferometer and the complex calculations required to determine the roll angle. By leveraging the Sagnac effect, the interferometer successfully detected angular velocity, which was subsequently integrated to derive the roll angle.  
            
            The results from multiple tests demonstrated that the interferometer was capable of accurately recording intensity and, through the application of refined equations, calculating angular velocity to a high degree of precision. However, while the system effectively measured angular distance travelled, it was unable to determine the direction of rotation. As a result, the interferometer recorded angular distance rather than true angular displacement (roll).  
            
            Overall, this project not only reinforced my expertise in optical sensing systems and data analysis but also provided me with valuable experience in designing and optimising precision measurement instruments.
            """
        )
        
        # Load the PDF
        pdf_url = "https://github.com/Spades2002/assets/blob/983a1a5f81036a588c13a7ed017bd227f667763e/Interferometer%20literature%20review.pdf"

        # Add download button before "Skills Gained"
        st.download_button(
            label="📄 Download Interferometer Literature Review",
            data=pdf_url,  # This now points to the PDF URL
            file_name="Interferometer_literature_review.pdf",
            mime="application/pdf",
        )
        
        st.write("**Skills Gained**:")
        st.write(
            """
            - **Programming Languages:** Python   
            - **Soft Skills:** Problem Solving, Time Management, Analytical & Critical Thinking
            - **Software Tools:** Siemens NX, MATLAB
            """
        )
        
# Other Projects Section
elif page == "Other Projects":
    other_project_page = st.sidebar.selectbox(
        "Select an Other Project",
        ["Colour and Object Detection", "Engineering Job Finder"],
    )

    st.markdown(f"""
        <div class="project-header">
            {other_project_page}
        </div>
    """, unsafe_allow_html=True)

    if other_project_page == "Colour and Object Detection":
        st.write(
            """
            ### **Real-time Colour and Object Detection Using OpenCV:**  
            This project combines two fundamental computer vision tasks into a single real-time system. Using a webcam feed, it detects objects via YOLOv8 (a state-of-the-art deep learning model) while simultaneously classifying colours at the screen centre with a K-Nearest Neighbours algorithm. The colour classifier was trained on a dataset of 865 named colours, enabling precise identification like "Olive Drab" or "Cadet Blue" from RGB values. 
            
            
            **Key Innovations**:  
            - **Hybrid Approach**: Merges deep learning (YOLO) with traditional ML (KNN) for multimodal perception  
            
            - **Context-Aware Visualisation**: Highlights both detected objects and dominant colour regions with adaptive bounding boxes  
            
            - **Robust Tolerance Handling**: Dynamically adjusts colour matching thresholds (±20 RGB units) to account for lighting variations  
            

            **Why This Project?**  
            As a Robotics Engineer specialising in perception systems, I built this to demonstrate my ability to integrate multiple computer vision techniques into functional prototypes. The project showcases:  
            
            1. **Algorithm Integration**: Combining pre-trained models with custom ML  
            2. **Real-Time Constraints**: Balancing accuracy with performance  
            3. **Problem Decomposition**: Breaking down complex vision tasks into manageable components

            *Part of my ongoing effort to develop portfolio projects that reflect the intersection of robotics, computer vision, and practical software engineering.*  
            """
        )
        st.markdown(
            """
            <a href="https://github.com/Spades2002/Other-Project-1" target="_blank">
                <button style="padding: 8px 16px; background-color: #24292e; color: white; border: none; border-radius: 4px; cursor: pointer;">
                    🚀 View GitHub Repository 
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    elif other_project_page == "Engineering Job Finder":
        col1, col2 = st.columns([3, 2])  # Adjust column width as needed

        with col1:
            # The text part of the project
            st.write("""
            This project focuses on creating an efficient platform for users to find engineering job opportunities using web scraping. The platform was built with Python and leverages various job listing APIs for real-time data retrieval. The aim was to automate the job search process and provide users with an intuitive interface.

            **Key Features**:
            - **Web Scraping**: Real-time job data retrieval using libraries such as BeautifulSoup and Scrapy.
            - **User Interface**: Designed using Streamlit with interactive features for a seamless user experience.
            - **Custom Filters**: Allow users to filter job opportunities based on location, industry, and more.

            ### **Key Innovations**:
            - **Skills Matching**: Uses Natural Language Processing (NLP) to extract skills from uploaded resumes.
            - **Real-Time Job Listings**: Retrieves the latest engineering job listings from Google Jobs and other job search engines.
            - **Interactive Interface**: Built using Streamlit, allowing users to upload resumes and immediately see job opportunities based on their skills.

            **Why This Project?**  
            As a Robotics Engineer, I wanted to create a tool that would simplify the job search process after graduation. This project allows users to easily match their skills with real-world job opportunities, making it an essential tool for those entering the job market.

            **Algorithm and Tools**:
            1. **NLP (Spacy)**: To extract skills from resumes.
            2. **Web Scraping (SerpAPI)**: To retrieve real-time job listings from Google Jobs.
            3. **Streamlit**: For the user interface and seamless interaction.
            """)
            
        with col2:
            # The image part of the project
            st.image("https://raw.githubusercontent.com/Spades2002/My-Portfolio/main/job-finder.png", use_container_width=True)
            
        st.markdown(
            """
            <a href="https://github.com/Spades2002/Other-Project-2" target="_blank">
                <button style="padding: 8px 16px; background-color: #24292e; color: white; border: none; border-radius: 4px; cursor: pointer;">
                    🚀 View GitHub Repository 
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
