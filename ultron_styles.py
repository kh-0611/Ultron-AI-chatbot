"""
ULTRON: Autonomous Control Core — visual theme
Dark academia x futuristic AI terminal. CSS only, no JavaScript.

Usage:
    from ultron_styles import custom_css
    st.markdown(custom_css, unsafe_allow_html=True)
"""

custom_css = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ==========================================================================
   1. DESIGN TOKENS
   ========================================================================== */
:root {
    /* Palette */
    --midnight:      #0a0f24;
    --navy:          #121937;
    --charcoal:      #0e1017;
    --lavender:      #b7a9d9;
    --lavender-dim:  #8a7fb0;
    --silver:        #b9c0cf;
    --ice:           #9fd3e6;
    --text:          #e6e8ef;
    --text-dim:      #9aa1b3;

    /* Surfaces & borders */
    --surface:       rgba(22, 27, 50, 0.55);
    --surface-hi:    rgba(30, 36, 66, 0.70);
    --border:        rgba(183, 169, 217, 0.18);
    --border-hi:     rgba(183, 169, 217, 0.45);

    /* Shadows & glows */
    --shadow:        0 10px 40px rgba(0, 0, 0, 0.45);
    --shadow-soft:   0 4px 18px rgba(0, 0, 0, 0.35);
    --glow-lav:      0 0 28px rgba(183, 169, 217, 0.28);
    --glow-ice:      0 0 24px rgba(159, 211, 230, 0.22);

    /* Shape & spacing */
    --radius:        18px;
    --radius-sm:     12px;
    --pad:           1.25rem;
    --gap:           1.1rem;

    /* Type */
    --font-serif:    'Cormorant Garamond', 'Georgia', serif;
    --font-sans:     'Inter', 'Segoe UI', system-ui, sans-serif;
    --font-mono:     'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

    --ease:          cubic-bezier(0.22, 0.61, 0.36, 1);
}

/* ==========================================================================
   2. APP SHELL & ATMOSPHERIC BACKGROUND
   ========================================================================== */
.stApp {
    font-family: var(--font-sans);
    color: var(--text);
    background:
        radial-gradient(1100px 600px at 12% -8%, rgba(183, 169, 217, 0.16), transparent 60%),
        radial-gradient(900px 700px at 105% 8%,  rgba(159, 211, 230, 0.09), transparent 55%),
        radial-gradient(900px 800px at 50% 125%, rgba(58, 70, 150, 0.28),   transparent 60%),
        linear-gradient(180deg, var(--midnight) 0%, var(--charcoal) 100%);
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] { background: transparent; }

[data-testid="stHeader"] { background: transparent; }

/* Hide the element container that only holds this <style> block */
[data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] style) { display: none; }

[data-testid="stMainBlockContainer"],
.block-container {
    max-width: 920px;
    padding: 3.5rem 1.5rem 5rem;
    animation: ultron-fade-up 0.9s var(--ease) both;
}

[data-testid="stVerticalBlock"] { gap: var(--gap); }

::selection { background: rgba(183, 169, 217, 0.35); color: #fff; }

/* Scrollbars */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(183, 169, 217, 0.25);
    border-radius: 10px;
    border: 2px solid transparent;
    background-clip: content-box;
}
::-webkit-scrollbar-thumb:hover { background: rgba(183, 169, 217, 0.45); background-clip: content-box; }

/* ==========================================================================
   3. TYPOGRAPHY & HEADINGS
   ========================================================================== */
/* st.title -> hero */
[data-testid="stHeading"] h1 {
    font-family: var(--font-serif);
    font-weight: 700;
    font-size: clamp(2.1rem, 6vw, 4.2rem);
    line-height: 1.05;
    letter-spacing: 0.06em;
    text-align: center;
    padding: 1.5rem 0 0.25rem;
    background: linear-gradient(180deg, #ffffff 0%, var(--silver) 45%, var(--lavender) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    filter: drop-shadow(0 0 22px rgba(183, 169, 217, 0.35));
    animation: ultron-glow 6s ease-in-out infinite;
}

/* st.header -> small eyebrow label under the hero */
[data-testid="stHeading"] h2 {
    font-family: var(--font-sans);
    font-weight: 500;
    font-size: 0.85rem;
    letter-spacing: 0.42em;
    text-transform: uppercase;
    text-align: center;
    color: var(--ice);
    padding: 0.25rem 0;
}

/* st.subheader -> cinematic subtitle */
[data-testid="stHeading"] h3 {
    font-family: var(--font-serif);
    font-style: italic;
    font-weight: 500;
    font-size: clamp(1.1rem, 2.6vw, 1.5rem);
    text-align: center;
    color: var(--silver);
    padding: 0 0 0.75rem;
}

/* "###" section headings written with st.markdown */
[data-testid="stMarkdownContainer"] h3 {
    font-family: var(--font-serif);
    font-weight: 600;
    font-size: 1.7rem;
    letter-spacing: 0.03em;
    color: var(--text);
    padding: 1rem 0 0.25rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
}
[data-testid="stMarkdownContainer"] h3::before {
    content: "\25C8";
    color: var(--lavender);
    font-size: 0.9rem;
    text-shadow: var(--glow-lav);
}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    font-size: 0.98rem;
    line-height: 1.75;
    color: var(--text);
}
[data-testid="stMarkdownContainer"] li::marker { color: var(--lavender); }
[data-testid="stMarkdownContainer"] strong { color: #fff; font-weight: 600; }

/* Emphasised tagline (***text***) */
[data-testid="stMarkdownContainer"] em {
    font-family: var(--font-serif);
    font-size: 1.15em;
    color: var(--lavender);
}
[data-testid="stMarkdownContainer"] p:has(> em > strong) {
    text-align: center;
    font-size: 1.25rem;
    padding: 0.4rem 0;
}

/* Captions */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-dim);
    text-align: center;
}

/* Dividers */
hr {
    border: none;
    height: 1px;
    margin: 1.75rem 0;
    background: linear-gradient(90deg, transparent, var(--border-hi), transparent);
}

/* ==========================================================================
   4. CARDS  (glass surfaces)
   ========================================================================== */
[data-testid="stText"],
[data-testid="stMetric"],
[data-testid="stTable"],
[data-testid="stJson"],
[data-testid="stLatex"],
[data-testid="stFileUploader"],
[data-testid="stMarkdownContainer"]:has(> ul),
[class*="st-key-card"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: var(--pad);
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    transition: transform 0.35s var(--ease), border-color 0.35s var(--ease), box-shadow 0.35s var(--ease);
}

[data-testid="stText"]:hover,
[data-testid="stMetric"]:hover,
[data-testid="stTable"]:hover,
[data-testid="stJson"]:hover,
[data-testid="stLatex"]:hover,
[data-testid="stFileUploader"]:hover,
[data-testid="stMarkdownContainer"]:has(> ul):hover {
    transform: translateY(-2px);
    border-color: var(--border-hi);
    box-shadow: var(--shadow), var(--glow-lav);
}

/* Keyed cards (st.container(key="card_...")): no hover lift, calmer nesting */
[class*="st-key-card"] { gap: 1rem; }
[class*="st-key-card"] [data-testid="stFileUploader"] {
    background: transparent;
    border: none;
    box-shadow: none;
    padding: 0;
    backdrop-filter: none;
}
[class*="st-key-card"] [data-testid="stFileUploader"]:hover { transform: none; box-shadow: none; }

/* Small section tag used above cards: st.markdown('<div class="tag">...</div>') */
.tag {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    color: var(--lavender-dim);
    margin-bottom: 0.2rem;
}

/* Welcome text (st.text) */
[data-testid="stText"] {
    font-family: var(--font-serif);
    font-size: 1.2rem;
    font-style: italic;
    color: var(--silver);
    text-align: center;
    white-space: normal;
}

/* LaTeX equation card */
[data-testid="stLatex"] { text-align: center; color: var(--ice); overflow-x: auto; }

/* ==========================================================================
   5. SYSTEM DIAGNOSTICS  (metric / table / json / code)
   ========================================================================== */
[data-testid="stMetric"] {
    background:
        linear-gradient(135deg, rgba(159, 211, 230, 0.07), transparent 60%),
        var(--surface);
    border-left: 3px solid var(--ice);
}
[data-testid="stMetricLabel"] p {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--text-dim);
}
[data-testid="stMetricValue"] {
    font-family: var(--font-mono);
    font-weight: 500;
    font-size: 2.6rem;
    color: var(--ice);
    text-shadow: var(--glow-ice);
}
[data-testid="stMetricDelta"] {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    color: var(--lavender) !important;
}
[data-testid="stMetricDelta"] svg { fill: var(--lavender) !important; }

/* Table */
[data-testid="stTable"] table {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-mono);
    font-size: 0.85rem;
}
[data-testid="stTable"] thead th {
    color: var(--lavender);
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-size: 0.72rem;
    text-align: left;
    padding: 0.7rem 0.9rem;
    border-bottom: 1px solid var(--border-hi);
    background: transparent;
}
[data-testid="stTable"] tbody td,
[data-testid="stTable"] tbody th {
    color: var(--text);
    padding: 0.7rem 0.9rem;
    border-bottom: 1px solid var(--border);
    background: transparent;
}
[data-testid="stTable"] tbody tr:last-child td,
[data-testid="stTable"] tbody tr:last-child th { border-bottom: none; }
[data-testid="stTable"] tbody tr:hover td { background: rgba(183, 169, 217, 0.07); }

/* JSON */
[data-testid="stJson"] { font-family: var(--font-mono); font-size: 0.85rem; }
[data-testid="stJson"] .react-json-view,
[data-testid="stJson"] > div {
    background: transparent !important;
    background-color: transparent !important;
    font-family: var(--font-mono) !important;
}

/* Code block styled as a developer terminal */
[data-testid="stCode"],
[data-testid="stCodeBlock"] {
    position: relative;
    background: rgba(8, 10, 20, 0.85);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    overflow: hidden;
}
[data-testid="stCode"]::before,
[data-testid="stCodeBlock"]::before {
    content: "\25CF  \25CF  \25CF      ultron_protocol.py";
    display: block;
    padding: 0.65rem 1rem;
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: var(--text-dim);
    background: linear-gradient(180deg, rgba(183, 169, 217, 0.10), rgba(183, 169, 217, 0.03));
    border-bottom: 1px solid var(--border);
}
[data-testid="stCode"] pre,
[data-testid="stCodeBlock"] pre {
    background: transparent !important;
    padding: 1rem 1.2rem !important;
    margin: 0;
}
[data-testid="stCode"] code,
[data-testid="stCodeBlock"] code {
    font-family: var(--font-mono) !important;
    font-size: 0.85rem;
    line-height: 1.7;
}

/* ==========================================================================
   6. WIDGET LABELS
   ========================================================================== */
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    font-family: var(--font-sans);
    font-size: 0.74rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--lavender-dim);
}

/* ==========================================================================
   7. OPERATIONAL SETTINGS  (select, radio, multiselect, number, slider)
   ========================================================================== */
/* Text / number / textarea shells */
div[data-baseweb="input"],
div[data-baseweb="base-input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] > div {
    background: rgba(10, 13, 28, 0.65) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    transition: border-color 0.3s var(--ease), box-shadow 0.3s var(--ease);
}
div[data-baseweb="input"]:hover,
div[data-baseweb="textarea"]:hover,
div[data-baseweb="select"] > div:hover { border-color: var(--border-hi) !important; }

div[data-baseweb="input"]:focus-within,
div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"] > div:focus-within {
    border-color: var(--lavender) !important;
    box-shadow: 0 0 0 3px rgba(183, 169, 217, 0.15), var(--glow-lav);
}

input, textarea {
    font-family: var(--font-sans) !important;
    color: var(--text) !important;
    caret-color: var(--ice);
}
textarea { font-family: var(--font-mono) !important; font-size: 0.9rem; }
input::placeholder, textarea::placeholder { color: var(--text-dim) !important; opacity: 0.7; }

/* Select text & icons */
div[data-baseweb="select"] span,
div[data-baseweb="select"] div { color: var(--text); }
div[data-baseweb="select"] svg { fill: var(--lavender); }

/* Dropdown menu */
div[data-baseweb="popover"] > div,
ul[data-testid="stSelectboxVirtualDropdown"],
div[data-baseweb="menu"] {
    background: var(--navy) !important;
    border: 1px solid var(--border-hi);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow);
}
li[role="option"] { color: var(--text); transition: background 0.2s var(--ease); }
li[role="option"]:hover,
li[role="option"][aria-selected="true"] { background: rgba(183, 169, 217, 0.16) !important; }

/* Multiselect tags */
span[data-baseweb="tag"] {
    background: rgba(183, 169, 217, 0.16) !important;
    border: 1px solid rgba(183, 169, 217, 0.4);
    border-radius: 999px !important;
    color: var(--text) !important;
    font-size: 0.8rem;
}
span[data-baseweb="tag"] span { color: var(--text) !important; }
span[data-baseweb="tag"] svg { fill: var(--lavender); }

/* Number input +/- steppers */
[data-testid="stNumberInputStepUp"],
[data-testid="stNumberInputStepDown"] {
    background: transparent !important;
    color: var(--lavender) !important;
    border-color: var(--border) !important;
}
[data-testid="stNumberInputStepUp"]:hover,
[data-testid="stNumberInputStepDown"]:hover { background: rgba(183, 169, 217, 0.15) !important; }

/* Radio -> pill selector */
div[role="radiogroup"] { display: flex; flex-wrap: wrap; gap: 0.6rem; }
label[data-baseweb="radio"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.4rem 1.1rem;
    margin: 0 !important;
    cursor: pointer;
    transition: all 0.3s var(--ease);
}
label[data-baseweb="radio"]:hover { border-color: var(--border-hi); transform: translateY(-1px); }
label[data-baseweb="radio"]:has(input:checked) {
    background: rgba(183, 169, 217, 0.18);
    border-color: var(--lavender);
    box-shadow: var(--glow-lav);
}
label[data-baseweb="radio"] p { font-size: 0.9rem; color: var(--text); }

/* Slider */
[data-testid="stSlider"] [role="slider"] {
    background: var(--lavender) !important;
    border: 2px solid #fff;
    box-shadow: var(--glow-lav);
}
[data-testid="stSliderThumbValue"],
[data-testid="stSliderThumbValue"] p {
    font-family: var(--font-mono);
    color: var(--ice) !important;
}
[data-testid="stTickBarMin"],
[data-testid="stTickBarMax"] { font-family: var(--font-mono); color: var(--text-dim); }

/* ==========================================================================
   8. FILE UPLOADER
   ========================================================================== */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(10, 13, 28, 0.5);
    border: 1px dashed var(--border-hi);
    border-radius: var(--radius-sm);
    transition: all 0.3s var(--ease);
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--ice);
    background: rgba(159, 211, 230, 0.05);
}
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploaderDropzoneInstructions"] span { color: var(--text-dim); font-size: 0.8rem; }
[data-testid="stFileUploaderDropzone"] button {
    background: transparent;
    border: 1px solid var(--border-hi);
    border-radius: 999px;
    color: var(--lavender);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    transition: all 0.3s var(--ease);
}
[data-testid="stFileUploaderDropzone"] button:hover {
    background: rgba(183, 169, 217, 0.15);
    color: #fff;
}

/* ==========================================================================
   9. EXECUTE COMMAND BUTTON
   ========================================================================== */
.stButton > button {
    font-family: var(--font-sans);
    font-weight: 500;
    font-size: 0.85rem;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: #fff;
    padding: 0.85rem 2.4rem;
    border-radius: 999px;
    border: 1px solid var(--border-hi);
    background: linear-gradient(135deg, rgba(183, 169, 217, 0.28), rgba(159, 211, 230, 0.14));
    box-shadow: 0 0 0 rgba(183, 169, 217, 0), var(--shadow-soft);
    transition: transform 0.35s var(--ease), box-shadow 0.35s var(--ease),
                border-color 0.35s var(--ease), background 0.35s var(--ease);
}
.stButton > button:hover {
    transform: translateY(-3px);
    border-color: var(--ice);
    background: linear-gradient(135deg, rgba(183, 169, 217, 0.42), rgba(159, 211, 230, 0.24));
    box-shadow: 0 10px 34px rgba(183, 169, 217, 0.30), 0 0 0 1px rgba(159, 211, 230, 0.5);
    color: #fff;
}
.stButton > button:active { transform: translateY(-1px) scale(0.99); }
.stButton > button:focus-visible { outline: 2px solid var(--ice); outline-offset: 3px; }
.stButton > button p { color: inherit; font-size: inherit; letter-spacing: inherit; }

/* ==========================================================================
   10. ALERTS  (success / warning / error / info)
   ========================================================================== */
[data-testid="stAlert"],
[data-testid="stAlertContainer"] {
    background: var(--surface-hi) !important;
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    color: var(--text);
    font-size: 0.92rem;
}
[data-testid="stAlert"] p,
[data-testid="stAlertContainer"] p { color: var(--text); }

/* ==========================================================================
   11. TERMINAL LOGS / CHAT CARDS
   ========================================================================== */
/* (a) Custom HTML cards -- see optional snippet in the instructions */
.msg {
    position: relative;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.3rem 1.1rem;
    margin: 0.35rem 0 0.8rem;
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(12px);
    animation: ultron-fade-up 0.5s var(--ease) both;
}
.msg-label {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
}
.msg-body { font-size: 0.97rem; line-height: 1.75; color: var(--text); word-wrap: break-word; }

.msg-operator { border-left: 3px solid var(--lavender); margin-right: 8%; }
.msg-operator .msg-label { color: var(--lavender); }

.msg-ultron {
    border-left: 3px solid var(--ice);
    margin-left: 8%;
    background:
        linear-gradient(135deg, rgba(159, 211, 230, 0.07), transparent 65%),
        var(--surface);
}
.msg-ultron .msg-label { color: var(--ice); }
.msg-ultron .msg-body { font-family: var(--font-serif); font-size: 1.12rem; }

/* (b) Native st.chat_message support, if you ever switch to it */
[data-testid="stChatMessage"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    box-shadow: var(--shadow-soft);
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])      { border-left: 3px solid var(--lavender); }
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) { border-left: 3px solid var(--ice); }

/* Exception traces (st.exception) */
[data-testid="stException"] {
    background: rgba(10, 13, 28, 0.8);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    font-family: var(--font-mono);
}

/* ==========================================================================
   12. ANIMATION  (restrained)
   ========================================================================== */
@keyframes ultron-fade-up {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes ultron-glow {
    0%, 100% { filter: drop-shadow(0 0 16px rgba(183, 169, 217, 0.28)); }
    50%      { filter: drop-shadow(0 0 30px rgba(183, 169, 217, 0.50)); }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        transition: none !important;
    }
}

/* ==========================================================================
   13. RESPONSIVE
   ========================================================================== */
@media (max-width: 768px) {
    :root { --pad: 1rem; --gap: 0.9rem; --radius: 14px; }

    [data-testid="stMainBlockContainer"],
    .block-container { padding: 2rem 0.9rem 3.5rem; }

    [data-testid="stHeading"] h2 { letter-spacing: 0.28em; font-size: 0.75rem; }
    [data-testid="stMarkdownContainer"] h3 { font-size: 1.4rem; }
    [data-testid="stMetricValue"] { font-size: 2.1rem; }
    [data-testid="stText"] { font-size: 1.05rem; }

    [data-testid="stTable"],
    [data-testid="stJson"] { overflow-x: auto; }

    .stButton > button { width: 100%; letter-spacing: 0.2em; }

    .msg-operator { margin-right: 0; }
    .msg-ultron   { margin-left: 0; }
}
</style>
"""