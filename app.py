import streamlit as st

# ==============================================================================
# STREAMLIT PAGE CONFIGURATION
# PC and desktop widescreen optimized, no OS dependencies, crash-resistant
# ==============================================================================
st.set_page_config(
    page_title="Michigan CCBHC 90-Day Psychological Services Appraisal Portal",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom top-level CSS for background matching the dark purple, digital scientific aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #0c051a !important;
        background: radial-gradient(circle at center, #120822 0%, #080311 100%) !important;
        color: #FFFFFF !important;
    }
    iframe {
        border: none !important;
        border-radius: 12px;
        box-shadow: 0 4px 30px rgba(0, 255, 102, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading using modern st.cache_data
@st.cache_data
def get_historical_claims_metrics():
    """
    Simulates loading of a massive historical database query for 12 months
    of psychological services billing data (1,420 unique claims).
    """
    return {
        "total_claims": 1420,
        "ncci_modifier_denials": 64,
        "telehealth_modifier_failures": 42,
        "exceeded_pa_caps": 31,
        "undocumented_interactive_feedback": 24,
        "average_tat_days": 24.5,
        "top_denial_codes": ["CO-97 (Bundled)", "CO-50 (Medically Unnecessary)", "CO-16 (Claim Lack Info)"],
        "unsupervised_llp_risk_hours": 160
    }

# Cache resource mapping using modern st.cache_resource
@st.cache_resource
def get_regulatory_frameworks():
    """
    Caches the rigid regulatory and policy mappings to stabilize performance
    and prevent circular re-runs on user interaction.
    """
    return {
        "MCL_333_18223": "Michigan Public Health Code governing Limited License Psychologists (LLPs)",
        "LARA_RULE_338_2569": "Michigan Board of Psychology administrative rule for supervisory evaluations",
        "MDHHS_APF_167": "Michigan Department of Health & Human Services guidelines for Restrictive Behavior Plans",
        "SAMHSA_CCBHC_CORE_2": "CCBHC screening, assessment, and diagnostic access standards",
        "CMS_NCCI_EDITS": "Centers for Medicare & Medicaid Services National Correct Coding Initiative modifiers"
    }

# Execute caching
claims_data = get_historical_claims_metrics()
frameworks = get_regulatory_frameworks()

# ==============================================================================
# GENERATE THE EMBEDDED HIGH-FIDELITY SPA PORTAL (HTML5 / Tailwind / Chart.js / Plotly.js)
# ==============================================================================
# We build an incredibly immersive single-page web app with interactive charts,
# chronological step-wise workflow tracker, live search, dynamic filtering,
# risk matrices, and a compiled executive report.
# ==============================================================================

html_spa_content = """
<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <title>Michigan CCBHC 90-Day Psychological Services Appraisal Portal</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Plotly.js CDN -->
    <script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brandPurple: '#4A154B',
                        darkPurple: '#120822',
                        glowGreen: '#22c55e',
                        lightGlowGreen: '#4ade80'
                    }
                }
            }
        }
    </script>
    <style>
        /* Glowing neon glass styles */
        .neon-border {
            box-shadow: 0 0 15px rgba(34, 197, 94, 0.2);
            border: 1px solid rgba(34, 197, 94, 0.3);
        }
        .neon-border:hover {
            box-shadow: 0 0 25px rgba(34, 197, 94, 0.4);
            border-color: rgba(34, 197, 94, 0.6);
        }
        /* Hide scrollbar for clean dashboard appearance */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #120822;
        }
        ::-webkit-scrollbar-thumb {
            background: #4A154B;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #22c55e;
        }
    </style>
</head>
<body class="bg-darkPurple text-white h-full overflow-y-auto antialiased">

    <!-- HEADER BLOCK -->
    <header class="border-b border-brandPurple bg-black/40 backdrop-blur px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-lg bg-glowGreen flex items-center justify-center font-bold text-darkPurple shadow-lg shadow-glowGreen/30 text-lg">🧬</div>
            <div>
                <h1 class="text-xl font-bold tracking-wider uppercase font-mono">SYS_DIAGNOSTIC_SPA_PORTAL</h1>
                <p class="text-xs text-glowGreen font-mono uppercase tracking-widest">CNS Healthcare • Michigan CCBHC 90-Day Psychological Services Appraisal</p>
            </div>
        </div>
        <div class="flex items-center gap-4 text-xs font-mono">
            <div class="px-3 py-1.5 rounded bg-brandPurple/30 border border-brandPurple text-purple-300">
                AUDITOR: DR. SCOTT NIEWINSKI, PSY.D.
            </div>
            <div class="px-3 py-1.5 rounded bg-glowGreen/10 border border-glowGreen/30 text-glowGreen animate-pulse">
                STATUS: LIVE COMPLIANCE CHECK DECK
            </div>
        </div>
    </header>

    <!-- MAIN GRID CONTAINER -->
    <main class="p-6 space-y-6">

        <!-- EXECUTIVE SCORECARDS -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="bg-black/40 p-4 rounded-xl border border-brandPurple/60 hover:border-glowGreen/50 transition duration-300">
                <span class="text-xs text-purple-300 font-mono tracking-wider block">COMPLIANCE RATING</span>
                <div class="flex items-baseline gap-2 mt-1">
                    <span id="metric-compliance-pct" class="text-3xl font-extrabold text-glowGreen">73.7%</span>
                    <span class="text-xs text-slate-400">Target: 100%</span>
                </div>
                <div class="w-full bg-slate-800 rounded-full h-1.5 mt-3">
                    <div id="metric-compliance-bar" class="bg-glowGreen h-1.5 rounded-full" style="width: 73.7%"></div>
                </div>
            </div>
            <div class="bg-black/40 p-4 rounded-xl border border-brandPurple/60 hover:border-glowGreen/50 transition duration-300">
                <span class="text-xs text-purple-300 font-mono tracking-wider block">ACTIVE AUDIT OBJECTIVES</span>
                <div class="flex items-baseline gap-2 mt-1">
                    <span id="metric-total-tasks" class="text-3xl font-extrabold text-white">19</span>
                    <span class="text-xs text-slate-400">Total Domains</span>
                </div>
                <p class="text-[10px] text-slate-400 mt-2 font-mono">MAP TO 5 OPERATIONAL PILLARS</p>
            </div>
            <div class="bg-black/40 p-4 rounded-xl border border-brandPurple/60 hover:border-glowGreen/50 transition duration-300">
                <span class="text-xs text-purple-300 font-mono tracking-wider block">IDENTIFIED COMPLIANCE GAPS</span>
                <div class="flex items-baseline gap-2 mt-1">
                    <span id="metric-gap-count" class="text-3xl font-extrabold text-rose-500">5</span>
                    <span class="text-xs text-rose-400 font-bold">Mitigation Needed</span>
                </div>
                <p class="text-[10px] text-rose-300 mt-2 font-mono">CRITICAL FINANCIAL/LICENSURE RISKS</p>
            </div>
            <div class="bg-black/40 p-4 rounded-xl border border-brandPurple/60 hover:border-glowGreen/50 transition duration-300">
                <span class="text-xs text-purple-300 font-mono tracking-wider block">PROJECTED REIMBURSEMENT REALIZATION</span>
                <div class="flex items-baseline gap-2 mt-1">
                    <span id="metric-revenue-realization" class="text-3xl font-extrabold text-glowGreen">88.2%</span>
                    <span class="text-xs text-slate-400">Fee-For-Service / PPS</span>
                </div>
                <p class="text-[10px] text-slate-400 mt-2 font-mono">POTENTIAL LOSS WITH PENDING COMPLIANCE</p>
            </div>
        </section>

        <!-- DYNAMIC DASHBOARD SELECTOR & RISK MATRIX FILTER -->
        <section class="bg-black/30 p-4 rounded-xl border border-brandPurple flex flex-wrap gap-4 items-center justify-between">
            <div class="flex flex-wrap gap-2">
                <button onclick="filterPhase('all')" class="phase-btn px-4 py-1.5 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition border border-glowGreen bg-glowGreen text-darkPurple" id="btn-phase-all">ALL PHASES</button>
                <button onclick="filterPhase('Phase 1')" class="phase-btn px-4 py-1.5 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition border border-brandPurple bg-brandPurple/20 text-purple-200" id="btn-phase-p1">PHASE 1: DISCOVERY (DAYS 1-30)</button>
                <button onclick="filterPhase('Phase 2')" class="phase-btn px-4 py-1.5 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition border border-brandPurple bg-brandPurple/20 text-purple-200" id="btn-phase-p2">PHASE 2: OPTIMIZATION (DAYS 31-60)</button>
                <button onclick="filterPhase('Phase 3')" class="phase-btn px-4 py-1.5 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition border border-brandPurple bg-brandPurple/20 text-purple-200" id="btn-phase-p3">PHASE 3: SUSTAINABILITY (DAYS 61-90)</button>
                <button onclick="filterPhase('Report')" class="phase-btn px-4 py-1.5 rounded-lg text-xs font-mono font-bold tracking-wider uppercase transition border border-brandPurple bg-brandPurple/20 text-purple-200" id="btn-phase-report">📝 PROGRESS & EXECUTIVE REPORT</button>
            </div>
            <div class="flex items-center gap-3">
                <span class="text-xs text-purple-300 font-mono uppercase tracking-wider">Risk Matrix Filter:</span>
                <select id="risk-filter" onchange="filterRiskTable()" class="bg-darkPurple border border-brandPurple text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-glowGreen font-mono">
                    <option value="all">SHOW ALL CATEGORIES</option>
                    <option value="Licensure & LARA">LICENSURE & LARA COMPLIANCE</option>
                    <option value="Revenue Cycle (NCCI)">REVENUE CYCLE (NCCI EDITS)</option>
                    <option value="Utilization Management">UTILIZATION MANAGEMENT</option>
                    <option value="CCBHC Compliance">CCBHC ACCESS & TIMELINES</option>
                    <option value="Coding Specificity">CODING SPECIFICITY (CPT 96130)</option>
                    <option value="Telehealth Regulations">TELEHEALTH REGULATIONS</option>
                </select>
            </div>
        </section>

        <!-- MAIN LAYOUT: SPLIT VIEW FOR PC -->
        <section class="grid grid-cols-1 lg:grid-cols-12 gap-6" id="dashboard-main-view">
            
            <!-- LEFT AREA: VISUAL CHART & STRENGTHS (4 COLS) -->
            <div class="lg:col-span-4 space-y-6">
                <!-- CHART 1: CPT DENIAL DRIVERS (PLOTLY DONUT) -->
                <div class="bg-black/40 p-4 rounded-xl border border-brandPurple neon-border">
                    <h3 class="text-sm font-bold text-purple-200 tracking-wider font-mono border-b border-brandPurple pb-2 mb-3">🚨 REVENUE LEAKAGE: CPT DENIAL DRIVERS</h3>
                    <div id="plotly-donut-denials" style="height: 250px;"></div>
                </div>

                <!-- CHART 2: CLINIC STATUS & TAT OVERVIEW (CHART.JS GROUPED) -->
                <div class="bg-black/40 p-4 rounded-xl border border-brandPurple neon-border">
                    <h3 class="text-sm font-bold text-purple-200 tracking-wider font-mono border-b border-brandPurple pb-2 mb-3">📊 OPERATIONS: REPORT TAT BY CLINIC</h3>
                    <div class="h-[220px]">
                        <canvas id="chartjs-clinic-tat"></canvas>
                    </div>
                </div>

                <!-- CLIFTONSTRENGTHS TEAM INTEGRATION BOARD -->
                <div class="bg-black/40 p-4 rounded-xl border border-brandPurple">
                    <h3 class="text-sm font-bold text-purple-200 tracking-wider font-mono border-b border-brandPurple pb-2 mb-3">🧠 SCOTT'S CLIFTONSTRENGTHS BLUEPRINT</h3>
                    <div class="space-y-3 mt-3">
                        <div class="p-2.5 rounded bg-brandPurple/10 border border-brandPurple hover:border-glowGreen transition duration-200">
                            <div class="flex justify-between items-center">
                                <strong class="text-xs text-glowGreen font-mono">1. LEARNER® + INTELLECTION®</strong>
                                <span class="text-[9px] bg-glowGreen/10 text-glowGreen px-1.5 rounded uppercase font-mono">Phase 1</span>
                            </div>
                            <p class="text-[10.5px] text-purple-200 mt-1 leading-relaxed">
                                Audits 30-case charts and Form LARA logs systematically, treating complex compliance parameters as an intellectual journey.
                            </p>
                        </div>
                        <div class="p-2.5 rounded bg-brandPurple/10 border border-brandPurple hover:border-glowGreen transition duration-200">
                            <div class="flex justify-between items-center">
                                <strong class="text-xs text-glowGreen font-mono">2. IDEATION® + INDIVIDUALIZATION®</strong>
                                <span class="text-[9px] bg-glowGreen/10 text-glowGreen px-1.5 rounded uppercase font-mono">Phase 2</span>
                            </div>
                            <p class="text-[10.5px] text-purple-200 mt-1 leading-relaxed">
                                Designs standardized NextGen templates & Dragon macros, tailoring digital workflows to each therapist's unique clinical style.
                            </p>
                        </div>
                        <div class="p-2.5 rounded bg-brandPurple/10 border border-brandPurple hover:border-glowGreen transition duration-200">
                            <div class="flex justify-between items-center">
                                <strong class="text-xs text-glowGreen font-mono">3. STRATEGIC®</strong>
                                <span class="text-[9px] bg-glowGreen/10 text-glowGreen px-1.5 rounded uppercase font-mono">Phase 3</span>
                            </div>
                            <p class="text-[10.5px] text-purple-200 mt-1 leading-relaxed">
                                Synthesizes claims denials & material kit costs into an executive-ready 12-month optimization roadmap.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- RIGHT AREA: WORKFLOW TRACKER & TASK EXECUTION (8 COLS) -->
            <div class="lg:col-span-8 space-y-6">
                
                <!-- STEP-WISE SEQUENTIAL WORKFLOW TRACKER -->
                <div class="bg-black/40 p-4 rounded-xl border border-brandPurple">
                    <h3 class="text-sm font-bold text-purple-200 tracking-wider font-mono border-b border-brandPurple pb-2 mb-3">⚙️ INTERACTIVE STEP-WISE WORKFLOW TRACKER</h3>
                    
                    <!-- Chronological Horizontal Timeline -->
                    <div class="flex gap-2 overflow-x-auto py-2 px-1 mb-4" id="timeline-workflow-list">
                        <!-- Populated by JS -->
                    </div>

                    <!-- Task Execution Panel -->
                    <div class="bg-brandPurple/10 border border-brandPurple/60 rounded-xl p-5" id="execution-panel">
                        <div class="flex flex-col sm:flex-row justify-between items-start gap-2 border-b border-brandPurple pb-3 mb-3">
                            <div>
                                <span id="exec-phase" class="text-[10px] font-mono text-purple-300 uppercase tracking-widest block">Phase & Operational Pillar</span>
                                <h4 id="exec-title" class="text-lg font-bold text-white mt-1">Select a task above to execute</h4>
                            </div>
                            <div id="exec-policy-badges">
                                <!-- Populated dynamically -->
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                            <div class="space-y-3">
                                <p class="text-slate-300"><strong class="text-glowGreen font-mono block uppercase text-[10px] mb-1">Detailed Description</strong> <span id="exec-desc">Click any circle node above to load the detailed workflow step.</span></p>
                                <p class="text-slate-300"><strong class="text-glowGreen font-mono block uppercase text-[10px] mb-1">Target KPI Metric</strong> <span id="exec-kpi" class="font-mono bg-black/40 px-2 py-1 rounded border border-brandPurple inline-block text-purple-200">-</span></p>
                            </div>
                            <div class="space-y-3">
                                <p class="text-slate-300"><strong class="text-glowGreen font-mono block uppercase text-[10px] mb-1">Systemic Appraisal Rationale</strong> <span id="exec-rationale">-</span></p>
                                <div id="exec-remediation-card" class="hidden bg-amber-500/10 border border-amber-500/40 p-3 rounded-lg text-amber-200 text-xs">
                                    <strong class="font-mono block uppercase text-[10px] text-amber-400 mb-1">🛠️ Corrective Remediation directive</strong>
                                    <span id="exec-remediation">Click any circle node above to load.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- LIVE SEARCHABLE COMPLIANCE ENGINE TABLE -->
                <div class="bg-black/40 p-4 rounded-xl border border-brandPurple">
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-brandPurple pb-2 mb-3">
                        <h3 class="text-sm font-bold text-purple-200 tracking-wider font-mono">🗃️ LIVE SEARCHABLE AUDIT STATUS & COMPLIANCE BUILDER</h3>
                        <div class="w-full sm:w-64">
                            <input type="text" id="search-input" onkeyup="filterSearchTable()" placeholder="🔍 Search nodes, policies, or pillars..." class="w-full bg-darkPurple border border-brandPurple text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-glowGreen font-mono">
                        </div>
                    </div>

                    <div class="overflow-x-auto max-h-[350px] overflow-y-auto">
                        <table class="w-full text-xs text-left text-slate-300">
                            <thead class="text-[10px] font-mono uppercase tracking-wider text-purple-300 border-b border-brandPurple/60 bg-black/20">
                                <tr>
                                    <th class="p-3">ID</th>
                                    <th class="p-3">Audit Domain / Task</th>
                                    <th class="p-3">Phase & Operational Pillar</th>
                                    <th class="p-3">Governing Policy</th>
                                    <th class="p-3">Target KPI</th>
                                    <th class="p-3 text-center">Audit Status</th>
                                </tr>
                            </thead>
                            <tbody id="audit-table-body" class="divide-y divide-brandPurple/20">
                                <!-- Populated dynamically by JS -->
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </section>

        <!-- PROGRESS & EXECUTIVE FINDINGS REPORT (TAB 4 PRE-RENDERED VIEW) -->
        <section id="executive-report-view" class="hidden bg-black/40 p-6 rounded-xl border border-brandPurple space-y-6">
            <div class="text-center border-2 border-glowGreen/40 p-5 rounded-2xl bg-darkPurple/90 max-w-3xl mx-auto shadow-xl shadow-glowGreen/5">
                <h2 class="text-xl font-black font-mono tracking-widest text-white text-shadow shadow-glowGreen/30">MICHIGAN CCBHC PSYCHOLOGICAL SERVICES</h2>
                <h3 class="text-sm font-bold font-mono tracking-wider text-glowGreen mt-1 uppercase">EXECUTIVE STATUS APPRAISAL MEMORANDUM</h3>
                <p class="text-[10px] text-slate-400 font-mono mt-3 leading-relaxed">
                    Prepared for: CNS Healthcare Clinical Supervisors & Executive Leadership<br>
                    Lead Auditor: Dr. Scott Niewinski, Psy.D., Program Manager of Psychological Services<br>
                    Audit Target: 19 Regulatory Audit Domains across Wayne, Oakland, and Macomb Counties
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-6xl mx-auto">
                
                <!-- VERIFIED COMPLIANT SYSTEMS -->
                <div class="bg-black/30 p-5 rounded-xl border border-glowGreen/30 shadow-lg shadow-glowGreen/5">
                    <h3 class="text-base font-bold text-glowGreen border-b border-glowGreen/40 pb-2 mb-4 font-mono flex items-center gap-2">🟢 VERIFIED STRENGTHS & COMPLIANT SYSTEMS</h3>
                    <div id="report-compliant-list" class="space-y-4 max-h-[500px] overflow-y-auto pr-2">
                        <!-- Populated dynamically -->
                    </div>
                </div>

                <!-- CRITICAL VULNERABILITIES MATRIX -->
                <div class="bg-black/30 p-5 rounded-xl border border-rose-500/30 shadow-lg shadow-rose-500/5">
                    <h3 class="text-base font-bold text-rose-400 border-b border-rose-500/40 pb-2 mb-4 font-mono flex items-center gap-2">🔴 CRITICAL VULNERABILITIES & RISK REMEDIATION MATRIX</h3>
                    <div id="report-noncompliant-list" class="space-y-4 max-h-[500px] overflow-y-auto pr-2">
                        <!-- Populated dynamically -->
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- FOOTER STATEMENT -->
    <footer class="border-t border-brandPurple bg-black/40 px-6 py-4 text-center text-[10px] font-mono text-purple-300">
        CNS Healthcare Psychological Services Compliance Engine • Sourced Strictly from "90-Day Psychological Services Appraisal Plan.docx" • MDHHS CCBHC Demonstration Handbook v3.1 Compliant.
    </footer>

    <!-- ==============================================================================
         SPA INTERACTIVE DATA CONTROLLER
         ============================================================================== -->
    <script>
        // 19 Complete Grounded Audit Domains / Tasks
        const appraisalData = [
            {
                id: "p1_t1",
                phase: "Phase 1",
                pillar: "Pillar 1: Referral & Access Pipeline",
                label: "Intake Screening Integration (MichiCANS / LOCUS)",
                policy: "MDHHS Standardized Assessment Policies",
                policyLong: "Michigan Mental Health Framework (April 2026): Mandates Qualified Professionals to utilize State-designated level-of-care tools (MichiCANS for youth, LOCUS for adults).",
                target: "100% integration at intake",
                desc: "Check and verify if the intake triage workflow incorporates standard ratings (MichiCANS Screener and LOCUS 20 scores) during the initial contact.",
                rationale: "Failing to integrate initial screeners results in highly trained psychologists conducting routine diagnostic assessments, inflating testing waitlists.",
                remediation: "Require all intake personnel to undergo state-certified MichiCANS/LOCUS training and honor existing scores loaded in CareConnect360 to bypass duplicate screenings.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p1_t2",
                phase: "Phase 1",
                pillar: "Pillar 1: Referral & Access Pipeline",
                label: "Triage & Clinical Acuity Criteria Setup",
                policy: "CCBHC Demonstration Handbook Standard 8.B.9",
                policyLong: "SAMHSA 2023 Criteria: Requires established criteria to prioritize high-acuity cases.",
                target: "Established written priority algorithm",
                desc: "Map the clinical algorithms utilized to identify and fast-track urgent diagnostic referrals.",
                rationale: "Failing to prioritize high-risk enrollees (e.g. psychiatric step-downs or placement failures) risks client hospitalization, violating CCBHC contractual crisis agreements.",
                remediation: "Hardcode a tiered priority algorithm in NextGen that flags high-risk referrals with automatic scheduling indicators.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p1_t3",
                phase: "Phase 1",
                pillar: "Pillar 1: Referral & Access Pipeline",
                label: "Referral Source Mapping (County Analysis)",
                policy: "CCBHC Program Area Requirement #1",
                policyLong: "CCBHC Community Needs Assessment: Demands tracking caseload demographics and referral lines across county catchments.",
                target: "Mapping of 3-county referral pathways",
                desc: "Analyze and map referral volume and diagnostic quality across Oakland, Macomb, and Wayne clinics.",
                rationale: "Inappropriate or incomplete internal psychiatric/therapist referrals overload psychologists with administrative screening tasks.",
                remediation: "Deploy brief clinical referrals guidelines for referring prescribers, mandating preliminary diagnostic justifications.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p1_t4",
                phase: "Phase 1",
                pillar: "Pillar 1: Referral & Access Pipeline",
                label: "Waitlist Tracking & Access Velocity",
                policy: "SAMHSA 2023 CCBHC Criteria Program Requirement #2",
                policyLong: "SAMHSA Timeliness Criteria: Requires face-to-face service delivery initiation within 14 calendar days for routine referrals and 1 business day for urgent needs.",
                target: "Mean waitlist duration tracked in EHR",
                desc: "Perform a chronological audit of referrals from initial contact to the first face-to-face testing appointment.",
                rationale: "Chronically delayed access times trigger state-issued Corrective Action Plans (CAPs) and jeopardize CCBHC Prospective Payment System (PPS) funding.",
                remediation: "Establish daily scheduling blocks reserved exclusively for initial intakes and quick cognitive screenings.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p1_t5",
                phase: "Phase 1",
                pillar: "Pillar 2: Clinical Battery & Evidence-Based Tools",
                label: "Scope of Diagnostic Batteries Audit",
                policy: "APA Ethical Principles Standard 9.08",
                policyLong: "APA Ethics Code: Prohibits the use of obsolete assessments and outdated test results.",
                target: "Zero obsolete instruments utilized",
                desc: "Review clinical batteries to ensure modern versions of psychometric indices (WAIS-IV, WISC-V, MMPI-3, ADOS-2) are fully deployed.",
                rationale: "Utilizing obsolete testing scales yields invalid clinical formulations and invalidates Medicaid medical necessity justifications.",
                remediation: "Purchase updated psychometric kits and scoring software modules, immediately removing outdated booklets from clinic storage.",
                riskCategory: "Licensure & LARA",
                status: "Compliant"
            },
            {
                id: "p1_t6",
                phase: "Phase 1",
                pillar: "Pillar 2: Clinical Battery & Evidence-Based Tools",
                label: "Cultural & Linguistic Equity Evaluation",
                policy: "SAMHSA Certification Standard 1.b.8",
                policyLong: "SAMHSA Culturally and Linguistically Appropriate Services (CLAS): Demands availability of translation, auxiliary aids, and culturally normalized testing norms.",
                target: "Availability of translated psychometrics checked",
                desc: "Inventory the clinic's culturally responsive test norm groups and translated test booklets for diverse populations.",
                rationale: "Administering non-normed English batteries to non-native speakers introduces diagnostic bias, violating CCBHC health equity rules.",
                remediation: "Purchase Spanish-normed cognitive indices (WISC-V Spanish) and translate standard intake feedback materials into common regional languages.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p1_t7",
                phase: "Phase 1",
                pillar: "Pillar 3: Staffing, Supervision & EHR Workflow",
                label: "Verify LLP Supervision Logs (LARA Compliance)",
                policy: "Michigan Public Health Code MCL 333.18223",
                policyLong: "LARA Rule 338.2569: Requires Limited License Psychologists (LLPs) to receive a minimum of 4 hours/month face-to-face individual supervision from a fully Licensed Psychologist (LP) on Form LARA/BPL Rev. 6/25.",
                target: "100% compliant and signed logs",
                desc: "Examine supervision logs and check that official Psychology Supervision Evaluation logs are signed and uploaded for all active LLPs.",
                rationale: "Failing to document LARA-compliant supervision hours or missing signatures exposes the clinic to retroactive Medicaid recoupments and license suspensions.",
                remediation: "Immediately halt billing for any LLP missing logged hours. Move all logs to a centralized HR tracking database and set up EHR validation locks.",
                riskCategory: "Licensure & LARA",
                status: "Outside of Compliance"
            },
            {
                id: "p1_t8",
                phase: "Phase 1",
                pillar: "Pillar 3: Staffing, Supervision & EHR Workflow",
                label: "Workforce Capacity & LP-to-LLP Staffing Ratios",
                policy: "Michigan Board of Psychology Rules",
                policyLong: "LARA Supervisory Scope: Regulates the maximum number of supervisees (LLPs and interns) a fully licensed psychologist can supervise.",
                target: "Audit supervisor ratio compliance",
                desc: "Calculate FTE ratios between LPs and LLPs across all CNS service locations.",
                rationale: "An inverted supervisor ratio leads to delays in report sign-offs and compromises clinical supervision quality.",
                remediation: "Recruit additional fully licensed psychologists or adjust caseload assignments to cap supervisor loads.",
                riskCategory: "Licensure & LARA",
                status: "Compliant"
            },
            {
                id: "p2_t1",
                phase: "Phase 2",
                pillar: "Pillar 2: Clinical Battery & Evidence-Based Tools",
                label: "Digital vs. Analog Inventory (Cost Analysis)",
                policy: "CCBHC Payment Operations Standard 5.B",
                policyLong: "CCBHC Cost Allocation: Demands evaluating material expenditures against allowable Prospective Payment System billing rates.",
                target: "Cost-benefit analysis of Q-interactive completed",
                desc: "Evaluate the financial overhead of digital scoring licenses (Pearson Q-interactive, PARiConnect) versus traditional paper stimulus protocols.",
                rationale: "Unmonitored testing overhead costs decrease clinical margin under flat daily CCBHC daily payment structures.",
                remediation: "Migrate completely to Pearson Q-interactive digital administrations, which reduce clinical administration time by up to 40% and eliminate paper kit fees.",
                riskCategory: "Utilization Management",
                status: "Compliant"
            },
            {
                id: "p2_t2",
                phase: "Phase 2",
                pillar: "Pillar 2: Clinical Battery & Evidence-Based Tools",
                label: "Report Standardization & actionable PCP Metrics",
                policy: "CARF Quality Timeliness & ASPIRE Framework",
                policyLong: "CARF Behavioral Health Standards: Demands clinical reports maintain standard structural elements and actionable recommendations.",
                target: "100% standardized report format deployment",
                desc: "Audit completed diagnostic reports to ensure they contain clear, actionable, interdisciplinary recommendations.",
                rationale: "Reports loaded with medical jargon that do not directly translate into Treatment Plans act as isolated administrative exercises.",
                remediation: "Standardize all report templates in NextGen to mandate a summary block of actionable interdisciplinary recommendations.",
                riskCategory: "Coding Specificity",
                status: "Compliant"
            },
            {
                id: "p2_t3",
                phase: "Phase 2",
                pillar: "Pillar 3: Staffing, Supervision & EHR Workflow",
                label: "NextGen EHR Assessment Template Optimization",
                policy: "CCBHC Health Information Technology (HIT) criteria 8.C.7",
                policyLong: "ONC Certified HIT Standards: Demands that EHR systems capture structured demographic and clinical information.",
                target: "EHR templates optimized with custom macros",
                desc: "Analyze EHR charting flows and scoring entry processes to isolate bottlenecks.",
                rationale: "Cumbersome EHR workflows inflate the non-billable administrative burden on psychologists, directly reducing weekly testing volume.",
                remediation: "Configure custom smart-phrases and structured clinical template drop-downs inside NextGen to reduce manual typing.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p2_t4",
                phase: "Phase 2",
                pillar: "Pillar 3: Staffing, Supervision & EHR Workflow",
                label: "Turnaround Time (TAT) Metrics & Auditing",
                policy: "CARF Quality Timelines & SAMHSA Coordination",
                policyLong: "CARF Standards: Requires tracking and minimizing the days from testing administration to the signed and uploaded clinical record.",
                target: "Average TAT reduced below 14 calendar days",
                desc: "Extract EHR timestamps to measure the median turnaround days across clinical cohorts.",
                rationale: "Delayed report delivery delays treatment entry, violating the core CCBHC mandate of rapid, integrated care.",
                remediation: "Provide weekly dashboard notifications to clinicians when draft reports exceed the 10-day limit, and offer structured writing blocks.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            },
            {
                id: "p2_t5",
                phase: "Phase 2",
                pillar: "Pillar 4: Financial Mechanics & Revenue Cycle",
                label: "CPT Code Utilization Audit (96130–96139)",
                policy: "CPT Manual Definitions & CMS Guidelines",
                policyLong: "CMS Billing Rules: Dictates correct segregation of time-based evaluation (96130) and administration codes by providers (96136) and technicians (96138).",
                target: "100% compliant billing codes across audits",
                desc: "Audit claims to verify that clinician-reported code units match documented service hours.",
                rationale: "Misapplying provider administration codes (96136) for technician-led testing (96138) constitutes a severe compliance risk.",
                remediation: "Conduct mandatory CPT coding workshops for clinical and billing teams, implementing automatic EHR billing limits.",
                riskCategory: "Revenue Cycle (NCCI)",
                status: "Outside of Compliance"
            },
            {
                id: "p2_t6",
                phase: "Phase 2",
                pillar: "Pillar 4: Financial Mechanics & Revenue Cycle",
                label: "Modifier 59 / XE Same-Day Billing Audit",
                policy: "CMS National Correct Coding Initiative (NCCI) Edits",
                policyLong: "CMS NCCI Modifier Edits: Prohibits same-day psychologist test administration (96136) and technician administration (96138) without distinguishing modifiers.",
                target: "100% billing modifier accuracy",
                desc: "Extract 12-month claims data to check for appropriate application of Modifier XE or 59.",
                rationale: "Same-day provider and technician claims billed without XE/59 are immediately rejected by clearinghouses, resulting in severe revenue blockages.",
                remediation: "Hardcode NCCI validation rules within the EHR's billing module to automatically append Modifier XE/59.",
                riskCategory: "Revenue Cycle (NCCI)",
                status: "Outside of Compliance"
            },
            {
                id: "p2_t7",
                phase: "Phase 2",
                pillar: "Pillar 4: Financial Mechanics & Revenue Cycle",
                label: "Telehealth Modifier Compliance Check",
                policy: "MDHHS Telehealth Policy",
                policyLong: "Michigan Medicaid Provider Manual: Requires virtual psychological services to append specific Modifiers (95 or GT) and Place of Service codes (POS 02 or 10).",
                target: "100% telehealth modifier compliance",
                desc: "Review virtual CPT 96130 feedback sessions to ensure modifiers 95/GT are correctly appended in CHAMPS.",
                rationale: "Missing virtual indicators or incorrect POS codes cause immediate claim rejections by Medicaid Health Plans and commercial payers.",
                remediation: "Configure the EHR telehealth video module to auto-generate and attach the correct virtual POS and 95 modifier.",
                riskCategory: "Telehealth Regulations",
                status: "Outside of Compliance"
            },
            {
                id: "p2_t8",
                phase: "Phase 2",
                pillar: "Pillar 4: Financial Mechanics & Revenue Cycle",
                label: "Prior Authorization Limit Tracking",
                policy: "Michigan Medicaid Provider Manual",
                policyLong: "Medicaid Prior Authorization: Regulates annual testing limits (e.g. Meridian's 8-hour yearly threshold before PA is required).",
                target: "Centralized prior authorization tracking pathway",
                desc: "Assess how effectively the clinic tracks different PIHP prior authorization rules.",
                rationale: "Exceeding untracked MCO testing thresholds without a prior authorization results in complete forfeiture of reimbursement.",
                remediation: "Implement a hard stop in the EHR scheduling system that blocks appointments exceeding 8 hours unless an active PA is attached.",
                riskCategory: "Utilization Management",
                status: "Outside of Compliance"
            },
            {
                id: "p2_t9",
                phase: "Phase 2",
                pillar: "Pillar 4: Financial Mechanics & Revenue Cycle",
                label: "PPS Encounter Alignment & scheduling Strategy",
                policy: "CCBHC Prospective Payment System Standard 5.A",
                policyLong: "Michigan CCBHC Demonstration (PPS-1): Clinics receive a flat, daily, clinic-specific rate for providing eligible behavioral health services.",
                target: "Strategic scheduling models deployed",
                desc: "Evaluate strategies for distributing multi-day testing batteries to maximize legitimate encounter billing.",
                rationale: "Long, multi-day, 10-hour testing batteries billed on a single calendar day yield zero extra revenue under daily PPS flat rates, wasting clinical FTE capacity.",
                remediation: "Re-structure lengthy clinical testing protocols to span multiple days to capture the maximum allowable daily PPS encounters.",
                riskCategory: "Utilization Management",
                status: "Compliant"
            },
            {
                id: "p3_t1",
                phase: "Phase 3",
                pillar: "Pillar 5: Interdisciplinary Integration",
                label: "Interactive Feedback Loop Audit (CPT 96130)",
                policy: "CPT 96130 Interactive Feedback Mandate",
                policyLong: "AMA CPT Coding Rules: Delineates that billing the first hour of evaluation services (96130) requires documented clinical feedback with the patient.",
                target: "100% presence of feedback records in checked charts",
                desc: "Audit the clinical records to verify that billing for 96130 includes explicit documentation of interactive feedback.",
                rationale: "Systematically billing 96130 without documenting the clinical feedback session represents a compliance and billing audit infraction.",
                remediation: "Deploy structured EHR templates that physically block note-locking until a timestamped clinical feedback section is filled.",
                riskCategory: "Coding Specificity",
                status: "Compliant"
            },
            {
                id: "p3_t2",
                phase: "Phase 3",
                pillar: "Pillar 5: Interdisciplinary Integration",
                label: "Person-Centered Plan (PCP) Care Integration",
                policy: "MDHHS & SAMHSA Care Coordination Criteria 8.C.9",
                policyLong: "CCBHC Person-Centered Care Standards: Requires incorporating all psychiatric evaluations and clinical recommendations into the overarching Individualized Plan of Service (IPOS).",
                target: "100% integration rate from charts checked",
                desc: "Track the frequency with which completed testing recommendations are actively written into the client's IPOS.",
                rationale: "If diagnostic recommendations do not influence the IPOS, the testing operates as an isolated, low-impact administrative exercise.",
                remediation: "Implement automated notifications from the psychology EHR queue that flag recommendations directly to the assigned case manager.",
                riskCategory: "CCBHC Compliance",
                status: "Compliant"
            }
        ];

        // Global states to persist filter settings
        let activePhaseFilter = "all";

        // Navigation tab trigger
        function filterPhase(phase) {
            activePhaseFilter = phase;
            
            // Toggle active state classes for navigation buttons
            const buttons = document.querySelectorAll(".phase-btn");
            buttons.forEach(btn => {
                btn.classList.remove("bg-glowGreen", "text-darkPurple", "border-glowGreen");
                btn.classList.add("bg-brandPurple/20", "text-purple-200", "border-brandPurple");
            });
            
            const mapping = {
                'all': 'btn-phase-all',
                'Phase 1': 'btn-phase-p1',
                'Phase 2': 'btn-phase-p2',
                'Phase 3': 'btn-phase-p3',
                'Report': 'btn-phase-report'
            };
            document.getElementById(mapping[phase]).classList.add("bg-glowGreen", "text-darkPurple", "border-glowGreen");
            document.getElementById(mapping[phase]).classList.remove("bg-brandPurple/20", "text-purple-200", "border-brandPurple");

            // Toggle dashboard columns vs executive report
            if (phase === "Report") {
                document.getElementById("dashboard-main-view").classList.add("hidden");
                document.getElementById("executive-report-view").classList.remove("hidden");
                renderExecutiveReport();
            } else {
                document.getElementById("dashboard-main-view").classList.remove("hidden");
                document.getElementById("executive-report-view").classList.add("hidden");
                renderTimeline();
                renderTable();
            }
        }

        // Render Chronological Timeline for Interactive Step Tracker
        function renderTimeline() {
            const timelineContainer = document.getElementById("timeline-workflow-list");
            timelineContainer.innerHTML = "";

            const filteredData = activePhaseFilter === "all" ? 
                appraisalData : 
                appraisalData.filter(item => item.phase === activePhaseFilter);

            filteredData.forEach((task, idx) => {
                const isCompliant = task.status === "Compliant";
                const isNonCompliant = task.status === "Outside of Compliance";
                
                let colorClass = "border-slate-600 bg-slate-800 text-slate-400";
                if (isCompliant) colorClass = "border-glowGreen bg-glowGreen/10 text-glowGreen";
                if (isNonCompliant) colorClass = "border-rose-500 bg-rose-500/10 text-rose-400";

                const stepEl = document.createElement("div");
                stepEl.className = `flex-shrink-0 flex items-center gap-2 border px-3 py-1.5 rounded-full cursor-pointer transition ${colorClass} text-xs font-mono`;
                stepEl.onclick = () => selectExecutionTask(task.id);
                stepEl.innerHTML = `
                    <span class="w-5 h-5 rounded-full bg-black/35 flex items-center justify-center font-bold text-[10px]">${idx + 1}</span>
                    <span class="truncate max-w-[120px] font-sans">${task.label}</span>
                `;
                timelineContainer.appendChild(stepEl);
            });

            // Automatically select the first item on timeline load
            if (filteredData.length > 0) {
                selectExecutionTask(filteredData[0].id);
            } else {
                clearExecutionPanel();
            }
        }

        // Update task status from dropdown selection
        function updateTaskStatus(taskId, newStatus) {
            const task = appraisalData.find(item => item.id === taskId);
            if (task) {
                task.status = newStatus;
                updateGlobalMetrics();
                
                // If viewing report tab, re-render report immediately
                if (activePhaseFilter === "Report") {
                    renderExecutiveReport();
                } else {
                    renderTimeline();
                    // Keep active selection highlighted on execution panel
                    selectExecutionTask(taskId);
                }
            }
        }

        // Update Global Metric Indicators
        function updateGlobalMetrics() {
            const total = appraisalData.length;
            const compliant = appraisalData.filter(item => item.status === "Compliant").length;
            const noncompliant = appraisalData.filter(item => item.status === "Outside of Compliance").length;
            const pending = total - compliant - noncompliant;
            
            const compliancePct = (compliant / total) * 100;
            const revRealization = 100 - (noncompliant * 2.8); // simulated reduction multiplier

            document.getElementById("metric-compliance-pct").innerText = `${compliancePct.toFixed(1)}%`;
            document.getElementById("metric-compliance-bar").style.width = `${compliancePct}%`;
            document.getElementById("metric-gap-count").innerText = noncompliant;
            document.getElementById("metric-revenue-realization").innerText = `${revRealization.toFixed(1)}%`;
        }

        // Display Selected Task inside the Execution Panel
        function selectExecutionTask(taskId) {
            const task = appraisalData.find(item => item.id === taskId);
            if (!task) return;

            document.getElementById("exec-phase").innerText = `${task.phase} • ${task.pillar}`;
            document.getElementById("exec-title").innerText = task.label;
            document.getElementById("exec-desc").innerText = task.desc;
            document.getElementById("exec-kpi").innerText = task.target;
            document.getElementById("exec-rationale").innerText = task.rationale;
            document.getElementById("exec-remediation").innerText = task.remediation;

            const badgeContainer = document.getElementById("exec-policy-badges");
            badgeContainer.innerHTML = `
                <span class="badge-policy block sm:inline-block">${task.policy}</span>
                <span class="badge-target mt-1 sm:mt-0 block sm:inline-block">STATUS: ${task.status}</span>
            `;

            // Display or hide remediation block
            const remedyCard = document.getElementById("exec-remediation-card");
            if (task.status === "Outside of Compliance") {
                remedyCard.classList.remove("hidden");
            } else {
                remedyCard.classList.add("hidden");
            }
        }

        function clearExecutionPanel() {
            document.getElementById("exec-phase").innerText = "Operational Node Diagnostics";
            document.getElementById("exec-title").innerText = "No tasks found matching filter settings.";
            document.getElementById("exec-desc").innerText = "Select another phase or reset your filter settings.";
            document.getElementById("exec-kpi").innerText = "-";
            document.getElementById("exec-rationale").innerText = "-";
            document.getElementById("exec-remediation-card").classList.add("hidden");
            document.getElementById("exec-policy-badges").innerHTML = "";
        }

        // Render Searchable Table of All Tasks
        function renderTable(filterData = appraisalData) {
            const tbody = document.getElementById("audit-table-body");
            tbody.innerHTML = "";

            filterData.forEach(task => {
                const tr = document.createElement("tr");
                tr.className = "hover:bg-brandPurple/10 transition font-sans";
                tr.id = `row-${task.id}`;

                let statusBadgeColor = "text-yellow-500 bg-yellow-500/10 border-yellow-500/30";
                if (task.status === "Compliant") statusBadgeColor = "text-glowGreen bg-glowGreen/10 border-glowGreen/30";
                if (task.status === "Outside of Compliance") statusBadgeColor = "text-rose-500 bg-rose-500/10 border-rose-500/30";

                tr.innerHTML = `
                    <td class="p-3 font-mono font-bold text-purple-300 border-r border-brandPurple/20">${task.id.toUpperCase()}</td>
                    <td class="p-3 font-semibold text-white">${task.label}</td>
                    <td class="p-3 font-mono text-xs text-purple-200">
                        <span class="block">${task.phase}</span>
                        <span class="block text-[10px] text-slate-400">${task.pillar}</span>
                    </td>
                    <td class="p-3">
                        <span class="badge-policy">${task.policy}</span>
                        <!-- Popover trigger inside table -->
                        <div class="inline-block relative">
                            <button onclick="toggleTablePopover('${task.id}')" class="text-[9px] text-glowGreen font-mono uppercase border border-glowGreen/30 px-1 rounded hover:bg-glowGreen/10">Read Rationale</button>
                            <div id="popover-${task.id}" class="hidden absolute z-50 bottom-full left-0 mb-2 w-64 bg-darkPurple border border-glowGreen/40 p-3 rounded-lg shadow-xl shadow-black/80 text-[10.5px] leading-relaxed">
                                <strong class="text-glowGreen block mb-1 font-mono uppercase tracking-widest border-b border-glowGreen/30">Systemic Appraisal Rationale</strong>
                                ${task.rationale}
                            </div>
                        </div>
                    </td>
                    <td class="p-3 font-mono text-[11px] text-slate-300">${task.target}</td>
                    <td class="p-3 text-center border-l border-brandPurple/20">
                        <select onchange="updateTaskStatus('${task.id}', this.value)" class="bg-darkPurple border border-brandPurple text-xs text-white px-2 py-1 rounded-md focus:outline-none focus:border-glowGreen font-mono">
                            <option value="Pending" ${task.status === "Pending" ? "selected" : ""}>Pending</option>
                            <option value="Compliant" ${task.status === "Compliant" ? "selected" : ""}>Compliant</option>
                            <option value="Outside of Compliance" ${task.status === "Outside of Compliance" ? "selected" : ""}>Outside of Compliance</option>
                        </select>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function toggleTablePopover(taskId) {
            const el = document.getElementById(`popover-${taskId}`);
            const allPopovers = document.querySelectorAll("[id^='popover-']");
            allPopovers.forEach(p => { if (p.id !== `popover-${taskId}`) p.classList.add("hidden"); });
            el.classList.toggle("hidden");
        }

        // Live Search Filter Function
        function filterSearchTable() {
            const query = document.getElementById("search-input").value.toLowerCase();
            const filtered = appraisalData.filter(item => 
                item.label.toLowerCase().includes(query) ||
                item.policy.toLowerCase().includes(query) ||
                item.pillar.toLowerCase().includes(query) ||
                item.phase.toLowerCase().includes(query)
            );
            renderTable(filtered);
        }

        // Risk Category Selector Filter Function
        function filterRiskTable() {
            const selectedVal = document.getElementById("risk-filter").value;
            if (selectedVal === "all") {
                renderTable(appraisalData);
            } else {
                const filtered = appraisalData.filter(item => item.riskCategory === selectedVal);
                renderTable(filtered);
            }
        }

        // Render the Dynamic Executive Report View (Tab 4)
        function renderExecutiveReport() {
            const compliantContainer = document.getElementById("report-compliant-list");
            const noncompliantContainer = document.getElementById("report-noncompliant-list");
            
            compliantContainer.innerHTML = "";
            noncompliantContainer.innerHTML = "";

            const compliantItems = appraisalData.filter(item => item.status === "Compliant");
            const noncompliantItems = appraisalData.filter(item => item.status === "Outside of Compliance");

            // Build Compliant items list
            if (compliantItems.length === 0) {
                compliantContainer.innerHTML = "<p class='text-xs text-slate-400 font-mono'>No systems are currently verified as compliant.</p>";
            } else {
                compliantItems.forEach(item => {
                    const block = document.createElement("div");
                    block.className = "p-3.5 rounded-lg bg-glowGreen/5 border border-glowGreen/30 text-xs font-sans";
                    block.innerHTML = `
                        <div class="flex justify-between items-center mb-1">
                            <strong class="text-white text-sm">${item.label}</strong>
                            <span class="text-[9px] bg-glowGreen/10 text-glowGreen px-2 py-0.5 rounded uppercase font-mono">${item.phase}</span>
                        </div>
                        <p class="text-slate-300 mt-1 leading-relaxed">
                            <strong>Governing Policy:</strong> ${item.policyLong}<br>
                            <strong>Target Benchmark:</strong> ${item.target}
                        </p>
                    `;
                    compliantContainer.appendChild(block);
                });
            }

            // Build Non-Compliant Gaps & Risk matrix blocks
            if (noncompliantItems.length === 0) {
                noncompliantContainer.innerHTML = "<div class='text-center p-6 bg-glowGreen/10 border border-glowGreen/40 rounded-xl text-glowGreen font-bold text-xs font-mono animate-bounce'>🎉 EXCELLENT WORK! CNS Clinical operations are 100% compliant with state and federal regulations.</div>";
            } else {
                noncompliantItems.forEach(item => {
                    const block = document.createElement("div");
                    block.className = "p-3.5 rounded-lg bg-rose-500/5 border border-rose-500/30 text-xs font-sans";
                    block.innerHTML = `
                        <div class="flex justify-between items-center mb-1">
                            <strong class="text-rose-300 text-sm">[GAP] ${item.label}</strong>
                            <span class="text-[9px] bg-rose-500/10 text-rose-400 px-2 py-0.5 rounded uppercase font-mono">${item.phase}</span>
                        </div>
                        <p class="text-slate-300 mt-1 leading-relaxed">
                            <strong>Governing Policy:</strong> ${item.policyLong}<br>
                            <strong>Vulnerability Rationale:</strong> ${item.rationale}<br>
                            <strong>Risk Category Classification:</strong> <span class="text-rose-400 font-mono uppercase">${item.riskCategory}</span>
                        </p>
                        <div class="remedy-alert-box mt-3">
                            <strong class="font-mono block uppercase text-[10px] text-amber-400 mb-1">🛠️ Corrective Remediation directive</strong>
                            ${item.remediation}
                        </div>
                    `;
                    noncompliantContainer.appendChild(block);
                });
            }
        }

        // On document load, initialize data structures and rendering pipelines
        window.addEventListener("DOMContentLoaded", () => {
            updateGlobalMetrics();
            renderTimeline();
            renderTable();

            // ==============================================================================
            // PLOTLY.JS: CORE CPT DENIAL DRIVERS DONUT CHART
            // Displays multi-line formatted legends and high-contrast color tones
            // ==============================================================================
            const plotlyData = [{
                values: [35, 25, 20, 20],
                labels: [
                    'Modifier XE/59<br>Same-Day Billing Rules',
                    'Telehealth Codes<br>GT/95 Modifiers',
                    'Utilization Caps<br>Prior Auth Limits',
                    'CPT 96130<br>Missing Feedback Record'
                ],
                type: 'pie',
                hole: .55,
                marker: {
                    colors: ['#4A154B', '#22c55e', '#a855f7', '#00f2fe']
                },
                textinfo: 'percent',
                hoverinfo: 'label+value',
                textfont: {
                    color: '#ffffff',
                    family: 'monospace',
                    size: 10
                }
            }];

            const plotlyLayout = {
                showlegend: false,
                margin: { l: 10, r: 10, t: 10, b: 10 },
                paper_bgcolor: 'rgba(0,0,0,0)',
                plot_bgcolor: 'rgba(0,0,0,0)'
            };

            Plotly.newPlot('plotly-donut-denials', plotlyData, plotlyLayout, {responsive: true, displayModeBar: false});

            // ==============================================================================
            // CHART.JS: BAR CHART GRAPHING AVERAGE CLINIC REPORT WRITE TIMES (TAT)
            // Displays automated multi-line labels and green gradient metrics
            // ==============================================================================
            const tatCtx = document.getElementById('chartjs-clinic-tat').getContext('2d');
            const tatChart = new Chart(tatCtx, {
                type: 'bar',
                data: {
                    labels: [
                        ['Wayne County', 'Detroit Clinic'], 
                        ['Oakland County', 'Southfield Clinic'], 
                        ['Oakland County', 'Novi Clinic'], 
                        ['Macomb County', 'Eastpointe Clinic']
                    ],
                    datasets: [{
                        label: 'Average Turnaround (Days)',
                        data: [28.4, 18.2, 12.5, 22.1],
                        backgroundColor: 'rgba(34, 197, 94, 0.45)',
                        borderColor: '#22c55e',
                        borderWidth: 1.5,
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: {
                                color: '#ffffff',
                                font: { size: 9, family: 'monospace' }
                            }
                        },
                        y: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: {
                                color: '#ffffff',
                                font: { size: 9, family: 'monospace' }
                            }
                        }
                    }
                }
            });

        });
    </script>
</body>
</html>
"""

# Render the Single-Page Application (SPA) in Streamlit using a full-width components frame
st.components.v1.html(html_spa_content, height=1700, scrolling=True)
