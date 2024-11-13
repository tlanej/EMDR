# main.py

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="EMDR App", layout="centered")

# Title of the app
st.title("EMDR (Eye Movement Desensitization and Reprocessing) App")

# Instructions
st.markdown("""
This EMDR app features a red ball that moves horizontally back and forth across the screen. Use the slider below to adjust the speed of the ball.
""")

# Initialize session state for pause/play
if 'is_paused' not in st.session_state:
    st.session_state.is_paused = False

# Speed slider
speed = st.slider("Adjust Ball Speed (balls per minute)", min_value=10, max_value=300, value=60, step=10)

# Convert speed to duration (seconds for one complete back and forth)
# Assuming "balls per minute" as complete cycles per minute
# Duration per cycle = 60 / speed seconds
duration = 60 / speed

# Pause/Play button
if st.button("Pause" if not st.session_state.is_paused else "Play"):
    st.session_state.is_paused = not st.session_state.is_paused

# HTML/CSS/JS for the animation
if not st.session_state.is_paused:
    animation_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .container {{
                position: relative;
                width: 100%;
                height: 200px;
                overflow: hidden;
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                border-radius: 10px;
            }}

            .ball {{
                position: absolute;
                top: 50%;
                left: 0;
                width: 50px;
                height: 50px;
                margin-top: -25px; /* Half of the ball's height to center vertically */
                background-color: red;
                border-radius: 50%;
                animation: moveBall {duration}s ease-in-out infinite;
            }}

            @keyframes moveBall {{
                0% {{ left: 0; }}
                50% {{ left: calc(100% - 50px); }}
                100% {{ left: 0; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="ball"></div>
        </div>
    </body>
    </html>
    """
else:
    # Display the ball without animation
    paused_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .container {
                position: relative;
                width: 100%;
                height: 200px;
                overflow: hidden;
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                border-radius: 10px;
            }

            .ball {
                position: absolute;
                top: 50%;
                left: 0;
                width: 50px;
                height: 50px;
                margin-top: -25px; /* Half of the ball's height to center vertically */
                background-color: red;
                border-radius: 50%;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="ball"></div>
        </div>
    </body>
    </html>
    """

    animation_html = paused_html

# Display the animation
st.components.v1.html(animation_html, height=250, scrolling=False)

# Divider for clarity
st.markdown("---")

# EMDR Self-Administration Instructions
st.header("Instructions to Self-Administer EMDR Procedure")

st.markdown("""
**Important:** While self-administered EMDR can be beneficial, it's recommended to consult with a trained EMDR therapist, especially if you're dealing with significant trauma or emotional distress.

### Step-by-Step Guide:

1. **Find a Comfortable and Quiet Space:**
   - Ensure you're in a safe environment free from distractions.
   - Sit in a comfortable chair with your feet flat on the ground.

2. **Identify the Issue:**
   - Think of a specific memory or issue you'd like to address.
   - Keep your focus on the image, thought, or memory related to this issue.

3. **Rate the Distress:**
   - On a scale from 0 to 10, rate the emotional disturbance associated with the issue (0 = no distress, 10 = maximum distress).

4. **Set Your Intentions:**
   - Decide what you aim to achieve from this session (e.g., reducing anxiety, gaining clarity).

5. **Begin the Ball Animation:**
   - Focus your eyes on the moving red ball.
   - Let your eyes follow the ball as it moves back and forth across the screen.

6. **Follow the Ball with Your Eyes:**
   - Maintain your focus on the ball's movement.
   - Let your thoughts and feelings related to the issue come and go without judgment.

7. **Continue for Several Minutes:**
   - Typically, 5-20 minutes per session is effective.
   - Use the slider to adjust the speed of the ball to your comfort level.

8. **Notice Your Feelings:**
   - Pay attention to any changes in your emotions, thoughts, or physical sensations.
   - Observe any new insights or perspectives that arise.

9. **Take Deep Breaths:**
   - After completing the session, take a few moments to breathe deeply and center yourself.

10. **Reflect and Journal:**
    - Consider writing down any thoughts, feelings, or insights gained during the session.
    - This can help in processing and integrating your experiences.

### Tips for Effective EMDR Sessions:

- **Consistency:** Regular sessions can enhance effectiveness.
- **Patience:** Emotional changes may occur gradually.
- **Safety:** If at any point you feel overwhelmed, stop the session and seek support if needed.
- **Personalization:** Adjust the speed and duration to suit your comfort and needs.

### Additional Resources:

- **EMDR International Association:** [www.emdria.org](https://www.emdria.org/)
- **Books:**
  - *"EMDR: The Breakthrough Therapy for Overcoming Anxiety, Stress, and Trauma"* by Francine Shapiro
- **Consult a Professional:** Consider seeking guidance from a certified EMDR therapist for tailored support.

""")
 
