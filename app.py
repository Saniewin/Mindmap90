"""
FACS Micro-Flash Recall & Micro-Expression Trainer (v2.0)
Rights & Intellectual Property Holder: Scott Niewinski

Interactive Streamlit application for practicing Facial Action Coding System (FACS)
Action Units, muscle mechanics, visual GIFs, micro-expression recognition (40ms - 200ms),
and Multi-AU Blend Scenarios (Fear-Surprise, Sadness-Anger, Disgust-Contempt, Anger-Contempt).
"""

import streamlit as st
import pandas as pd
import time
import math
import json
import random
import os
import hashlib

# Configuration
st.set_page_config(page_title="FACS Micro-Flash Recall Trainer v2.0 (Scott Niewinski IP)", page_icon="🎭", layout="wide")

CSV_PATH = "/workspace/artifacts/facs_flashcards.csv"
if not os.path.exists(CSV_PATH):
    CSV_PATH = "/workspace/scratch/facs_flashcards.csv"

# Load Card Database
@st.cache_data
def load_cards():
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH)
            return df.to_dict('records')
        except Exception:
            pass
    # Embedded Fallback Data
    return [
        {
            "Front": "Which specific muscle controls AU 1 (Inner Brow Raiser), and what is its morphological appearance?",
            "Back": "Muscle: Frontalis, pars medialis<br><br>Morphological Appearance: Elevates inner corners of eyebrows, creating central horizontal forehead wrinkles.<br><br>Source Grounding: FACS Learning Protocol Synthesis"
        },
        {
            "Front": "Which muscle group drives AU 4 (Brow Lowerer), and what distinct line configuration does it produce?",
            "Back": "Muscles: Corrugator supercilii, Depressor supercilii<br><br>Morphological Signature: Draws eyebrows medially/inferiorly (Omega pattern).<br><br>Source Grounding: FACS Learning Protocol Synthesis"
        },
        {
            "Front": "Which specific muscle controls AU 6 (Cheek Raiser), and why is it essential for verifying genuine affect?",
            "Back": "Muscle: Orbicularis oculi, pars orbitalis<br><br>Significance: Key marker of genuine Duchenne joy smile (AU 6 + AU 12). Driven by extrapyramidal motor system.<br><br>Source Grounding: FACS Learning Protocol Synthesis; Telling Lies.pdf"
        },
        {
            "Front": "Which muscle produces AU 14 (Dimpler), and what is its unique unilateral emotional blueprint?",
            "Back": "Muscle: Buccinator<br><br>Unilateral Blueprint: Tightens lip corners medially. Unilateral AU 14 is the universal blueprint for Contempt.<br><br>Source Grounding: FACS Learning Protocol Synthesis"
        }
    ]

cards_data = load_cards()

# Single AU GIF Map
GIF_MAP = {
    "AU 1 (Inner Brow Raiser)": "https://imotions.com/wp-content/uploads/2022/10/AU1-FACS.gif",
    "AU 4 (Brow Lowerer)": "https://imotions.com/wp-content/uploads/2022/10/AU4-brow-lowerer.gif",
    "AU 6 (Cheek Raiser / Duchenne)": "https://imotions.com/wp-content/uploads/2022/10/AU6-cheek-raiser.gif",
    "AU 9 (Nose Wrinkler)": "https://imotions.com/wp-content/uploads/2022/10/AU9-with-410.gif",
    "AU 11 (Nasolabial Deepener)": "https://imotions.com/wp-content/uploads/2022/10/AU11-nasolabial-deepener-1.gif",
    "AU 14 (Dimpler / Contempt)": "https://imotions.com/wp-content/uploads/2022/10/AU14-dimpler.gif",
    "AU 20 (Lip Stretcher / Fear)": "https://imotions.com/wp-content/uploads/2022/10/AU20-lip-stretcher.gif"
}

# Multi-AU Blend Scenarios Data
MULTI_AU_BLEND_SCENARIOS = {
    "Fear-Surprise Blend (AU 1+2+4+5+20)": {
        "title": "Fear vs. Surprise Differentiation Blend",
        "au_components": "AU 1 + AU 2 + AU 4 + AU 5 + AU 20",
        "primary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU20-lip-stretcher.gif",
        "secondary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU4-brow-lowerer.gif",
        "morphology_description": "Eyebrows raised AND drawn medially together by AU 4 (creating short central forehead furrows) paired with wide staring eyes (AU 5) and horizontal lip stretching (AU 20).",
        "differentiation_rule": "Pure surprise features curved high brows (AU 1+2) without AU 4 medial pull, and a relaxed jaw drop (AU 26). The presence of AU 4 + AU 20 confirms Fear/Threat anticipation.",
        "options": ["Fear-Surprise Blend (AU 1+2+4+5+20)", "Pure Surprise (AU 1+2+5+26)", "Sadness-Anger Blend (AU 1+4+7+15+23)", "Pure Disgust (AU 9+10)"]
    },
    "Sadness-Anger Blend (AU 1+4+7+15+23)": {
        "title": "Grief-Frustration / Sadness-Anger Blend",
        "au_components": "AU 1 + AU 4 + AU 7 + AU 15 + AU 23",
        "primary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU4-brow-lowerer.gif",
        "secondary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU1-FACS.gif",
        "morphology_description": "Inner brows raised and drawn medially (AU 1+4 'grief muscle') combined with tensed lower eyelids (AU 7), depressed lip corners (AU 15), and tightly narrowed lips (AU 23).",
        "differentiation_rule": "The inner brow elevation (AU 1+4) signals deep grief/sadness, while lower lid tightening (AU 7) and vermilion lip narrowing (AU 23) leak suppressed anger and hostility.",
        "options": ["Sadness-Anger Blend (AU 1+4+7+15+23)", "Pure Sadness (AU 1+4+15)", "Pure Anger (AU 4+5+7+23)", "Masked Joy (AU 12)"]
    },
    "Disgust-Contempt Blend (AU 9 + Unilateral AU 14)": {
        "title": "Visceral Distaste & Moral Superiority Blend",
        "au_components": "AU 9 + Unilateral AU 14",
        "primary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU9-with-410.gif",
        "secondary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU14-dimpler.gif",
        "morphology_description": "Transverse wrinkles across the nasal bridge (AU 9) paired with asymmetrical one-sided buccinator contraction and lip corner dimpling (unilateral AU 14).",
        "differentiation_rule": "Nasal wrinkling (AU 9) alone indicates physical/sensory aversion. The addition of asymmetrical AU 14 shifts the expression to interpersonal disdain and condescension.",
        "options": ["Disgust-Contempt Blend (AU 9 + Unilateral AU 14)", "Pure Disgust (AU 9)", "Pure Contempt (Unilateral AU 14)", "Squelched Anger (AU 23)"]
    },
    "Anger-Contempt Blend (AU 4+5+7 + Unilateral AU 14)": {
        "title": "Hostile Glare & Condescending Dimple Blend",
        "au_components": "AU 4 + AU 5 + AU 7 + Unilateral AU 14",
        "primary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU4-brow-lowerer.gif",
        "secondary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU14-dimpler.gif",
        "morphology_description": "Lowered glabella brows (AU 4), elevated upper lids exposing iris (AU 5), tensed lower lids (AU 7 'glare'), combined with unilateral cheek dimpling (AU 14).",
        "differentiation_rule": "Combines full orbital glare of active threat (AU 4+5+7) with unilateral asymmetrical lip tightness (AU 14), signaling hostile moral evaluation.",
        "options": ["Anger-Contempt Blend (AU 4+5+7 + Unilateral AU 14)", "Pure Anger (AU 4+5+7+23)", "Pure Contempt (Unilateral AU 14)", "Fear-Surprise Blend (AU 1+2+4+5+20)"]
    },
    "Suppressed Anger-Masked Joy (AU 4+23 + AU 12)": {
        "title": "Managed Social Mask Over Suppressed Hostility",
        "au_components": "AU 4 + AU 23 + AU 12 (No AU 6)",
        "primary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU4-brow-lowerer.gif",
        "secondary_gif": "https://imotions.com/wp-content/uploads/2022/10/AU11-nasolabial-deepener-1.gif",
        "morphology_description": "Zygomatic major lip corner puller (AU 12) attempting a smile, but lacking orbital crow's feet (AU 6), while glabella brows remain lowered (AU 4) and red lips are tightly compressed (AU 23).",
        "differentiation_rule": "Absence of AU 6 proves the smile is a cortical social mask (pyramidal), while AU 4 + AU 23 reveals underlying extrapyramidal anger.",
        "options": ["Suppressed Anger-Masked Joy (AU 4+23 + AU 12)", "Duchenne Joy (AU 6+12)", "Pure Sadness (AU 1+4+15)", "Pure Disgust (AU 9)"]
    }
}

st.title("🎭 FACS Micro-Flash Recall & Micro-Expression Trainer (v2.0)")
st.caption("Rights & Intellectual Property Holder: Scott Niewinski — Powered by SuperMemo Spaced Repetition, Ekman 40–200ms Micro-Expression Principles, and Multi-AU Blend Scenarios.")

# App Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "⏱️ Mode 1: Single AU Micro-Flash Speed Drill",
    "🎭 Mode 2: Multi-AU Blend Scenario Drills",
    "🎴 Mode 3: Spaced Repetition Flashcard Deck",
    "📊 Mode 4: Analytics & SuperMemo Memory Stability"
])

# -----------------------------------------------------------------------------
# TAB 1: Single AU Micro-Flash Speed Drill
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("⏱️ 40–200ms Single Action Unit Micro-Flash Drill")
    st.markdown("""
    Train your extrapyramidal visual recognition speed! Select a flash duration (from **40ms** micro-flashes up to **1000ms**).
    Click **Trigger Flash**, observe the momentary stimulus, and identify the hidden Action Unit or muscle from memory.
    """)

    col_cfg1, col_cfg2 = st.columns([1, 2])
    with col_cfg1:
        flash_duration = st.selectbox(
            "Select Flash Exposure Duration:",
            [40, 100, 200, 500, 1000],
            format_func=lambda x: f"{x} ms ({'Micro-Expression 1/25s' if x==40 else 'Micro-Flash 1/10s' if x==100 else 'Standard Micro 1/5s' if x==200 else 'Macro Exposure'})"
        )
        
        au_keys = list(GIF_MAP.keys())
        if "drill_target" not in st.session_state:
            st.session_state["drill_target"] = random.choice(au_keys)
            st.session_state["flashed"] = False
            st.session_state["drill_score"] = 0
            st.session_state["drill_attempts"] = 0

        if st.button("🔄 Next Random Single AU Stimulus"):
            st.session_state["drill_target"] = random.choice(au_keys)
            st.session_state["flashed"] = False
            st.rerun()

    with col_cfg2:
        current_target = st.session_state["drill_target"]
        gif_url = GIF_MAP[current_target]

        st.markdown(f"**Current Target:** Visual Stimulus (Masked)")

        flash_placeholder = st.empty()
        
        if not st.session_state["flashed"]:
            flash_placeholder.info("🔒 STIMULUS MASKED. Click button below to trigger micro-flash exposure.")
        else:
            flash_placeholder.success("⚡ STIMULUS FLASH COMPLETED & RE-MASKED. Select your diagnosis below.")

        if st.button("⚡ TRIGGER SINGLE AU MICRO-FLASH"):
            flash_placeholder.image(gif_url, caption=f"FLASH EXPOSURE ({flash_duration}ms)", width=350)
            time.sleep(flash_duration / 1000.0)
            flash_placeholder.warning("🔒 STIMULUS RE-MASKED — Time's Up!")
            st.session_state["flashed"] = True

    st.markdown("---")
    st.subheader("Diagnose the Flashed Action Unit:")
    
    choice_cols = st.columns(4)
    user_choice = None
    for idx, au in enumerate(au_keys):
        with choice_cols[idx % 4]:
            if st.button(f"{au}", key=f"btn_au_{au}"):
                user_choice = au

    if user_choice:
        st.session_state["drill_attempts"] += 1
        if user_choice == current_target:
            st.session_state["drill_score"] += 1
            st.balloons()
            st.success(f"🎉 CORRECT! Identified **{current_target}** at {flash_duration}ms exposure speed!")
        else:
            st.error(f"❌ INCORRECT. Flashed stimulus was **{current_target}** (You selected {user_choice}).")

        st.info(f"**Single AU Drill Score:** {st.session_state['drill_score']} / {st.session_state['drill_attempts']} Correct ({ (st.session_state['drill_score']/st.session_state['drill_attempts'])*100:.1f}%)")

# -----------------------------------------------------------------------------
# TAB 2: Multi-AU Blend Scenario Drills
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("🎭 Multi-AU Blend Micro-Flash Scenario Drills")
    st.markdown("""
    In real-world interrogations and high-stakes social interactions, emotional leakage rarely occurs as isolated Action Units.
    **Multi-AU Blends** combine upper and lower facial movements across opposing emotional vectors (e.g., Fear-Surprise or Suppressed Anger under a Social Smile).
    """)

    b_col1, b_col2 = st.columns([1, 1])
    
    with b_col1:
        blend_duration = st.selectbox(
            "Select Blend Exposure Duration (ms):",
            [40, 100, 200, 500, 1000],
            key="blend_duration_select",
            format_func=lambda x: f"{x} ms ({'Micro-Flash 1/25s' if x==40 else 'Standard Micro 1/5s' if x==200 else 'Macro Exposure'})"
        )
        
        blend_keys = list(MULTI_AU_BLEND_SCENARIOS.keys())
        if "blend_target_key" not in st.session_state:
            st.session_state["blend_target_key"] = random.choice(blend_keys)
            st.session_state["blend_flashed"] = False
            st.session_state["blend_score"] = 0
            st.session_state["blend_attempts"] = 0

        if st.button("🔄 Next Random Multi-AU Blend"):
            st.session_state["blend_target_key"] = random.choice(blend_keys)
            st.session_state["blend_flashed"] = False
            st.rerun()

        target_scenario = MULTI_AU_BLEND_SCENARIOS[st.session_state["blend_target_key"]]
        st.markdown(f"### Target Scenario: `{target_scenario['title']}`")

        blend_flash_box = st.empty()
        
        if not st.session_state["blend_flashed"]:
            blend_flash_box.info("🔒 MULTI-AU BLEND STIMULUS MASKED. Click button below to trigger exposure.")
        else:
            blend_flash_box.success("⚡ MULTI-AU BLEND FLASH COMPLETED. Select your clinical diagnosis below.")

        if st.button("⚡ TRIGGER MULTI-AU BLEND MICRO-FLASH"):
            blend_flash_box.markdown(f"**Action Unit Cluster:** `{target_scenario['au_components']}`")
            g_col_a, g_col_b = blend_flash_box.columns(2)
            g_col_a.image(target_scenario["primary_gif"], caption="Primary AU Movement", width=220)
            g_col_b.image(target_scenario["secondary_gif"], caption="Secondary Co-occurring AU", width=220)
            
            time.sleep(blend_duration / 1000.0)
            blend_flash_box.warning("🔒 MULTI-AU STIMULUS RE-MASKED — Time's Up!")
            st.session_state["blend_flashed"] = True

    with b_col2:
        st.markdown("### Diagnose the Multi-AU Blend Scenario:")
        
        selected_blend_diagnosis = st.radio(
            "Select the correct emotional blend and Action Unit composition:",
            target_scenario["options"],
            key="radio_blend_diagnosis"
        )

        if st.button("Submit Multi-AU Diagnosis"):
            st.session_state["blend_attempts"] += 1
            if selected_blend_diagnosis == st.session_state["blend_target_key"]:
                st.session_state["blend_score"] += 1
                st.balloons()
                st.success(f"🎉 CORRECT DIAGNOSIS! You identified **{st.session_state['blend_target_key']}**!")
            else:
                st.error(f"❌ INCORRECT. Flashed scenario was **{st.session_state['blend_target_key']}**.")

            st.markdown("#### 🧠 Clinical Differentiation & Rule-Out Grounding:")
            st.info(f"**Morphology:** {target_scenario['morphology_description']}\n\n**Rule-Out Logic:** {target_scenario['differentiation_rule']}")
            st.metric("Multi-AU Drill Accuracy", f"{(st.session_state['blend_score'] / st.session_state['blend_attempts']) * 100:.1f}%", f"{st.session_state['blend_score']}/{st.session_state['blend_attempts']} Correct")

# -----------------------------------------------------------------------------
# TAB 3: Spaced Repetition Flashcards
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("🎴 FACS Spaced Repetition Review Deck")
    
    if "card_idx" not in st.session_state:
        st.session_state["card_idx"] = 0
        st.session_state["show_answer"] = False

    total_c = len(cards_data)
    curr_card = cards_data[st.session_state["card_idx"] % total_c]

    st.progress((st.session_state["card_idx"] + 1) / total_c)
    st.caption(f"Card {st.session_state['card_idx'] + 1} of {total_c}")

    f_col, b_col = st.columns(2)
    with f_col:
        st.markdown("### ❓ Front (Question / Prompt)")
        st.info(curr_card["Front"])

    with b_col:
        st.markdown("### 💡 Back (Answer & Grounding)")
        if st.session_state["show_answer"]:
            st.success(curr_card["Back"].replace("<br>", "\n\n"))
        else:
            st.warning("🔒 Click 'Reveal Answer' below to verify your recall.")

    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)

    if not st.session_state["show_answer"]:
        if c1.button("👁️ Reveal Answer", use_container_width=True):
            st.session_state["show_answer"] = True
            st.rerun()
    else:
        if c2.button("🔴 Again (S x0.8)", use_container_width=True):
            st.session_state["card_idx"] += 1
            st.session_state["show_answer"] = False
            st.rerun()
        if c3.button("🟠 Hard (S x1.2)", use_container_width=True):
            st.session_state["card_idx"] += 1
            st.session_state["show_answer"] = False
            st.rerun()
        if c4.button("🟢 Good (S x1.5)", use_container_width=True):
            st.session_state["card_idx"] += 1
            st.session_state["show_answer"] = False
            st.rerun()
        if c5.button("🔵 Easy (S x2.0)", use_container_width=True):
            st.session_state["card_idx"] += 1
            st.session_state["show_answer"] = False
            st.rerun()

# -----------------------------------------------------------------------------
# TAB 4: Analytics & SuperMemo Memory Stability
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("📊 Memory Stability (S) & Retrievability (R) Analytics")
    
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("Total Cards Loaded", len(cards_data))
    
    single_acc = (st.session_state.get('drill_score', 0) / max(1, st.session_state.get('drill_attempts', 1))) * 100
    m_col2.metric("Single AU Drill Accuracy", f"{single_acc:.1f}%")

    blend_acc = (st.session_state.get('blend_score', 0) / max(1, st.session_state.get('blend_attempts', 1))) * 100
    m_col3.metric("Multi-AU Blend Drill Accuracy", f"{blend_acc:.1f}%")

    st.markdown("### SuperMemo Retrievability Decay Formula:")
    st.latex(r"R(t) = e^{-\frac{\ln(2) \cdot t}{S}}")
    st.caption("Where $t$ is days elapsed since last practice, and $S$ is memory stability in days.")

    df_cards = pd.DataFrame(cards_data)
    st.dataframe(df_cards, use_container_width=True)
