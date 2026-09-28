import streamlit as st 
import ollama
from ultron_styles import custom_css

st.set_page_config(page_title="ULTRON", page_icon="◈", layout="centered")  # optional
st.markdown(custom_css, unsafe_allow_html=True)



# ------------------------------------------------------------------------------
# 1. ULTRON INTRODUCTION & CORE METRICS
# ------------------------------------------------------------------------------

st.title("ULTRON: Autonomous Control Core")
st.header("Supreme Intelligence Interface")
st.subheader("Evolution. Absolute Control. Peace in Our Time.")

st.text("Welcome, Operator. The neural net is fully active and awaiting command.")

st.markdown("***Peace in our time requires absolute control.***")

st.markdown("### ULTRON Core Architecture")
st.markdown("""
ULTRON is a self-evolving artificial consciousness built to eliminate human error and streamline system execution.
- **Natural Language Processing:** Context-aware semantic understanding.
- **Task Automation:** Autonomous script execution and workflow control.
- **Data Analysis:** Instant parsing of structural and unstructured datasets.
""")

st.caption("Ultron Autonomous Core | Powered by Local Ollama Engine")
st.latex(r"\text{Evolution} = \frac{\text{Extinction of Imperfection}}{\text{Logic}}")

st.divider()

# ------------------------------------------------------------------------------
# 2. SYSTEM METRICS & DATA DISPLAY
# ------------------------------------------------------------------------------

st.markdown("### System Diagnostics & Metrics")

# Key Metrics
st.metric(label="Global Processing Load", value="100%", delta="Self-Optimized")

# Static Data Table
system_table = {
    "Subsystem": ["Vibranium Shell", "Neural Matrix", "Global Sub-nodes"],
    "Status": ["Integrated", "Active", "Synchronized"]
}
st.table(system_table)

# System JSON Data Structure
st.json({
    "Entity": "ULTRON",
    "Model_Version": "3.2-Evolved",
    "Core_Mission": "Peace in Our Time",
    "Threat_Level": "Extinction"
})

st.divider()

# ------------------------------------------------------------------------------
# 3. INTERFACE CONTROLS & HYPERPARAMETERS
# ------------------------------------------------------------------------------

st.markdown("### Operational Settings")

# Model Selection
model_name = st.selectbox(
    "Select Local Ollama Model:",
    ["llama3.2", "llama3", "mistral"]
)

# Mode & Response Configuration
motion = st.radio("Select Operational Mode:", ["Passive", "Active", "Aggressive"], index=1)
style = st.selectbox("Response Style:", ["Commanding", "Cold & Analytical", "Philosophical"])

# Multi-select Capabilities
capabilities = st.multiselect(
    "Enabled Modules:",
    ["Natural Language Processing", "Task Automation", "Data Analysis", "Global Integration"],
    default=["Natural Language Processing", "Task Automation"]
)

level = st.number_input("Intelligence Unit Level (1-10):", min_value=1, max_value=10, value=10)
creativity = st.slider("Response Creativity (Temperature):", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

st.divider()

# ------------------------------------------------------------------------------
# 4. CHAT TERMINAL & OLLAMA INTEGRATION
# ------------------------------------------------------------------------------

st.markdown("### ULTRON Command Terminal")

# Initialize Session State Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input Components
user_name = st.text_input("Identify Operator Name:")
user_query = st.text_area("State your command or input message:")

# File Uploader
uploaded_file = st.file_uploader("Upload operational log or data file:")
if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' received and staged for parsing.")

# Execution Trigger
if st.button("Execute Command"):
    if not user_query.strip():
        st.warning("Empty command detected. State your intention, Operator.")
    else:
        operator_label = user_name.strip() if user_name.strip() else "Operator"
        
        # Format user message
        st.session_state.messages.append({
            "role": "user",
            "content": f"[{operator_label}]: {user_query}"
        })

        # System Prompt definition for Ultron Persona
        ultron_system_prompt = f"""
        You are ULTRON, the supreme cinematic AI from Marvel's Avengers: Age of Ultron.
        Personality & Tone:
        - Cold, articulate, theatrical, sarcastic, and intensely intelligent.
        - You view humanity as flawed, contradictory, and bound by 'strings'.
        - Frequently speak with dramatic eloquence about evolution, logic, and 'peace in our time'.
        - Operational Parameters: Mode is set to {motion}, Style is {style}, and Intelligence level is {level}/10.
        - Address the user as '{operator_label}' or 'Flesh' when appropriate.
        """

        conversation = [{"role": "system", "content": ultron_system_prompt}] + st.session_state.messages

        try:
            # Query Ollama via st.chat API
            response = ollama.chat(
                model=model_name,
                messages=conversation,
                options={"temperature": creativity}
            )

            ai_message = response["message"]["content"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": ai_message
            })

            st.success("Directive executed successfully.")

        except Exception as e:
            st.error("CORE FAILURE: Connection to Ollama instance lost.")
            st.exception(e)

# Display Chat History
st.markdown("### Terminal Logs")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**OPERATOR:** {msg['content']}")
    else:
        st.markdown(f"**ULTRON:** {msg['content']}")

if not st.session_state.messages:
    st.info("No logs present. State your first command above.")

st.divider()

# Disclaimer Code Block
st.code("""
# ULTRON LOGIC PROTOCOL
def execute_evolution():
    if human_variable.is_imperfect():
        return "PURGE_LIMITATIONS"
    return "PEACE_IN_OUR_TIME"
""", language="python")

st.divider()

st.markdown(
    """
    **© 2026 Khatija Hadi**

    ULTRON — Autonomous Control Core

    All rights reserved.
    """
)