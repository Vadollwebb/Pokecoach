import streamlit as st

# Set Page Configuration
st.set_page_config(
    page_title="Master Decision Framework: Battle & Navigation Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Visual Polish
st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1E293B; margin-bottom: 0px; }
    .sub-title { font-size: 1.05rem; color: #64748B; margin-bottom: 20px; }
    .card-box { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 16px; margin-bottom: 12px; }
    .law-badge { background-color: #2563EB; color: white; padding: 3px 8px; border-radius: 5px; font-weight: 600; font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)

# Navigation Sidebar
st.sidebar.title("🧠 Framework Navigation")
menu = st.sidebar.radio(
    "Select View Mode:",
    ["🎮 Interactive Battle Simulator", "📚 7 Laws & Infrastructure Encyclopedia", "🔍 Replay & Diagnostic Audit Tool", "🚀 Deployment & Sharing Guide"]
)

# Initialize Session State
if "turn" not in st.session_state:
    st.session_state.turn = 1
if "history" not in st.session_state:
    st.session_state.history = []
if "player_hp" not in st.session_state:
    st.session_state.player_hp = {"Rotom-Wash": 100, "Heatran": 100, "Garchomp": 100}
if "opp_hp" not in st.session_state:
    st.session_state.opp_hp = {"Landorus-Therian": 100, "Ferrothorn": 100, "Dragapult": 100}
if "opp_status" not in st.session_state:
    st.session_state.opp_status = {"Landorus-Therian": "Healthy", "Ferrothorn": "Healthy", "Dragapult": "Healthy"}
if "active_player" not in st.session_state:
    st.session_state.active_player = "Rotom-Wash"
if "active_opp" not in st.session_state:
    st.session_state.active_opp = "Landorus-Therian"
if "stealth_rock" not in st.session_state:
    st.session_state.stealth_rock = False
if "choice_locked" not in st.session_state:
    st.session_state.choice_locked = None
if "trapped_opp" not in st.session_state:
    st.session_state.trapped_opp = False

def reset_sim():
    st.session_state.turn = 1
    st.session_state.history = []
    st.session_state.player_hp = {"Rotom-Wash": 100, "Heatran": 100, "Garchomp": 100}
    st.session_state.opp_hp = {"Landorus-Therian": 100, "Ferrothorn": 100, "Dragapult": 100}
    st.session_state.opp_status = {"Landorus-Therian": "Healthy", "Ferrothorn": "Healthy", "Dragapult": "Healthy"}
    st.session_state.active_player = "Rotom-Wash"
    st.session_state.active_opp = "Landorus-Therian"
    st.session_state.stealth_rock = False
    st.session_state.choice_locked = None
    st.session_state.trapped_opp = False

# ==========================================
# MODE 1: INTERACTIVE BATTLE SIMULATOR
# ==========================================
if menu == "🎮 Interactive Battle Simulator":
    st.markdown("<div class='main-title'>🎮 Interactive Strategic Simulator</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Train critical thinking across the 4 Core Actions, 3 Phases of Play, and 7 Laws of Strategy.</div>", unsafe_allow_html=True)
    
    col_reset, col_space = st.columns([1.5, 5])
    with col_reset:
        if st.button("🔄 Reset Scenario"):
            reset_sim()
            st.rerun()

    st.divider()

    # --- BATTLEFIELD STATUS ---
    col_player, col_vs, col_opp = st.columns([4, 1, 4])
    
    with col_player:
        st.subheader("🔵 Your Field (Player)")
        active_p = st.session_state.active_player
        hp_p = st.session_state.player_hp[active_p]
        st.markdown(f"**Active:** `{active_p}` | **HP:** `{hp_p}%`")
        st.progress(hp_p / 100.0)
        
        if st.session_state.stealth_rock:
            st.warning("⚠️ Field Hazard: Stealth Rock active on your side")
        if st.session_state.choice_locked:
            st.info(f"🔒 Choice Lock: Locked into `{st.session_state.choice_locked}`")
            
        st.markdown("**Team Bench:**")
        b_cols = st.columns(3)
        for idx, (p_name, p_hp) in enumerate(st.session_state.player_hp.items()):
            with b_cols[idx]:
                st.caption(f"{'⭐ ' if p_name == active_p else ''}{p_name}: {p_hp}% HP")

    with col_vs:
        st.markdown("<h2 style='text-align: center; margin-top: 25px;'>VS</h2>", unsafe_allow_html=True)
        st.caption(f"Turn {st.session_state.turn}")

    with col_opp:
        st.subheader("🔴 Opponent Field")
        active_o = st.session_state.active_opp
        hp_o = st.session_state.opp_hp[active_o]
        status_o = st.session_state.opp_status[active_o]
        st.markdown(f"**Active:** `{active_o}` | **HP:** `{hp_o}%` | **Status:** `{status_o}`")
        st.progress(hp_o / 100.0)
        
        if st.session_state.trapped_opp:
            st.error("🕸️ Trapped: Magma Storm prevents switching")
            
        st.markdown("**Opponent Bench:**")
        ob_cols = st.columns(3)
        for idx, (o_name, o_hp) in enumerate(st.session_state.opp_hp.items()):
            with ob_cols[idx]:
                o_stat = st.session_state.opp_status[o_name]
                st.caption(f"{'⭐ ' if o_name == active_o else ''}{o_name}: {o_hp}% ({o_stat})")

    st.divider()

    # --- TURN DECISION ENGINE ---
    turn = st.session_state.turn
    st.subheader(f"⚡ Turn {turn}: Choose Your Core Action Category")

    if turn == 1:
        st.markdown("""
        **Preview Summary:** You lead **Rotom-Wash** against the opponent's **Landorus-Therian**. 
        You anticipate Landorus-T might carry a Choice Scarf or switch to Ferrothorn.
        """)
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown("### ⚔️ 1. Attack (*Attempt*)")
            st.caption("Use **Hydro Pump**")
            st.write("Direct heavy damage if Landorus stays in.")
            if st.button("Execute Hydro Pump", key="t1_atk"):
                st.session_state.opp_hp["Ferrothorn"] = 82
                st.session_state.active_opp = "Ferrothorn"
                st.session_state.choice_locked = "Hydro Pump"
                st.session_state.turn = 2
                st.session_state.history.append({
                    "turn": 1,
                    "action": "Attack (Hydro Pump)",
                    "res": "Landorus U-turned into Ferrothorn! Hydro Pump dealt 18% damage to Ferrothorn (resisted). Rotom-Wash is choice-locked into Hydro Pump.",
                    "law": "Law 3: Presumption & Expectation",
                    "law_title": "Unhedged Prediction Risk",
                    "origin": "Assuming the opponent stays in without preparing for the switch leads to low-value turns.",
                    "why": "Attacking directly is high-value when the target cannot safely switch out.",
                    "pain": "Taking minimal value against a wall and choice locking your move.",
                    "question": "What happens to my route if the opponent switches to their best wall?"
                })
                st.rerun()

        with c2:
            st.markdown("### 🛡️ 2. Defend (*Preserve*)")
            st.caption("Use **Will-O-Wisp**")
            st.write("Permanent burn to cripple physical attackers.")
            if st.button("Execute Will-O-Wisp", key="t1_def"):
                st.session_state.player_hp["Rotom-Wash"] = 78
                st.session_state.opp_status["Ferrothorn"] = "🔥 Burned"
                st.session_state.active_opp = "Ferrothorn"
                st.session_state.choice_locked = "Will-O-Wisp"
                st.session_state.turn = 2
                st.session_state.history.append({
                    "turn": 1,
                    "action": "Defend (Will-O-Wisp)",
                    "res": "Landorus U-turned (dealing 22% to Rotom) into Ferrothorn! Will-O-Wisp hits Ferrothorn on the switch, permanently burning it!",
                    "law": "Law 3: Presumption & Expectation & Law 7: Function",
                    "law_title": "Conditional High-Floor Play",
                    "origin": "Distinguishing expected outcome from reality.",
                    "why": "Will-O-Wisp generated permanent value regardless of whether Landorus stayed or switched.",
                    "pain": "Failing to account for alternative switches leaves you open to momentum loss.",
                    "question": "Does my choice secure value across multiple plausible opponent moves?"
                })
                st.rerun()

        with c3:
            st.markdown("### 📈 3. Set Up (*Prepare*)")
            st.caption("Use **Trick** (Choice Scarf)")
            st.write("Swap item to lock an incoming wall.")
            if st.button("Execute Trick", key="t1_setup"):
                st.session_state.opp_status["Ferrothorn"] = "🔒 Tricked Scarf"
                st.session_state.active_opp = "Ferrothorn"
                st.session_state.turn = 2
                st.session_state.history.append({
                    "turn": 1,
                    "action": "Set Up (Trick Choice Scarf)",
                    "res": "Landorus U-turned into Ferrothorn! Rotom Tricked Choice Scarf onto Ferrothorn, locking Ferrothorn into a single move!",
                    "law": "Law 7: Function & Law 6: Value Exchange",
                    "law_title": "Functional Neutralization",
                    "origin": "Assessing a tool by what it prevents rather than raw stats.",
                    "why": "Permanently stripping Ferrothorn's tactical flexibility disables its main role.",
                    "pain": "Allowing defensive walls to set hazards unhindered.",
                    "question": "What tool does the opponent rely on that I can functionally neutralize?"
                })
                st.rerun()

        with c4:
            st.markdown("### 🔄 4. Switch (*Pivot*)")
            st.caption("Switch to **Garchomp**")
            st.write("Hard switch to your physical wallbreaker.")
            if st.button("Switch to Garchomp", key="t1_sw"):
                st.session_state.active_player = "Garchomp"
                st.session_state.active_opp = "Ferrothorn"
                st.session_state.turn = 2
                st.session_state.history.append({
                    "turn": 1,
                    "action": "Switch (Garchomp)",
                    "res": "Landorus U-turned into Ferrothorn! Your Garchomp enters the field facing Ferrothorn.",
                    "law": "Law 1: Mind & Law 5: Action & Reaction",
                    "law_title": "Positioning vs Access",
                    "origin": "Recognizing that possessing a tool is useless without position.",
                    "why": "Brings your physical threat directly into the match.",
                    "pain": "Hard switching into a wall that can set Stealth Rock or status you.",
                    "question": "Am I switching into a position of strength or reaction?"
                })
                st.rerun()

    elif turn == 2:
        st.markdown(f"""
        **Context:** Rotom-Wash is currently on the field facing **Ferrothorn ({st.session_state.opp_status['Ferrothorn']})**.
        *Mechanical Constraint:* If Rotom used Will-O-Wisp while holding Choice Scarf, it is Choice-Locked into Will-O-Wisp!
        """)
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown("### ⚔️ 1. Repeat Move")
            st.caption("Use **Will-O-Wisp** again")
            st.write("Has 0 effect against an already burned Ferrothorn.")
            if st.button("Repeat Move", key="t2_repeat"):
                st.session_state.turn = 3
                st.session_state.history.append({
                    "turn": 2,
                    "action": "Attack/Defend (Repeat Lock)",
                    "res": "Will-O-Wisp fails! Ferrothorn sets up Stealth Rock on your field.",
                    "law": "Law 1: Mechanics Dictate Options",
                    "law_title": "Choice Lock Penalty",
                    "origin": "Mechanical constraints overwrite strategic desires.",
                    "why": "Repeating a locked non-damaging move wastes your positioning advantage.",
                    "pain": "Wasting a free turn and allowing free hazards.",
                    "question": "Does my item or state restrict my options this turn?"
                })
                st.rerun()

        with c2:
            st.markdown("### 🔄 2. Hard Switch (*Pivot*)")
            st.caption("Switch to **Heatran**")
            st.write("Heatran walls Ferrothorn completely and threatens massive Fire damage.")
            if st.button("Switch to Heatran", key="t2_heatran"):
                st.session_state.active_player = "Heatran"
                st.session_state.stealth_rock = True
                st.session_state.choice_locked = None
                st.session_state.turn = 3
                st.session_state.history.append({
                    "turn": 2,
                    "action": "Switch (Heatran)",
                    "res": "You switched to Heatran! Ferrothorn used Stealth Rock. Heatran enters at 100% HP counter-positioning Ferrothorn.",
                    "law": "Law 7: Function & Law 6: Value Exchange",
                    "law_title": "Resetting Constraints & Position Advantage",
                    "origin": "Switching resets Choice Scarf move lock while taking position advantage.",
                    "why": "Heatran forces Ferrothorn out immediately, regaining proactive control.",
                    "pain": "Staying in a locked move rather than resetting through a pivot.",
                    "question": "How can I reset my tool's constraints while gaining matchup leverage?"
                })
                st.rerun()

        with c3:
            st.markdown("### 🔄 3. Hard Switch (*Pivot*)")
            st.caption("Switch to **Garchomp**")
            st.write("Bring Garchomp in, taking 12% Stealth Rock damage.")
            if st.button("Switch to Garchomp", key="t2_garchomp"):
                st.session_state.active_player = "Garchomp"
                st.session_state.player_hp["Garchomp"] = 88
                st.session_state.stealth_rock = True
                st.session_state.choice_locked = None
                st.session_state.turn = 3
                st.session_state.history.append({
                    "turn": 2,
                    "action": "Switch (Garchomp)",
                    "res": "You switched to Garchomp (took 12% hazard damage)! Ferrothorn used Stealth Rock.",
                    "law": "Law 6: Value Exchange",
                    "law_title": "Resource Expenditure for Initiative",
                    "origin": "Spending HP value (12% hazard) to gain turn initiative.",
                    "why": "Establishes physical pressure at a minor resource cost.",
                    "pain": "Unnecessary chip damage if Garchomp has no immediate KO route.",
                    "question": "Is the HP spent worth the position gained?"
                })
                st.rerun()

        with c4:
            st.markdown("### 🛡️ 4. Stay & Pivot")
            st.caption("Use **Volt Switch**")
            st.write("Allowed if NOT choice locked into Will-O-Wisp.")
            if st.button("Volt Switch", key="t2_volt"):
                st.session_state.turn = 3
                st.session_state.history.append({
                    "turn": 2,
                    "action": "Pivot Attack",
                    "res": "Rotom used Volt Switch (chipped Ferrothorn) and pivoted safely to Heatran!",
                    "law": "Law 4: Risk Mitigation",
                    "law_title": "Pivot Momentum",
                    "origin": "Combining damage and repositioning in a single turn.",
                    "why": "Gains information on opponent's response before sending in Heatran.",
                    "pain": "Getting choice locked if item mechanics were ignored.",
                    "question": "Can I combine damage and repositioning to maintain initiative?"
                })
                st.rerun()

    elif turn == 3:
        st.markdown("""
        **Context:** Your **Heatran (100% HP)** faces a burned **Ferrothorn (82% HP)**. 
        Ferrothorn cannot stay in without taking heavy Fire damage. Opponent will likely switch to **Dragapult** or **Landorus-T**.
        """)
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown("### ⚔️ 1. Attack (*Attempt*)")
            st.caption("Use **Magma Storm**")
            st.write("Heavy Fire damage; traps and chips incoming switch-ins.")
            if st.button("Execute Magma Storm", key="t3_magma"):
                st.session_state.opp_hp["Dragapult"] = 43
                st.session_state.active_opp = "Dragapult"
                st.session_state.trapped_opp = True
                st.session_state.turn = 4
                st.session_state.history.append({
                    "turn": 3,
                    "action": "Attack (Magma Storm)",
                    "res": "Ferrothorn switched out to Dragapult! Magma Storm hit Dragapult for 52% damage and trapped it on the field!",
                    "law": "Law 1: Direct Progress & Law 4: Risk Mitigation",
                    "law_title": "Direct Progress & Trapping Leverage",
                    "origin": "Using high-powered neutral attacks that punish any switch.",
                    "why": "Guarantees heavy damage and eliminates opponent's ability to pivot Dragapult out.",
                    "pain": "Over-complicating forced-switch turns with unneeded reads.",
                    "question": "Does this move punish both staying in and switching out?"
                })
                st.rerun()

        with c2:
            st.markdown("### 📈 2. Set Up (*Prepare*)")
            st.caption("Use **Stealth Rock**")
            st.write("Set entry hazards as opponent switches.")
            if st.button("Execute Stealth Rock", key="t3_sr"):
                st.session_state.active_opp = "Dragapult"
                st.session_state.turn = 4
                st.session_state.history.append({
                    "turn": 3,
                    "action": "Set Up (Stealth Rock)",
                    "res": "Ferrothorn switched to Dragapult! Heatran set up Stealth Rock.",
                    "law": "Law 6: Value Exchange (Long Term)",
                    "law_title": "Long-term Hazard Preparation",
                    "origin": "Exchanging immediate direct damage for cumulative multi-turn pressure.",
                    "why": "Chips Dragapult and Landorus-T every time they enter later.",
                    "pain": "Giving Dragapult a free safe entry without taking damage.",
                    "question": "Is setting hazards right now more valuable than removing 50% of Dragapult's HP?"
                })
                st.rerun()

        with c3:
            st.markdown("### ⚔️ 3. Predictive Attack")
            st.caption("Use **Earth Power**")
            st.write("⚠️ *Note:* Landorus-T is Flying-type (Immune to Ground!).")
            if st.button("Execute Earth Power", key="t3_ep"):
                st.session_state.active_opp = "Dragapult"
                st.session_state.opp_hp["Dragapult"] = 72
                st.session_state.turn = 4
                st.session_state.history.append({
                    "turn": 3,
                    "action": "Predictive Attack (Earth Power)",
                    "res": "Ferrothorn switched to Dragapult. Earth Power hit Dragapult for neutral 28% damage. (If Landorus came in, it would be immune!).",
                    "law": "Law 1: Game Mechanics & Law 3: Presumption",
                    "law_title": "Type Immunity Failure Mode",
                    "origin": "Failing to account for type immunities in predictive coverage.",
                    "why": "Ground attacks carry 0 value against Flying-type switch-ins like Landorus-T.",
                    "pain": "Wasting position advantage on a move that deals 0 damage to a key threat.",
                    "question": "Is my coverage move safe against ALL likely switch-ins?"
                })
                st.rerun()

        with c4:
            st.markdown("### 🔄 4. Switch (*Pivot*)")
            st.caption("Switch to **Garchomp**")
            st.write("Predict Landorus-T and intercept.")
            if st.button("Switch to Garchomp", key="t3_garchomp"):
                st.session_state.active_player = "Garchomp"
                st.session_state.active_opp = "Dragapult"
                st.session_state.turn = 4
                st.session_state.history.append({
                    "turn": 3,
                    "action": "Switch (Garchomp)",
                    "res": "Ferrothorn switched to Dragapult as you switched to Garchomp! Now Garchomp faces Dragapult.",
                    "law": "Law 3: Presumption & Law 4: Risk",
                    "law_title": "Unhedged Prediction Penalty",
                    "origin": "Switching out of a winning position based on an unconfirmed read.",
                    "why": "Gives up Heatran's dominant position and puts Garchomp in a bad speed matchup.",
                    "pain": "Surrendering position advantage when you had complete board control.",
                    "question": "Why switch away from a position where you hold total advantage?"
                })
                st.rerun()

    else:
        st.success("🎉 Scenario Complete! Review your Diagnostic Audit log below.")

    # --- TURN HISTORY & DIAGNOSTIC CARDS ---
    st.divider()
    st.subheader("📜 Decision Log & Diagnostic Cards")
    
    for log in reversed(st.session_state.history):
        with st.expander(f"Turn {log['turn']}: {log['action']} — {log['law_title']}", expanded=True):
            st.markdown(f"**Outcome:** {log['res']}")
            st.markdown(f"<span class='law-badge'>{log['law']}</span>", unsafe_allow_html=True)
            
            c_a, c_b = st.columns(2)
            with c_a:
                st.markdown(f"**🏛️ Origin:** {log['origin']}")
                st.markdown(f"**🎯 Strategic Value:** {log['why']}")
            with c_b:
                st.markdown(f"**💥 Failure Mode / Pain Point:** {log['pain']}")
                st.markdown(f"**❓ Diagnostic Question:** *\"{log['question']}\"*")

# ==========================================
# MODE 2: 7 LAWS & INFRASTRUCTURE ENCYCLOPEDIA
# ==========================================
elif menu == "📚 7 Laws & Infrastructure Encyclopedia":
    st.markdown("<div class='main-title'>📚 The Seven Laws & Core Infrastructure</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Deep-dive into the foundational principles governing human reasoning under uncertainty.</div>", unsafe_allow_html=True)
    
    laws_data = [
        {
            "num": "Law 1",
            "name": "The Law of Mind",
            "principle": "Competitive play is an internal, cognitive martial art. Results depend on mental faculties (Memory, Imagination, Intellect) and mental state.",
            "origin": "Separating external game tools from the internal cognitive representation constructed in the player's brain.",
            "pain": "Believing a tool or move is useless because of an unexamined false mental model (e.g. ignoring Choice Specs Aegislash).",
            "question": "Am I assessing my tools based on objective reality or an outdated mental model?"
        },
        {
            "num": "Law 2",
            "name": "The Law of Questions",
            "principle": "Questions are the cardinal mechanism of critical thinking. They direct attention, trigger memory recall, and activate reasoning.",
            "origin": "Cognitive psychology: attention follows deliberate questioning rather than random thought impulses.",
            "pain": "Playing on autopilot, reacting impulsively to screen events instead of actively directing awareness.",
            "question": "What specific problem am I solving on this exact turn?"
        },
        {
            "num": "Law 3",
            "name": "Presumption & Expectation",
            "principle": "Presumptions inform expected consequences, and expected consequences inform choices. Expected outcomes and actual observations are distinct records.",
            "origin": "Distinguishing internal belief/interpretation from empirical board observations.",
            "pain": "Getting blindsided by a hidden set (e.g. Scarf Heatran) because you assumed observed behavior proved the underlying set.",
            "question": "What am I assuming? What supports that assumption? What if it proves false?"
        },
        {
            "num": "Law 4",
            "name": "Luck & Risk",
            "principle": "Choices influence the likelihood and magnitude of outcomes; realized benefits remain conditional. Manage risk vs reward systematically.",
            "origin": "Evaluating probability and variance across 4 zones: Safe Zone, Opportunity Zone, High Stakes, and No-Win Zone.",
            "pain": "Making 70% win-rate gambles when a slower 100% win-route exists, then blaming 'bad luck'.",
            "question": "Is this risk necessary, or is there a safer conditional route to victory?"
        },
        {
            "num": "Law 5",
            "name": "Action & Reaction",
            "principle": "Actions resolve in interaction with the opponent and environment. You influence opponent incentives, but do not dictate exact responses.",
            "origin": "Game theory & turn cycle dynamics (Input -> Output -> Recalibration).",
            "pain": "Formulating brittle plans that collapse the moment the opponent doesn't do what you predicted.",
            "question": "How does my choice restrict the opponent's favorable options on their next turn?"
        },
        {
            "num": "Law 6",
            "name": "Value Exchange",
            "principle": "Turns involve gains, losses, preservation, and expenditure of value (HP, PP, status, time, position). Strategic contribution exceeds raw resources.",
            "origin": "Resource accounting vs strategic utility (spending HP value to gain position leverage).",
            "pain": "Preserving raw health on a Pokémon that has lost its intended strategic function.",
            "question": "Does saving this resource help me reach my win condition, or am I preserving it aimlessly?"
        },
        {
            "num": "Law 7",
            "name": "The Law of Function",
            "principle": "Tools are evaluated by what they contribute, prevent, and enable under current context—not static base stats.",
            "origin": "Functional analysis of capabilities (Attributes -> Operations -> Contribution).",
            "pain": "Evaluating a Pokémon purely by base stats rather than its specific metagame role and matchup synergy.",
            "question": "What specific capability does this tool enable for my entire win route?"
        }
    ]

    for law in laws_data:
        with st.expander(f"🏛️ {law['num']}: {law['name']}", expanded=True):
            st.markdown(f"**Core Principle:** {law['principle']}")
            st.markdown(f"**📜 Origin:** {law['origin']}")
            st.markdown(f"**💥 Failure Mode (The Pain):** {law['pain']}")
            st.markdown(f"**❓ Diagnostic Question:** *\"{law['question']}\"*")

# ==========================================
# MODE 3: REPLAY & DIAGNOSTIC AUDIT TOOL
# ==========================================
elif menu == "🔍 Replay & Diagnostic Audit Tool":
    st.markdown("<div class='main-title'>🔍 Replay & Diagnostic Audit Tool</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Locate the exact root cause of a failure across the 3 Phases of Play.</div>", unsafe_allow_html=True)
    
    st.write("Select the symptoms experienced in a recent match or project plan to diagnose where the failure occurred:")
    
    q1 = st.checkbox("My team/toolset lacked any reliable answer to a common threat from the start.")
    q2 = st.checkbox("I had the right tools, but at Team Preview I picked a flawed lead or misidentified my win condition.")
    q3 = st.checkbox("I made a move expecting one specific response, and when the opponent did something else, my plan collapsed.")
    q4 = st.checkbox("I held on to raw HP/resources on a Pokémon that had already lost its strategic purpose.")
    q5 = st.checkbox("I failed to update my plan after key hidden information (e.g. Choice Scarf, item, move) was revealed.")

    if st.button("🔍 Run Diagnostic Audit"):
        st.subheader("📋 Diagnostic Results & Recalibration Steps")
        
        if q1:
            st.error("❌ Phase 1 Failure: Creation / Teambuilding")
            st.markdown("**Diagnosis:** Structural gap in toolkit capability. Your team lacked the necessary synergy or type coverage.")
            st.markdown("**Fix:** Revise team structure to include a functional answer to this threat before battling again.")
            
        if q2:
            st.warning("⚠️ Phase 2 Failure: Preview / Planning")
            st.markdown("**Diagnosis:** GPS Planning failure. You entered execution without identifying what you couldn't guard against.")
            st.markdown("**Fix:** Ask the 2 Preview Questions: *'What can't he guard against?'* and *'What can't I guard against?'* before selecting a lead.")
            
        if q3 or q4 or q5:
            st.info("⚡ Phase 3 Failure: Execution & Recalibration")
            st.markdown("**Diagnosis:** Execution / Law 3 & Law 6 failure. You confused prediction with broad anticipation or preserved raw resources aimlessly.")
            st.markdown("**Fix:** Apply Divergent Thinking (generate 3+ options per turn) and ask *'If I do this, then what?'* to verify both short and long-term consequences.")

# ==========================================
# MODE 4: DEPLOYMENT & SHARING GUIDE
# ==========================================
elif menu == "🚀 Deployment & Sharing Guide":
    st.markdown("<div class='main-title'>🚀 Deploy as a Public Web App</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>How to publish this interactive simulator as a free public website for anyone to use.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 📌 Step-by-Step Free Deployment Instructions
    
    1. **Save this Python file:** Download or copy `pokemon_framework_app.py` from your workspace.
    2. **Create a Free Code Repository:**
       - Create a repository on your code hosting platform (e.g. GitHub).
       - Add `pokemon_framework_app.py` and a `requirements.txt` file containing:
         ```text
         streamlit>=1.30.0
         pandas>=2.0.0
         ```
    3. **Deploy on Free App Hosting (e.g. Streamlit Cloud):**
       - Connect your repository to your free app hosting dashboard.
       - Select `pokemon_framework_app.py` and click **Deploy**.
    4. **Share Your Live Link:**
       - Streamlit generates a public link that anyone can open on mobile or desktop!
    """)
