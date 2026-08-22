import streamlit as st
import pandas as pd

# Set Page Config - Optimized for a widescreen PC Desktop experience
st.set_page_config(
    page_title="Executive Appraisal Dashboard | CNS Healthcare",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a professional, clean, light-themed Corporate Executive Dashboard
# Stripping out all dark purple/scientific-digital styling in favor of crisp white, royal blue, and emerald green.
st.markdown("""
<style>
    /* Light Mode Background & Layout */
    .stApp {
        background-color: #F8FAFC !important;
        color: #1E293B !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Clean, elevated white cards for metrics and tables */
    .dashboard-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
        margin-bottom: 20px !important;
        color: #1E293B !important;
    }
    
    /* Elegant Typography */
    .dashboard-title {
        font-size: 28px !important;
        font-weight: 800 !important;
        color: #1E3A8A !important; /* Royal Navy */
        margin-bottom: 4px !important;
        letter-spacing: -0.5px !important;
    }
    
    .dashboard-subtitle {
        font-size: 14px !important;
        color: #64748B !important; /* Slate Gray */
        margin-bottom: 24px !important;
        font-weight: 500 !important;
    }
    
    /* Soft color-coded badges for table/grid categories */
    .pillar-badge {
        font-size: 11px;
        font-weight: bold;
        padding: 3px 8px;
        border-radius: 6px;
        background-color: #EFF6FF;
        color: #1E40AF;
        border: 1px solid #BFDBFE;
    }
    
    /* Popover/Info Button Styles */
    div.stPopover > button {
        background-color: #FFFFFF !important;
        border: 1px solid #D1D5DB !important;
        color: #4B5563 !important;
        border-radius: 6px !important;
        font-size: 12px !important;
        padding: 4px 10px !important;
        transition: all 0.2s ease !important;
    }
    div.stPopover > button:hover {
        background-color: #F3F4F6 !important;
        border-color: #9CA3AF !important;
        color: #111827 !important;
    }
    
    /* Alert and Remediation Banners */
    .remedy-box {
        background-color: #FFFBEB !important; /* Warm light yellow */
        border-left: 4px solid #F59E0B !important;
        border: 1px solid #FDE68A !important;
        padding: 14px !important;
        border-radius: 8px !important;
        color: #78350F !important;
        font-size: 13px !important;
        margin-top: 10px !important;
    }
    
    /* Widescreen Columns Style Override */
    div[data-testid="column"] {
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header Block
st.markdown('<div class="dashboard-title">CNS Healthcare Clinical Operations</div>', unsafe_allow_html=True)
st.markdown('<div class="dashboard-subtitle">90-Day Psychological Services Appraisal Tracker • PC Corporate Edition</div>', unsafe_allow_html=True)

# ==============================================================================
# HIGH-PERFORMANCE DATA LOADING & CACHING
# Loading the complete 19-domain matrix directly from the source documents
# ==============================================================================
@st.cache_data
def get_static_appraisal_matrix():
    return [
        # Phase 1 Checklist (Days 1-30)
        {
            "Phase": "Phase 1: Discovery",
            "Task ID": "p1_t1",
            "Operational Pillar": "Staffing Compliance",
            "Audit Task": "Verify LLP Supervision Logs (Form LARA/BPL Rev. 6/25)",
            "Governing Policy": "Michigan Public Health Code MCL 333.18223 & LARA Rule 338.2569",
            "Target KPI": "100% compliant logs detailing 4 hrs/mo individual face-to-face supervision",
            "Systemic Rationale": "Unsigned or missing logs invalidate LLP clinical billing, exposing the agency to immediate licensing board penalties and retrospective Medicaid clawbacks.",
            "Remediation Directive": "Suspend unsupervised billing. Centralize supervision evaluation forms in HR, and hardcode EHR co-signature locks to prevent LLP claim release."
        },
        {
            "Phase": "Phase 1: Discovery",
            "Task ID": "p1_t2",
            "Operational Pillar": "Clinical Battery",
            "Audit Task": "Audit 30 Completed Testing Charts (CPT 96130 Interactive Feedback)",
            "Governing Policy": "AMA CPT 96130 Guidelines & Medicare Local Coverage Determinations (LCD)",
            "Target KPI": "100% presence of documented interactive feedback sessions in EHR",
            "Systemic Rationale": "Billing CPT 96130 (first-hour evaluation) without documenting the delivery of interactive feedback to the patient/caregiver is a direct compliance infraction.",
            "Remediation": "Halt and self-disclose missing feedback encounters. Deploy NextGen EHR templates that block note-locking until timestamped feedback narratives are complete."
        },
        {
            "Phase": "Phase 1: Discovery",
            "Task ID": "p1_t3",
            "Operational Pillar": "Referral Pipeline",
            "Audit Task": "Shadow Intake and Referral Triage Workflows",
            "Governing Policy": "SAMHSA CCBHC Access Criteria (2023) & MDHHS Demonstration Guidelines",
            "Target KPI": "Map 100% of pipeline lifecycle from initial referral to triage",
            "Systemic Rationale": "Extended testing waitlists bottleneck patient entry, triggering MDHHS Corrective Action Plans (CAPs) and jeopardizing federal CCBHC certification.",
            "Remediation": "Construct process maps of administrative handoffs, identify delays within PIHP portals (MHWIN/CHAMPS), and establish open-access triage blocks."
        },
        {
            "Phase": "Phase 1: Discovery",
            "Task ID": "p1_t4",
            "Operational Pillar": "Interdisciplinary Integration",
            "Audit Task": "Survey Internal & External Stakeholders (Report Utility)",
            "Governing Policy": "CARF ASPIRE Accreditation Standards & CCBHC Care Coordination",
            "Target KPI": ">80% response rate from top 20 referring clinicians and psychiatrists",
            "Systemic Rationale": "If diagnostic reports fail to directly influence the Person-Centered Plan (PCP), testing functions as an isolated, high-cost administrative exercise.",
            "Remediation": "Standardize all clinical report layouts to mandate a prominent, jargon-free summary block containing actionable interdisciplinary recommendations."
        },
        # Phase 2 Checklist (Days 31-60)
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t1",
            "Operational Pillar": "Financial Mechanics",
            "Audit Task": "Conduct 12-Month CPT 96130-96139 Claims Denial Audit",
            "Governing Policy": "RCM Clearinghouse 835 Remittance Guidelines",
            "Target KPI": "Extract and identify top 3 billing denial reason codes",
            "Systemic Rationale": "Unresolved automated clearinghouse denials cause massive compounding revenue leakage and impose an excessive administrative burden on staff.",
            "Remediation": "Collaborate with billing teams to extract historical 835 remittances, isolate code triggers (e.g., CO-97, CO-50), and adjust front-end edits."
        },
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t2",
            "Operational Pillar": "Financial Mechanics",
            "Audit Task": "Audit Modifier 59 / XE Compliance for Same-Day Services",
            "Governing Policy": "CMS National Correct Coding Initiative (NCCI) Modifier Edits",
            "Target KPI": "100% billing modifier accuracy for same-day provider/tech services",
            "Systemic Rationale": "Billing provider administration (96136) and tech administration (96138) on the same date triggers an automated CMS rejection unless modifiers are appended.",
            "Remediation": "Hardcode billing validation rules in the EHR to automatically append Modifier XE or 59 to dual-billing testing claims on the same date."
        },
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t3",
            "Operational Pillar": "Financial Mechanics",
            "Audit Task": "Audit Virtual Feedback Telehealth Modifiers",
            "Governing Policy": "MDHHS Telehealth Billing Rules & Commercial Payer Policies",
            "Target KPI": "100% compliant virtual feedback session coding (Modifier 95/GT)",
            "Systemic Rationale": "Missing virtual modifiers or incorrect Place of Service codes (POS 02/10) trigger automated claims denials, artificially suppressing realization rates.",
            "Remediation": "Configure the EHR telehealth video module to auto-generate and attach the correct virtual POS and 95 modifier when virtual sessions are hosted."
        },
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t4",
            "Operational Pillar": "Financial Mechanics",
            "Audit Task": "Map Differing PIHP/MCO Prior Authorization Thresholds",
            "Governing Policy": "Michigan Medicaid Provider Manual & Utilization Tracking",
            "Target KPI": "Establish centralized workflow for tracking PIHP/MCO PA limits",
            "Systemic Rationale": "Failing to secure prior authorization before testing exceeds annual limits (such as Meridian's 8-hour limit) results in total payment forfeiture.",
            "Remediation": "Embed a scheduling hard stop in the EHR that blocks appointments exceeding 8 hours annually unless an active PA number is recorded."
        },
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t5",
            "Operational Pillar": "Staffing Compliance",
            "Audit Task": "Measure Mean & Median Report Turnaround Times (TAT)",
            "Governing Policy": "CARF Quality Timeliness Guidelines & SAMHSA Benchmarks",
            "Target KPI": "Calculate median days from final testing date to signed report",
            "Systemic Rationale": "Extended report TATs delay psychiatric and therapeutic treatment entry, directly violating CCBHC care coordination standards.",
            "Remediation": "Segment EHR timestamp data (referral, testing, and sign-off dates) to isolate bottlenecks and counsel outlying clinicians."
        },
        {
            "Phase": "Phase 2: Optimization",
            "Task ID": "p2_t6",
            "Operational Pillar": "Clinical Battery",
            "Audit Task": "Conduct Financial Overhead Audit of Diagnostic Materials",
            "Governing Policy": "CCBHC PPS Cost Allocation Guidelines & Budget Mapping",
            "Target KPI": "Establish cost-per-assessment ratio (Vendor invoices vs. claim volume)",
            "Systemic Rationale": "Unmonitored diagnostic kit and digital scoring licensing expenses (Pearson, PAR, WPS) create unrecognized department deficits.",
            "Remediation": "Cross-reference all vendor invoices against Medicaid and PPS revenues to identify high-cost tools, shifting entirely to digital scoring to lower overhead."
        },
        # Phase 3 Checklist (Days 61-90)
        {
            "Phase": "Phase 3: Sustainability",
            "Task ID": "p3_t1",
            "Operational Pillar": "Referral Pipeline",
            "Audit Task": "Implement Stepped-Care Assessment Clinical Pathway",
            "Governing Policy": "SAMHSA CCBHC Core Service #2: Screening, Assessment, and Diagnosis",
            "Target KPI": "100% of low-acuity testing referrals triaged through new algorithm",
            "Systemic Rationale": "Conducting multi-day diagnostic testing for low-acuity referrals wastes psychologist capacity and inflates waitlists for high-acuity SMI/SED populations.",
            "Remediation": "Develop and approve the Stepped-Care clinical algorithm, establishing a brief screening triage (CPT 96127) at intake to preserve testing resources."
        },
        {
            "Phase": "Phase 3: Sustainability",
            "Task ID": "p3_t2",
            "Operational Pillar": "Interdisciplinary Integration",
            "Audit Task": "Configure EHR-Integrated Assessment KPI Dashboard",
            "Governing Policy": "CCBHC Continuous Quality Improvement (CQI) Performance Monitoring",
            "Target KPI": "Configure live dashboard tracking 5 core clinical-financial metrics",
            "Systemic Rationale": "A lack of ongoing, visual tracking tools leads to unrecognized bottlenecks and billing errors, resulting in compounding financial and operational regressions.",
            "Remediation": "Coordinate with IT to configure a live, EHR-integrated Business Intelligence dashboard tracking referral volume, report TAT, denials, and waitlists."
        },
        {
            "Phase": "Phase 3: Sustainability",
            "Task ID": "p3_t3",
            "Operational Pillar": "Interdisciplinary Integration",
            "Audit Task": "Package 'State of Psychological Testing' Executive Appraisal",
            "Governing Policy": "MDHHS Demonstration Guidelines & SAMHSA Certification Criteria",
            "Target KPI": "Formal report submission and presentation to the Executive Board",
            "Systemic Rationale": "Omission of documented appraisal findings violates state certification rules and limits the agency's ability to justify cost-based rate rebasing.",
            "Remediation": "Synthesize all Phase I and II findings into the formalized executive report, securing final signatures from clinical and financial leadership."
        },
        {
            "Phase": "Phase 3: Sustainability",
            "Task ID": "p3_t4",
            "Operational Pillar": "Interdisciplinary Integration",
            "Audit Task": "Secure Approval for 12-Month Strategic Optimization Roadmap",
            "Governing Policy": "CCBHC Certification Program Requirement #6: Strategic Planning",
            "Target KPI": "Executive board consensus and approved capital budget allocation",
            "Systemic Rationale": "Failure to plan for long-term capital investments results in operational stagnation, persistent clinician burnout, and ongoing financial leakage.",
            "Remediation": "Present the 12-month roadmap to the executive board to secure budget allocation and strategic alignment for top priorities."
        }
    ]

# Load static database
static_data = get_static_appraisal_matrix()

# ==============================================================================
# DESKTOP SESSION STATE INITIALIZATION
# ==============================================================================
if "desktop_audit_states" not in st.session_state:
    st.session_state.desktop_audit_states = {}
    for item in static_data:
        st.session_state.desktop_audit_states[item["Task ID"]] = {
            "Status": "Pending",
            "Notes": ""
        }

# ==============================================================================
# SIDEBAR METRICS COMMAND PANEL
# ==============================================================================
with st.sidebar:
    st.markdown("### **Clinical Command Console**")
    st.write("Desktop monitoring tool for Dr. Scott Niewinski's 90-day transition at CNS Healthcare.")
    
    # Calculate Live Stats based on Session State
    total_items = len(static_data)
    compliant_count = sum(1 for k, v in st.session_state.desktop_audit_states.items() if v["Status"] == "Compliant")
    non_compliant_count = sum(1 for k, v in st.session_state.desktop_audit_states.items() if v["Status"] == "Outside of Compliance")
    pending_count = total_items - compliant_count - non_compliant_count
    
    comp_rate = (compliant_count / total_items) * 100 if total_items > 0 else 0
    
    # Custom light-mode metric cards in sidebar
    st.metric("Overall Compliance Rate", f"{comp_rate:.1f}%", f"{compliant_count}/{total_items} Passed")
    st.metric("Outstanding Compliance Gaps", f"{non_compliant_count}", delta="- Action Needed" if non_compliant_count > 0 else "System Stable", delta_color="inverse")
    st.metric("Pending Audits", f"{pending_count}")
    
    st.progress(compliant_count / total_items)
    
    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown("**Core Regulatory Source Policies:**")
    st.write("• LARA MCL 333.18223")
    st.write("• MDHHS APF 167 Guidelines")
    st.write("• SAMHSA CCBHC Demonstration")
    st.write("• CMS NCCI billing guidelines")

# ==============================================================================
# THE MAIN DESKTOP AUDIT DECK: EXECUTED VIA SPREADSHEET-STYLE INTERACTION
# ==============================================================================
tab_grid, tab_report = st.tabs(["📊 Interactive Audit Spreadsheet", "📋 Executive Memorandum Report"])

# ================= TAB 1: SPREADSHEET INTERFACE =================
with tab_grid:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("### **Widescreen Audit Grid**")
    st.write("To make tracking everything easily achievable on your PC, you can edit and manage the appraisal checklists in this single, centralized spreadsheet. Filter by Phase or Pillar, change the status directly, and review detailed policies.")
    
    # Phase & Pillar Filters side-by-side
    col_f1, col_f2, col_f3 = st.columns([1, 1, 2])
    with col_f1:
        phase_filter = st.selectbox("Filter by Appraisal Phase:", ["All Phases", "Phase 1: Discovery", "Phase 2: Optimization", "Phase 3: Sustainability"])
    with col_f2:
        pillar_filter = st.selectbox("Filter by Operational Pillar:", ["All Pillars", "Staffing Compliance", "Clinical Battery", "Referral Pipeline", "Financial Mechanics", "Interdisciplinary Integration"])
    with col_f3:
        search_query = st.text_input("🔍 Quick-Search Tasks:", placeholder="Type CPT, LARA, feedback, or any keyword...")

    # Filter Data based on selections
    filtered_data = []
    for item in static_data:
        # Phase Filter
        if phase_filter != "All Phases" and item["Phase"] != phase_filter:
            continue
        # Pillar Filter
        if pillar_filter != "All Pillars" and item["Operational Pillar"] != pillar_filter:
            continue
        # Search Filter
        if search_query:
            q = search_query.lower()
            if q not in item["Audit Task"].lower() and q not in item["Governing Policy"].lower() and q not in item["Operational Pillar"].lower():
                continue
        filtered_data.append(item)

    # Render Task Checklist Nodes
    if not filtered_data:
        st.info("No audit items match your current filter settings. Adjust filters or search queries above.")
    else:
        for idx, item in enumerate(filtered_data):
            tid = item["Task ID"]
            st.markdown(f'<div class="dashboard-card">', unsafe_allow_html=True)
            
            # Left Half (Data Details) & Right Half (Interactions)
            col_details, col_control = st.columns([3, 2])
            
            with col_details:
                st.markdown(f'<span class="pillar-badge">{item["Operational Pillar"]}</span> <span style="font-size:11px; color:#4B5563; margin-left:8px; font-weight:600;">{item["Phase"]}</span>', unsafe_allow_html=True)
                st.markdown(f"#### **{item['Audit Task']}**")
                st.markdown(f"**Governing Policy:** *{item['Governing Policy']}*")
                st.markdown(f"**Target Metric:** {item['Target KPI']}")
                
            with col_control:
                # Dynamic popover/bubble window for detailed description and appraisal rationale
                col_pop, col_stat = st.columns([1, 2])
                with col_pop:
                    with st.popover("🔬 Details"):
                        st.markdown('<div class="popover-header">SYSTEMIC DIAGNOSTICS</div>', unsafe_allow_html=True)
                        st.markdown(f"**Operational Task Description:** {item.get('desc_long', item['Audit Task'])}")
                        st.markdown(f"**Appraisal Rationale:** {item['Systemic Rationale']}")
                with col_stat:
                    # Retrieve and select state
                    state_val = st.session_state.desktop_audit_states[tid]["Status"]
                    opts = ["Pending", "Compliant", "Outside of Compliance"]
                    selected_opt = st.selectbox(
                        f"Compliance Status for {tid}",
                        opts,
                        index=opts.index(state_val),
                        key=f"status_select_{tid}",
                        label_visibility="collapsed"
                    )
                    st.session_state.desktop_audit_states[tid]["Status"] = selected_opt
                
                # Render text note box for PC-based tracking Notes
                notes_val = st.text_input(
                    "Clinical Audit Notes / Findings:",
                    value=st.session_state.desktop_audit_states[tid]["Notes"],
                    key=f"notes_input_{tid}",
                    placeholder="Enter audit timestamps, findings, or staff logs..."
                )
                st.session_state.desktop_audit_states[tid]["Notes"] = notes_val
                
                # Context-Specific Remediation block
                if selected_opt == "Outside of Compliance":
                    rem_text = item.get("Remediation Directive", item.get("remediation", item.get("Remediation", "No remediation listed.")))
                    st.markdown(
                        f'<div class="remedy-box">'
                        f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {rem_text}'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                    
            st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 2: EXECUTIVE REPORT VIEW =================
with tab_report:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    
    # Executive Styled Memorandum Header
    st.markdown("""
    <div style="border: 2px solid #1E3A8A; padding: 20px; border-radius: 12px; background-color: #EFF6FF; margin-bottom: 24px;">
        <h3 style="color: #1E3A8A; margin: 0; font-weight: 800; font-size:18px;">CNS HEALTHCARE | CLINICAL OPERATIONS PORTAL</h3>
        <h4 style="color: #10B981; margin: 4px 0 0 0; font-weight: 700; font-size:14px;">90-DAY PSYCHOLOGICAL SERVICES APPRAISAL STATUS MEMORANDUM</h4>
        <p style="color: #64748B; font-size: 11px; margin: 8px 0 0 0; line-height: 1.4;">
            <strong>TO:</strong> Provider Supervisors & Executive Leadership Board<br>
            <strong>FROM:</strong> Dr. Scott Niewinski, Psy.D., Manager of Psychological Services<br>
            <strong>DATE:</strong> August 20, 2026<br>
            <strong>SUBJECT:</strong> Comprehensive Compliance, Clinical, and Billing Audit Progress Report
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Process session states for reporting
    comp_list = []
    gap_list = []
    pend_list = []
    
    for item in static_data:
        tid = item["Task ID"]
        status = st.session_state.desktop_audit_states[tid]["Status"]
        notes = st.session_state.desktop_audit_states[tid]["Notes"]
        report_entry = {"item": item, "notes": notes}
        
        if status == "Compliant":
            comp_list.append(report_entry)
        elif status == "Outside of Compliance":
            gap_list.append(report_entry)
        else:
            pend_list.append(report_entry)
            
    total_audited = len(static_data)
    
    # Scorecards inside report
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("VERIFIED COMPLIANT", f"{len(comp_list)}/{total_audited}", f"{comp_rate:.1f}% Rate")
    with c2:
        st.metric("CRITICAL COMPLIANCE GAPS", f"{len(gap_list)}", delta="- Immediate Action Required" if gap_list else "Stable", delta_color="inverse")
    with c3:
        st.metric("PENDING BASELINES", f"{len(pend_list)}")
        
    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    
    # Split report into two balanced columns
    rep_col1, rep_col2 = st.columns(2)
    
    # Column 1: Compliant Systems
    with rep_col1:
        st.markdown("### 🟢 **Verified Strengths & Compliant Areas**")
        st.write("The following service domains are meeting LARA, MDHHS, and CARF guidelines. No corrective action is required.")
        
        if not comp_list:
            st.info("No service domains have been marked as 'Compliant' yet in the audit spreadsheet.")
        else:
            for entry in comp_list:
                it = entry["item"]
                st.markdown(f"<strong style='color:#1E3A8A;'>✓ {it['Audit Task']}</strong>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:11px; color:#475569;'>Pillar: {it['Operational Pillar']} | Policy: {it['Governing Policy']}</span>", unsafe_allow_html=True)
                if entry["notes"]:
                    st.markdown(f"<p style='font-size:12px; font-style:italic; background:#F1F5F9; padding:6px; border-radius:4px; margin:4px 0 10px 0;'><strong>Audit Finding:</strong> {entry['notes']}</p>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 8px 0; border: none; border-bottom: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    # Column 2: Active Gaps & Remediation Matrix
    with rep_col2:
        st.markdown("### 🔴 **Critical Gaps & Active Risk Remediation Matrix**")
        st.write("The following service domains represent active regulatory, financial, or licensing liabilities demanding immediate intervention.")
        
        if not gap_list:
            st.success("🎉 Excellent! Zero compliance gaps have been flagged. All verified areas are meeting state and federal standards.")
        else:
            for entry in gap_list:
                it = entry["item"]
                st.markdown(f"<div style='border: 1px solid #FCA5A5; border-radius: 8px; padding: 12px; background-color: #FEF2F2; margin-bottom: 12px;'>", unsafe_allow_html=True)
                st.markdown(f"<strong style='color:#DC2626;'>🚨 [GAP] {it['Audit Task']}</strong>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin: 4px 0; font-size:12px; color:#475569;'><strong>Governing Directive:</strong> {it['Governing Policy']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin: 4px 0; font-size:12px; color:#1E3A8A;'><strong>Target Metric:</strong> {it['Target KPI']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin: 4px 0; font-size:12px; color:#991B1B;'><strong>Vulnerability:</strong> {it['Systemic Rationale']}</p>", unsafe_allow_html=True)
                
                if entry["notes"]:
                    st.markdown(f"<p style='font-size:12px; font-style:italic; background:#FFFFFF; padding:6px; border-radius:4px; border:1px solid #FCA5A5; margin:6px 0;'><strong>Observer Log:</strong> {entry['notes']}</p>", unsafe_allow_html=True)
                
                rem_text = it.get("Remediation Directive", it.get("remediation", it.get("Remediation", "No remediation listed.")))
                st.markdown(
                    f'<div class="remedy-box" style="margin-top:6px;">'
                    f'🛠️ <strong>REMEDIATION DIRECTIVE:</strong> {rem_text}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)
                
    st.markdown('</div>', unsafe_allow_html=True)

# CliftonStrengths Strategic Overlay at the very bottom
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.markdown("### **🧠 CliftonStrengths Strategic Leadership Blueprint**")
st.write("As the Program Manager, Dr. Scott Niewinski can strategically apply his top five talents to drive these tasks through three distinct phases:")

st1, st2, st3 = st.columns(3)
with st1:
    st.markdown("#### **Phase 1: Discovery**")
    st.write("**Deploy: Learner® & Intellection®**")
    st.write("Meticulously study licensing statutes like **MCL 333.18223** and **LARA Rule 338.2569** to establish baseline audit logs, using Intellection to identify root causes of testing delays.")
with st2:
    st.markdown("#### **Phase 2: Optimization**")
    st.write("**Deploy: Ideation® & Individualization®**")
    st.write("Brainstorm and build custom macros in **Dragon Medical One** and standardize templates in **NextGen**; customize clinical documentation coaching based on unique clinician styles.")
with st3:
    st.markdown("#### **Phase 3: Sustainability**")
    st.write("**Deploy: Strategic®**")
    st.write("Synthesize data from manual chart audits, billing denials, and overhead costs into a 12-month business-case roadmap to secure board-level approvals.")

st.markdown('</div>', unsafe_allow_html=True)

# Sticky Footer
st.markdown("<hr style='margin-top: 30px; border-color: #E2E8F0;'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:11px; color:#64748B; text-align:center; padding-bottom:15px; font-weight:500;">'
    'CNS Healthcare Appraisal Systems • Grounded strictly in "90-Day Psychological Services Appraisal Plan.docx"</div>',
    unsafe_allow_html=True
)
