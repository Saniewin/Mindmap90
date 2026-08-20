import streamlit as st

# STREAMLIT PAGE CONFIGURATION & DESKTOP WIDE-LAYOUT
st.set_page_config(
    page_title="Psychology Mindmap Guide",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Dark Purple, Digital Scientific & Matrix-inspired theme (Purple, Green, and White color scheme)
st.markdown("""
<style>
    /* Main body background & Scientific-Digital canvas layout */
    .stApp {
        background: radial-gradient(circle at center, #1E052D 0%, #0C0117 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
        position: relative;
    }
    
    /* Glowing digital grid overlay */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 102, 0.015) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 102, 0.015) 1px, transparent 1px);
        background-size: 25px 20px;
        pointer-events: none;
        z-index: 0;
    }

    /* Device frame mockup for Samsung S26 Ultra centered canvas */
    @media (min-width: 450px) {
        .block-container {
            max-width: 440px !important;
            padding: 24px !important;
            background: rgba(18, 4, 30, 0.95) !important;
            border-radius: 40px !important;
            box-shadow: 0 0 40px rgba(0, 255, 102, 0.15) !important;
            margin-top: 15px !important;
            margin-bottom: 25px !important;
            border: 4px solid #4E146F !important; /* Deep Purple Frame */
            position: relative;
            z-index: 1;
        }
    }
    
    /* Scientific holographic card styling */
    .mindmap-node-card {
        background: rgba(30, 8, 48, 0.85) !important;
        border: 1px solid rgba(0, 255, 102, 0.25) !important;
        border-radius: 16px !important;
        padding: 18px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    .mindmap-node-card:hover {
        border-color: rgba(0, 255, 102, 0.7) !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.35) !important;
    }
    
    /* Glowing typography headers */
    .app-title {
        font-size: 22px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(0, 255, 102, 0.6) !important;
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 1px !important;
        margin-bottom: 2px !important;
    }
    
    .app-subtitle {
        font-size: 10px !important;
        color: #00FF66 !important; /* Matrix/Vibrant Green */
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 2px !important;
        margin-bottom: 24px !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
    }
    
    /* Scientific node headers */
    .node-title {
        font-size: 15px !important;
        font-weight: 800 !important;
        color: #00FF66 !important;
        font-family: monospace !important;
        margin-bottom: 8px !important;
    }

    /* Policy and Strength tags */
    .policy-label {
        font-size: 10px;
        font-weight: 700;
        background-color: rgba(78, 20, 111, 0.5); /* Purple tint */
        color: #E1BEE7; /* Light Purple text */
        padding: 3px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 6px;
        border: 1px solid rgba(78, 20, 111, 0.7);
        font-family: monospace;
    }
    
    .strength-tag {
        font-size: 10px;
        font-weight: 700;
        background-color: rgba(0, 255, 102, 0.08); /* Green tint */
        color: #00FF66; /* Vibrant Green text */
        padding: 3px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 6px;
        margin-right: 4px;
        border: 1px solid rgba(0, 255, 102, 0.3);
        font-family: monospace;
    }

    /* Popover button override */
    div.stPopover > button {
        background-color: rgba(0, 255, 102, 0.05) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        color: #00FF66 !important;
        border-radius: 8px !important;
        font-size: 10px !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 3px 10px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        margin-top: 8px !important;
    }
    div.stPopover > button:hover {
        background-color: rgba(0, 255, 102, 0.15) !important;
        border-color: #00FF66 !important;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.4) !important;
        color: #FFFFFF !important;
    }

    /* Popover content styles */
    .bubble-header {
        font-size: 13px;
        color: #00FF66;
        font-family: monospace;
        font-weight: bold;
        border-bottom: 1px solid rgba(0, 255, 102, 0.3);
        padding-bottom: 4px;
        margin-bottom: 8px;
    }

    .bubble-box {
        background: rgba(78, 20, 111, 0.3);
        padding: 8px;
        border-radius: 8px;
        border-left: 3px solid #9C27B0;
        font-size: 11px;
        color: #FFE082;
        margin-bottom: 8px;
    }

    /* Pipeline Step style */
    .pipeline-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        background: rgba(30, 8, 48, 0.6);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid rgba(78, 20, 111, 0.4);
    }
    .pipeline-step {
        font-size: 9px;
        font-family: monospace;
        text-align: center;
        flex: 1;
        padding: 4px;
        border-radius: 6px;
        color: #808080;
    }
    .pipeline-step.active {
        color: #00FF66;
        font-weight: bold;
        background: rgba(0, 255, 102, 0.08);
        border: 1px solid rgba(0, 255, 102, 0.2);
    }

    /* Bullet list items styling */
    .bullet-item {
        font-size: 12px !important;
        line-height: 1.4 !important;
        margin-bottom: 6px !important;
        color: #E0E0E0 !important;
    }

    .digital-divider {
        height: 1px;
        background: linear-gradient(to right, rgba(0, 255, 102, 0.4), rgba(78, 20, 111, 0.6), transparent);
        border: none;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# App Title & Subtitle Header
st.markdown('<div class="app-title">MINDMAP_QUICK_REF</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">CNS PSYCH_SERVICES APPRAISAL GUIDES</div>', unsafe_allow_html=True)

# Master Data Schema - strictly grounded in the "90-Day Psychological Services Appraisal Plan.docx"
mindmap_db = {
    "Phase I: Days 1–30": {
        "tag": "PHASE_1_DISCOVERY",
        "rationale": "Focuses on establish regulatory and clinical baseline benchmarks across Wayne, Oakland, and Macomb clinics. Under CCBHC Core Service #2, establishing these baseline standards is non-negotiable prior to systemic redesign.",
        "nodes": {
            "p1_n1": {
                "name": "LLP Supervision Logs Audit",
                "policy": "MCL 333.18223 & LARA Rule 338.2569",
                "target": "100% compliant LARA Form logs",
                "strengths": ["Learner", "Intellection", "Individualization"],
                "checklist": [
                    "Audit LLP and Temporary LLP active files for Form LARA/BPL Rev. 6/25 logs.",
                    "Verify each LLP receives a minimum of 4 hours/month of individual face-to-face LP supervision.",
                    "Ensure Fully Licensed Psychologists (LPs) co-sign LLP-written notes and assessments in the EHR.",
                    "Review completed supervisory forms for signatures, dates, and legal compliance before payroll release."
                ],
                "strengths_leverage": {
                    "theme": "Learner® + Intellection®",
                    "opportunity": "Transforms dry regulatory licensing logs into an active, intellectual assessment of clinical supervision quality.",
                    "example": "Meticulously study Michigan Public Health Code MCL 333.18223 rules. Set up a central digital HR portal that monitors supervisee logs and notifies LPs by the 25th of every month, removing administrative friction."
                }
            },
            "p1_n2": {
                "name": "30-Case Stratified Chart Audit",
                "policy": "CPT 96130 Interactive Feedback Guidelines",
                "target": "100% documented feedback in EHR charts",
                "strengths": ["Learner", "Strategic", "Intellection"],
                "checklist": [
                    "Verify that CPT code 96130 evaluations contain documented clinical integration & decision-making.",
                    "Check for explicit documentation of an interactive feedback session delivered face-to-face with client/caregiver.",
                    "Review billing times to ensure CPT 96130 represents at least 31 minutes of professional provider time.",
                    "Confirm technician-administered testing (96138) is strictly segregated from provider-administered testing (96136)."
                ],
                "strengths_leverage": {
                    "theme": "Learner® + Strategic®",
                    "opportunity": "Allows identifying systemic claims vulnerabilities before they result in insurance recoupments.",
                    "example": "Manually extract and analyze a randomized, stratified sample of 30 clinical charts. Note where interactive feedback sessions are omitted, and deploy an EHR-embedded billing block that halts claim release until feedback documentation is completed."
                }
            },
            "p1_n3": {
                "name": "Intake & Referral Triage Shadowing",
                "policy": "SAMHSA CCBHC Access Criteria (2023)",
                "target": "Map 100% of referral pipeline lifecycle",
                "strengths": ["Strategic", "Ideation"],
                "checklist": [
                    "Shadow intake coordinators and triage specialists to map the diagnostic referral lifecycle.",
                    "Track staff interactions with Prepaid Inpatient Health Plan (PIHP) portals (such as DWIHN's MHWIN or CHAMPS).",
                    "Identify specific administrative delay points from the moment a referral is received to scheduling.",
                    "Examine triage protocols for high-acuity priority populations (SMI/SED transitioning from inpatient care)."
                ],
                "strengths_leverage": {
                    "theme": "Strategic® + Ideation®",
                    "opportunity": "Provides immediate, visual mapping of administrative handoff points and waitlist bottle-necks.",
                    "example": "Trace the path of testing referrals from clinical request to scheduled appointment. Spot where portal delays occur and brainstorm a simplified EHR referral queue to bypass redundant approval loops."
                }
            },
            "p1_n4": {
                "name": "Stakeholder Readability Survey",
                "policy": "CARF Report Utility Standards",
                "target": ">80% response rate from top 20 clinicians",
                "strengths": ["Individualization", "Learner"],
                "checklist": [
                    "Design and distribute clinical utility surveys to internal psychiatric prescribers and outpatient therapists.",
                    "Conduct structured qualitative interviews with external regional community mental health stakeholders.",
                    "Assess whether completed psychological evaluation recommendations are actively integrated into the Person-Centered Plan.",
                    "Analyze report turnaround times and language complexity to identify gaps in report readability."
                ],
                "strengths_leverage": {
                    "theme": "Individualization® + Learner®",
                    "opportunity": "Identifies the custom informational needs of referring clinicians, ensuring reports are readable and therapeutically valuable.",
                    "example": "Analyze feedback from therapists and psychiatrists. Standardize report structures to include a clear, jargon-free summary section containing actionable interdisciplinary recommendations."
                }
            }
        }
    },
    "Phase II: Days 31–60": {
        "tag": "PHASE_2_OPERATIONAL_ANALYSIS",
        "rationale": "Transition from discovery to detailed, data-driven audits. This phase mathematically quantifies billing denial patterns, coding modifiers, prior authorizations, turnaround times, and material cost allocations.",
        "nodes": {
            "p2_n1": {
                "name": "RCM Claims Denial Audit",
                "policy": "RCM 835 Remittance Guidelines",
                "target": "Identify top 3 testing denial codes",
                "strengths": ["Strategic", "Learner"],
                "checklist": [
                    "Collaborate with the revenue cycle team to extract a 12-month historical claims database for CPT 96130–96139.",
                    "Isolate and analyze recurring billing denial codes, specifically checking for CO-97 and CO-50 rejections.",
                    "Evaluate automated clearinghouse billing rules to identify technical errors causing claims blockages.",
                    "Quantify the total financial leakage and administrative appeal burden associated with denied testing claims."
                ],
                "strengths_leverage": {
                    "theme": "Strategic® + Learner®",
                    "opportunity": "Pinpoints the root causes of insurance claims denials, locking down clinical revenue.",
                    "example": "Audit the 12-month remittance history to trace where testing evaluations are triggering bundled billing edits. Build an active list of top 3 denial reason codes to target with clinical-billing staff training."
                }
            },
            "p2_n2": {
                "name": "Modifier 59 / XE Compliance Audit",
                "policy": "CMS National Correct Coding Initiative (NCCI)",
                "target": "100% same-day billing compliance",
                "strengths": ["Strategic", "Intellection"],
                "checklist": [
                    "Audit same-day dual-provider testing sessions to verify correct modifier application.",
                    "Check if Modifier XE (separate encounter) or Modifier 59 is applied when psychologists and techs bill on the same date.",
                    "Verify that provider-administered CPT codes (96136) are strictly segregated from tech codes (96138).",
                    "Develop standardized billing rules for same-day provider/technician testing administrations."
                ],
                "strengths_leverage": {
                    "theme": "Strategic® + Intellection®",
                    "opportunity": "Prevents automated CMS claims rejections and post-payment Fraud, Waste, and Abuse compliance audits.",
                    "example": "Inspect billing records for same-day psychologist and tech administration. Hardcode automated billing rules in the EHR to automatically append Modifier XE when dual-billing parameters are detected."
                }
            },
            "p2_n3": {
                "name": "Telehealth Modifier Audit",
                "policy": "MDHHS Telehealth Billing Rules",
                "target": "100% compliant virtual feedback coding",
                "strengths": ["Learner", "Ideation"],
                "checklist": [
                    "Audit virtual CPT 96130 clinical feedback sessions for modifier accuracy.",
                    "Verify the correct placement of telehealth Modifiers (95 or GT) on remote feedback claims.",
                    "Check that Place of Service (POS) codes 02 (telehealth home) or 10 are aligned with client location.",
                    "Develop an EHR-integrated automation template for telehealth testing services."
                ],
                "strengths_leverage": {
                    "theme": "Learner® + Ideation®",
                    "opportunity": "Unlocks clean claim rates for virtual clinical feedback, bypassing travel barriers for consumers.",
                    "example": "Analyze remote feedback documentation. Configure the EHR telehealth module to auto-generate and append Modifier 95 and POS 10 whenever a virtual link is initiated."
                }
            },
            "p2_n4": {
                "name": "PA Threshold Tracking",
                "policy": "Medicaid Prior Authorization Guidelines",
                "target": "Centralize PA tracking systems",
                "strengths": ["Strategic", "Learner"],
                "checklist": [
                    "Map prior authorization rules across regional Prepaid Inpatient Health Plans and Medicaid Managed Care Plans.",
                    "Track Meridian's annual 8-hour testing calendar threshold before a PA is strictly required.",
                    "Verify DWIHN's requirements for immediate, bundled authorization using specialty billing codes.",
                    "Design EHR-embedded alerts to notify clinicians before they exceed tracking limits."
                ],
                "strengths_leverage": {
                    "theme": "Learner® + Strategic®",
                    "opportunity": "Eliminates payment forfeitures caused by conducting unauthorized testing hours.",
                    "example": "Study the PA rules for regional payers. Program a scheduling block in the EHR that prevents booking testing slots exceeding 8 hours annually without an active, attached authorization number."
                }
            },
            "p2_n5": {
                "name": "Report Turnaround Time (TAT) Metrics",
                "policy": "CARF Access & Timeliness Guidelines",
                "target": "Establish median write-time metrics",
                "strengths": ["Individualization", "Strategic"],
                "checklist": [
                    "Extract EHR timestamp data to measure median days from final testing date to signed report.",
                    "Segment the clinician testing pool to isolate individual writing and scoring bottlenecks.",
                    "Analyze TAT across three distinct intervals: referral-to-auth, auth-to-testing, and testing-to-signed-report.",
                    "Deliver personalized, performance-coaching sessions to outlying clinicians to accelerate delivery."
                ],
                "strengths_leverage": {
                    "theme": "Individualization® + Strategic®",
                    "opportunity": "Reduces delays in treatment entry by providing targeted, strengths-based clinician coaching.",
                    "example": "Segment report writing times into precise intervals. Identify specific clinicians struggling with write times and provide custom-tailored EHR dictation macros to speed up report completion."
                }
            },
            "p2_n6": {
                "name": "Financial Cost Allocation Analysis",
                "policy": "CCBHC PPS Cost Allocation Guidelines",
                "target": "Calculate cost-per-assessment ratio",
                "strengths": ["Intellection", "Strategic"],
                "checklist": [
                    "Review vendor invoices for consumable testing forms and scoring licenses (Pearson Q-interactive, PARiConnect, WPS).",
                    "Cross-reference total software and test kit expenditures against Medicaid Fee-For-Service and PPS revenues.",
                    "Analyze the cost-efficiency of digital testing versus traditional paper-and-pencil diagnostic protocols.",
                    "Quantify departmental overhead to align testing resource allocation with the daily CCBHC prospective payment rate."
                ],
                "strengths_leverage": {
                    "theme": "Intellection® + Strategic®",
                    "opportunity": "Minimizes material overhead and proves the ROI of transitioning the department to digital psychometrics.",
                    "example": "Calculate the average kit and scoring cost per evaluation. Present a cost-benefit analysis showing how migrating to Pearson Q-interactive digital scoring reduces paper costs and saves clinical hours."
                }
            }
        }
    },
    "Phase III: Days 61–90": {
        "tag": "PHASE_3_SYNTHESIS_ROADMAP",
        "rationale": "The final phase synthesizes clinical, financial, and regulatory findings into an actionable 12-month strategic roadmap, deploying permanent quality improvement dashboards and clinical pathways.",
        "nodes": {
            "p3_n1": {
                "name": "Stepped-Care Assessment Protocol",
                "policy": "SAMHSA CCBHC Core Service #2",
                "target": "Completed clinical triage algorithm",
                "strengths": ["Ideation", "Strategic"],
                "checklist": [
                    "Design a clinical triage pathway utilizing brief, rapid screenings (CPT 96127) at intake.",
                    "Establish a diagnostic algorithm to filter low-acuity cases away from intensive psychological testing.",
                    "Reserve multi-hour, highly expensive testing batteries exclusively for complex differential diagnoses (SMI/SED).",
                    "Ensure the new triage clinical algorithm meets SAMHSA CCBHC access and diagnostic criteria."
                ],
                "strengths_leverage": {
                    "theme": "Ideation® + Strategic®",
                    "opportunity": "Conceives an innovative, clinical-first filter that systematically eliminates testing waitlist backlogs.",
                    "example": "Design the Stepped-Care clinical protocol where clients receive rapid, targeted emotional assessments at intake. This triages simple diagnostic questions and reserves intensive batteries for complex differential cases, protecting clinician capacity."
                }
            },
            "p3_n2": {
                "name": "EHR KPI Dashboard",
                "policy": "CCBHC CQI Performance Monitoring",
                "target": "Track 5 core metrics on live dashboard",
                "strengths": ["Intellection", "Strategic", "Ideation"],
                "checklist": [
                    "Identify the 5 core operational and financial metrics needed for psychological service oversight.",
                    "Coordinate with the IT and EHR database departments to configure a real-time Business Intelligence dashboard.",
                    "Track weekly referral volumes, report turnaround times, claims denials, waitlist durations, and overhead costs.",
                    "Provide leadership and clinical supervisors with real-time visibility to prevent operational regressions."
                ],
                "strengths_leverage": {
                    "theme": "Intellection® + Strategic®",
                    "opportunity": "Builds high-fidelity, data-driven visual tracking systems to permanently protect the department from revenue leakage.",
                    "example": "Wireframe and deploy a live EHR BI dashboard. Set up automatic visual warnings that alert clinical leadership when report turnaround times approach critical thresholds or claims denials spike."
                }
            },
            "p3_n3": {
                "name": "Executive Appraisal Report",
                "policy": "MDHHS Demonstration Oversight Guidelines",
                "target": "Submit comprehensive report to executive board",
                "strengths": ["Intellection", "Learner"],
                "checklist": [
                    "Synthesize all Phase I chart audits, LARA logs, and triage shadowing findings into a cohesive report.",
                    "Integrate Phase II mathematical denial analyses, modifier error matrices, and cost overhead metrics.",
                    "Draft a formalized 'State of Psychological Testing' Executive Appraisal Report detailing compliance risks.",
                    "Secure clinical and financial leadership review and signatures before formal submission."
                ],
                "strengths_leverage": {
                    "theme": "Intellection® + Learner®",
                    "opportunity": "Compiles diverse, complex regulatory and clinical data points into an authoritative, defensible master report.",
                    "example": "Synthesize all baseline audits, claims data, and financial findings into a highly polished executive appraisal. This document proves compliance with MDHHS rules and justifies cost-based rate rebasing."
                }
            },
            "p3_n4": {
                "name": "12-Month Strategic Roadmap",
                "policy": "CCBHC Certification Program Requirement #6",
                "target": "Secure executive consensus on top 3 priorities",
                "strengths": ["Strategic", "Individualization", "Ideation"],
                "checklist": [
                    "Present the completed 12-month strategic roadmap to the CNS Healthcare executive board.",
                    "Outline necessary capital investments, including digital scoring platform interoperability.",
                    "Establish plans for centralizing LARA supervision logs and launching CPT modifier billing training.",
                    "Secure executive consensus and formal budget approvals for the top three operational priorities."
                ],
                "strengths_leverage": {
                    "theme": "Strategic® + Individualization®",
                    "opportunity": "Secures executive funding while maximizing clinician buy-in for long-term digital and billing transformations.",
                    "example": "Present the roadmap to the executive board. Highlight how capital investments in digital scoring platforms will lower material overhead, protect the agency from LARA audit risks, and decrease clinician burnout."
                }
            }
        }
    }
}

# Real-time search/filter feature for quick reference
search_query = st.text_input("🔍 Search Mindmap Nodes (e.g. LARA, CPT, Modifier, Triage):", "").strip().lower()

# Render Progress Bar across phases
col_act1, col_act2, col_act3 = st.columns(3)
with col_act1:
    p1_active = st.button("Phase I (Days 1–30)", use_container_width=True)
with col_act2:
    p2_active = st.button("Phase II (Days 31–60)", use_container_width=True)
with col_act3:
    p3_active = st.button("Phase III (Days 61–90)", use_container_width=True)

# Keep track of active tab in session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Phase I: Days 1–30"

if p1_active:
    st.session_state.active_tab = "Phase I: Days 1–30"
elif p2_active:
    st.session_state.active_tab = "Phase II: Days 31–60"
elif p3_active:
    st.session_state.active_tab = "Phase III: Days 61–90"

# Highlight active pipeline step
st.markdown('<div class="pipeline-container">', unsafe_allow_html=True)
p1_class = "active" if st.session_state.active_tab == "Phase I: Days 1–30" else ""
p2_class = "active" if st.session_state.active_tab == "Phase II: Days 31–60" else ""
p3_class = "active" if st.session_state.active_tab == "Phase III: Days 61–90" else ""
st.markdown(f'<div class="pipeline-step {p1_class}">PHASE_I: DISCOVERY</div>', unsafe_allow_html=True)
st.markdown(f'<div class="pipeline-step {p2_class}">PHASE_II: ANALYSIS</div>', unsafe_allow_html=True)
st.markdown(f'<div class="pipeline-step {p3_class}">PHASE_III: ROADMAP</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Display Node cards based on current active tab and search query
selected_phase = st.session_state.active_tab
phase_data = mindmap_db[selected_phase]

st.markdown(f"### 📡 **Active Phase: {selected_phase}**")

# Overarching Phase blueprint popover
with st.popover("🔬 CLICK FOR PHASE SYSTEM DIAGNOSTIC BLUEPRINT"):
    st.markdown(f'<div class="bubble-header">STRATEGIC APPRAISAL FOCUS</div>', unsafe_allow_html=True)
    st.write(phase_data["rationale"])

st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)

# Filter nodes based on search
nodes_found = False
for node_id, node_info in phase_data["nodes"].items():
    # Search filter logic
    search_text = f"{node_info['name']} {node_info['policy']} {' '.join(node_info['strengths'])} {' '.join(node_info['checklist'])}".lower()
    if search_query and search_query not in search_text:
        continue
        
    nodes_found = True
    st.markdown(f'<div class="mindmap-node-card">', unsafe_allow_html=True)
    
    # Header tag indicators
    st.markdown(f'<div class="policy-label">📜 {node_info["policy"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="target-label">🎯 Target: {node_info["target"]}</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="node-title">NODE_ID::{node_id.upper()} // {node_info["name"].upper()}</div>', unsafe_allow_html=True)
    
    # Review Items (Bulleted list)
    st.markdown("**Items to Review & Audit:**")
    for item in node_info["checklist"]:
        st.markdown(f'<div class="bullet-item">• {item}</div>', unsafe_allow_html=True)
        
    # Strengths tags list
    st.markdown("<p style='margin: 8px 0 2px 0; font-size:11px; font-weight:bold; color:#00FF66;'>APPLYING SCOTT\'S TOP STRENGTHS:</p>", unsafe_allow_html=True)
    for s in node_info["strengths"]:
        st.markdown(f'<span class="strength-tag">⚡ {s}</span>', unsafe_allow_html=True)
        
    # Popover for Strengths Leverage Example
    with st.popover(f"🧠 Leverage {node_info['strengths_leverage']['theme']} for this Task"):
        st.markdown(f'<div class="bubble-header">STRENGTHS-BASED LEADERSHIP DIRECTIVE</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bubble-box"><strong>Unique Opportunity:</strong> {node_info["strengths_leverage"]["opportunity"]}</div>', unsafe_allow_html=True)
        st.write(f"**How Scott Leverages this Strength:** {node_info['strengths_leverage']['example']}")
        
    st.markdown('</div>', unsafe_allow_html=True)

if not nodes_found:
    st.info("No matching nodes found for search term. Try another query (e.g. LARA, CPT, Modifier).")

# Sticky Scientific Footer
st.markdown("<hr style='margin-top: 30px; border-color: rgba(0, 255, 102, 0.2);'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:9px; color:#808080; text-align:center; padding-bottom:15px; font-family: monospace;">'
    'CNS Healthcare Appraisal Systems • Grounded strictly in "90-Day Psychological Services Appraisal Plan.docx"'
    '</div>',
    unsafe_allow_html=True
)
