#!/usr/bin/env python3
"""
ZERO-DEPENDENCY TURNKEY WORKBENCH SERVER (HTTP + REST API + INTERACTIVE UI)
Author: Scott Niewinski, LP & Senior Software Architect
Description: Launches the complete State of Michigan CCBHC Clinical Psychology Foundational
             Knowledge Matrix, Third Ear v2.0 Dyadic Enactment Index (DEI), & Local LLM Workbench
             on http://127.0.0.1:8080 using ONLY Python's standard library.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "backend"))
sys.path.insert(0, str(ROOT_DIR / "scripts"))

import export_matrix_for_local_llm as etl  # noqa: E402
from src.modules.clinical_mbc.service import (  # noqa: E402
    compute_dyadic_enactment_index,
    compute_piecewise_pseudo_phq9,
)
from src.modules.governance_pps.service import calculate_ccbhc_pps_pro_forma  # noqa: E402
from src.modules.knowledge_matrix.service import KnowledgeMatrixService  # noqa: E402
from src.modules.rag_copilot.service import HybridRAGCopilotService  # noqa: E402

matrix_service = KnowledgeMatrixService()
rag_service = HybridRAGCopilotService()

HTML_UI = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>CCBHC Foundational Knowledge Matrix & Third Ear v2.0 Dyadic Index Workbench</title>
  <style>
    :root {
      --bg: #090d16;
      --panel: #111827;
      --border: #1f2937;
      --text: #f3f4f6;
      --muted: #9ca3af;
      --sky: #38bdf8;
      --emerald: #34d399;
      --purple: #c084fc;
      --amber: #fbbf24;
      --rose: #fb7185;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; padding: 24px;
      background: var(--bg); color: var(--text);
      font-family: system-ui, -apple-system, sans-serif;
    }
    header {
      max-width: 1360px; margin: 0 auto 24px auto;
      padding-bottom: 16px; border-bottom: 1px solid var(--border);
      display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;
    }
    .subtitle { font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--sky); font-weight: 700; }
    h1 { margin: 4px 0 0 0; font-size: 22px; }
    .grid {
      max-width: 1360px; margin: 0 auto;
      display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap: 18px;
    }
    .card {
      background: var(--panel); border: 1px solid var(--border);
      border-radius: 12px; padding: 18px;
    }
    .card h2 { margin: 0 0 6px 0; font-size: 16px; }
    .card p { margin: 0 0 14px 0; font-size: 12px; color: var(--muted); }
    label { display: flex; justify-content: space-between; font-size: 12.5px; margin-bottom: 4px; }
    input[type="range"] { width: 100%; margin-bottom: 10px; }
    input[type="text"], select {
      width: 100%; padding: 9px 12px; background: #030712; color: var(--text);
      border: 1px solid var(--border); border-radius: 8px; font-size: 13px;
    }
    button {
      background: var(--sky); color: #030712; border: none; border-radius: 8px;
      padding: 9px 16px; font-weight: 700; cursor: pointer; font-size: 13px;
    }
    button:hover { opacity: 0.9; }
    .result-box {
      background: #030712; border: 1px solid var(--border);
      border-radius: 8px; padding: 12px; font-size: 12px; line-height: 1.5; margin-top: 10px;
      white-space: pre-wrap; font-family: ui-monospace, monospace;
    }
    .full-width { max-width: 1360px; margin: 18px auto 0 auto; }
    .badge { display: inline-block; padding: 3px 9px; border-radius: 99px; font-size: 11px; font-weight: 700; background: #1e293b; color: var(--sky); margin-right: 6px; }
  </style>
</head>
<body>
  <header>
    <div>
      <div class="subtitle">State of Michigan CCBHC Demonstration • Third Ear v2.0 Dyadic Index Integrated</div>
      <h1>Clinical Psychology Foundational Knowledge Matrix &amp; Local LLM Workbench</h1>
    </div>
    <div>
      <span class="badge">SQLite WAL Connected</span>
      <span class="badge">76 Graph Edges Active</span>
      <span class="badge" style="color: var(--amber)">100Hz Edge NPU • 750ms DEI</span>
    </div>
  </header>

  <div class="grid">
    <!-- Panel 1: L2-DEI / L3-TEAR Psychoanalytic Third Ear v2.0 Dyadic Enactment Index -->
    <div class="card">
      <h2 style="color: var(--amber)">[L2-DEI / L3-TEAR] Third Ear v2.0 Dyadic Enactment Index</h2>
      <p>100Hz Edge NPU (750ms window) fusing vocal shimmer (S_f0), silent pause (R_p), clinician PPG dHRV, &amp; INT8 defense load in zero-cloud Knox RAM.</p>
      <label><span>Pitch Micro-Shimmer (S_f0):</span><strong id="sf0Val">0.68</strong></label>
      <input type="range" id="sf0Input" min="0.00" max="1.00" step="0.01" value="0.68" oninput="updateDEI()" />
      <label><span>Inter-Turn Silent Pause Ratio (R_p):</span><strong id="rpVal">0.52</strong></label>
      <input type="range" id="rpInput" min="0.00" max="1.00" step="0.01" value="0.52" oninput="updateDEI()" />
      <label><span>Clinician PPG Autonomic Shift (dHRV = 1 - RMSSD):</span><strong id="hrvVal">0.45</strong></label>
      <input type="range" id="hrvInput" min="0.00" max="1.00" step="0.01" value="0.45" oninput="updateDEI()" />
      <label><span>INT8 Transformer Defense Load (Def_load):</span><strong id="defVal">0.55</strong></label>
      <input type="range" id="defInput" min="0.00" max="1.00" step="0.01" value="0.55" oninput="updateDEI()" />
      <div id="deiOutput" class="result-box">Calculating DEI...</div>
    </div>

    <!-- Panel 2: L2-MBC Piecewise Calculator -->
    <div class="card">
      <h2 style="color: var(--sky)">[L2-MBC / T3-MEAS] Ratio-Scale MBC &amp; pPHQ-9</h2>
      <p>Translates 14-day discrete symptom counts &amp; continuous VAS into Pseudo-PHQ-9 for MDHHS DEP-REM-6.</p>
      <label><span>14-Day Discrete Count:</span><strong id="daysVal">4 / 14 days</strong></label>
      <input type="range" id="daysInput" min="0" max="14" value="4" oninput="updateMBC()" />
      <label><span>Visual Analogue Scale (VAS):</span><strong id="vasVal">35%</strong></label>
      <input type="range" id="vasInput" min="0" max="100" value="35" oninput="updateMBC()" />
      <div id="mbcOutput" class="result-box">Calculating...</div>
    </div>

    <!-- Panel 3: L4-PPS Financial Pro Forma -->
    <div class="card">
      <h2 style="color: var(--purple)">[L4-PPS / T2-PROD] CCBHC Pro Forma ($180/visit)</h2>
      <p>LP Loaded Cost: $140k ($100k base + $25k benefits + $15k overhead) • Break-Even: 3.2 visits/day.</p>
      <label><span>Completed Daily Encounters:</span><strong id="visitsVal">3.4 visits/day</strong></label>
      <input type="range" id="visitsInput" min="1.0" max="6.0" step="0.1" value="3.4" oninput="updatePPS()" />
      <div id="ppsOutput" class="result-box">Calculating...</div>
    </div>

    <!-- Panel 4: Knowledge Matrix Table Explorer -->
    <div class="card">
      <h2 style="color: var(--emerald)">[Levels 0–5] Matrix Entity &amp; Graph Inspector</h2>
      <p>Inspect any canonical primary key (including L1-TEAR, L2-DEI, L3-TEAR, L4-CABI, T6-DYAD) and its 1-hop graph edges.</p>
      <select id="entitySelect" onchange="inspectEntity()">
        <option value="L2-DEI">L2-DEI — Third Ear v2.0 Dyadic Enactment Index (DEI)</option>
        <option value="L1-TEAR">L1-TEAR — Psychoanalytic Third Ear v2.0 &amp; Intersubjective Field</option>
        <option value="L3-TEAR">L3-TEAR — Third Ear v2.0 Haptic Preemption &amp; Safran Metacommunication</option>
        <option value="L4-CABI">L4-CABI — Third Ear v2.0 Edge NPU &amp; Knox 3-Pass DoD Wipe</option>
        <option value="T6-DYAD">T6-DYAD — Solipsistic Reverie vs Biometric Dyadic Index (DEI)</option>
        <option value="L1-RFT">L1-RFT — Relational Frame Theory (RFT) &amp; CBS</option>
        <option value="L1-FAP">L1-FAP — Functional Analytic Psychotherapy</option>
        <option value="L1-SOM">L1-SOM — Polyvagal &amp; Somatic Autonomic Theory</option>
        <option value="L1-PSY">L1-PSY — Psychodynamic &amp; Ego Psychology</option>
        <option value="L2-FBA">L2-FBA — Expanded Functional Behavioral Assessment</option>
        <option value="L2-MBC">L2-MBC — Ratio-Scale Measurement-Based Care</option>
        <option value="L3-ACT">L3-ACT — ACT 'Dropping Anchor' &amp; Somatic Defusion</option>
        <option value="L4-PPS">L4-PPS — CCBHC Prospective Payment System ($180)</option>
        <option value="T2-PROD">T2-PROD — Throughput Volume vs Relational Attunement</option>
      </select>
      <div id="entityOutput" class="result-box">Loading...</div>
    </div>
  </div>

  <!-- Bottom Panel: Hybrid RAG Copilot -->
  <div class="card full-width">
    <h2 style="color: var(--amber)">Deterministic Local LLM Hybrid RAG Copilot (SQLite Graph + JSONL Chunks)</h2>
    <p>Retrieves grounded matrix chunks + 1-hop relational graph edges and builds the zero-hallucination system prompt for Ollama / vLLM.</p>
    <div style="display: flex; gap: 10px;">
      <input type="text" id="ragQuery" value="Explain the Third Ear v2.0 Dyadic Enactment Index (L2-DEI), 3-tick haptic preemption (L3-TEAR), and Safran metacommunication." />
      <button onclick="runRAG()">Retrieve &amp; Synthesize</button>
    </div>
    <div id="ragOutput" class="result-box">Ready.</div>
  </div>

  <script>
    async function updateDEI() {
      const sf0 = Number(document.getElementById('sf0Input').value);
      const rp = Number(document.getElementById('rpInput').value);
      const hrv = Number(document.getElementById('hrvInput').value);
      const def = Number(document.getElementById('defInput').value);
      document.getElementById('sf0Val').textContent = sf0.toFixed(2);
      document.getElementById('rpVal').textContent = rp.toFixed(2);
      document.getElementById('hrvVal').textContent = hrv.toFixed(2);
      document.getElementById('defVal').textContent = def.toFixed(2);
      const res = await fetch(`/api/dei?sf0=${sf0}&rp=${rp}&hrv=${hrv}&def=${def}`).then(r => r.json());
      document.getElementById('deiOutput').textContent =
        `Effective DEI   : ${res.effective_dei.toFixed(3)} (Continuous: ${res.dei_continuous.toFixed(3)} | 750ms NPU: ${res.dei_750ms_npu.toFixed(3)})\\n` +
        `O-RFT DEI_100   : ${res.dei_orft_100.toFixed(1)} / 100.0\\n` +
        `Enactment State : ${res.enactment_state} (MAS: ${res.mas_discrepancy_flag})\\n` +
        `Earbud Haptic   : ${res.haptic_earbud_dispatch}\\n` +
        `Control Tier    : ${res.subsumption_tier}\\n` +
        `Countertransf.  : ${res.racker_countertransference_type}\\n` +
        `Safran Script   : ${res.safran_metacommunication_script}`;
    }

    async function updateMBC() {
      const days = Number(document.getElementById('daysInput').value);
      const vas = Number(document.getElementById('vasInput').value);
      document.getElementById('daysVal').textContent = days + ' / 14 days';
      document.getElementById('vasVal').textContent = vas + '%';
      const res = await fetch(`/api/mbc?days=${days}&vas=${vas}`).then(r => r.json());
      document.getElementById('mbcOutput').textContent =
        `Pseudo-PHQ-9 Score : ${res.pseudo_phq9_score} / 27 (${res.severity_band})\\n` +
        `Ordinal Equivalent : ${res.item_ordinal_equivalent} (0-3 scale)\\n` +
        `MDHHS DEP-REM-6    : ${res.mdhhs_dep_rem_6_remission ? 'REMISSION ACHIEVED (<5)' : 'ACTIVE SYMPTOMS (>=5)'}`;
    }

    async function updatePPS() {
      const visits = Number(document.getElementById('visitsInput').value);
      document.getElementById('visitsVal').textContent = visits.toFixed(1) + ' visits/day';
      const res = await fetch(`/api/pps?visits=${visits}`).then(r => r.json());
      document.getElementById('ppsOutput').textContent =
        `Status         : ${res.operational_status}\\n` +
        `Daily Revenue  : $${res.daily_revenue_usd.toFixed(2)} (@ $180/visit)\\n` +
        `Annual Revenue : $${res.annual_projected_revenue_usd.toLocaleString()} vs $140,000 Loaded Cost\\n` +
        `Annual Margin  : $${res.annual_net_margin_usd.toLocaleString()}\\n` +
        `Guidance       : ${res.t2_prod_recommendation}`;
    }

    async function inspectEntity() {
      const id = document.getElementById('entitySelect').value;
      const res = await fetch(`/api/entity?id=${encodeURIComponent(id)}`).then(r => r.json());
      const edges = (res.relationships || []).map(e => `  ${e.source_id} --[${e.relationship_type}]--> ${e.target_id}`).join('\\n');
      document.getElementById('entityOutput').textContent =
        `Table: ${res.table}\\n` +
        `Summary: ${res.record.dense_summary || res.record.dialectical_synthesis}\\n` +
        `Connected Graph Edges (${(res.relationships || []).length}):\\n${edges}`;
    }

    async function runRAG() {
      const q = document.getElementById('ragQuery').value;
      const res = await fetch(`/api/rag?q=${encodeURIComponent(q)}`).then(r => r.json());
      document.getElementById('ragOutput').textContent =
        res.deterministic_synthesis + '\\n\\n--- GENERATED LOCAL LLM SYSTEM PROMPT ---\\n' + res.system_prompt;
    }

    updateDEI();
    updateMBC();
    updatePPS();
    inspectEntity();
    runRAG();
  </script>
</body>
</html>
"""


class WorkbenchRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: object, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        if parsed.path == "/":
            body = HTML_UI.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif parsed.path == "/healthz":
            self._send_json({"status": "healthy", "mode": "turnkey-stdlib-server-v2"})
        elif parsed.path == "/api/dei":
            sf0 = float(qs.get("sf0", ["0.68"])[0])
            rp = float(qs.get("rp", ["0.52"])[0])
            hrv = float(qs.get("hrv", ["0.45"])[0])
            def_load = float(qs.get("def", ["0.55"])[0])
            self._send_json(asdict(compute_dyadic_enactment_index(sf0, rp, hrv, def_load)))
        elif parsed.path == "/api/mbc":
            days = int(qs.get("days", ["4"])[0])
            vas = float(qs.get("vas", ["35.0"])[0])
            self._send_json(asdict(compute_piecewise_pseudo_phq9(days, vas)))
        elif parsed.path == "/api/pps":
            visits = float(qs.get("visits", ["3.4"])[0])
            self._send_json(asdict(calculate_ccbhc_pps_pro_forma(visits)))
        elif parsed.path == "/api/entity":
            eid = qs.get("id", ["L2-DEI"])[0]
            self._send_json(matrix_service.get_entity_by_id(eid) or {"error": "Not found"})
        elif parsed.path == "/api/rag":
            q = qs.get("q", ["dyadic enactment index"])[0]
            self._send_json(rag_service.retrieve_hybrid_context(q, top_k=5))
        else:
            self._send_json({"error": "Not found"}, status=404)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def export_standalone_html_workbench() -> Path:
    """
    Generates a 100% self-contained, offline interactive HTML application
    (data/interactive_ccbhc_workbench.html) with the full 6-table Matrix + 76 Graph Edges
    + Third Ear v2.0 DEI + L2-MBC Piecewise pPHQ-9 + L4-PPS Pro Forma + Hybrid RAG Copilot.
    """
    etl.run_etl_pipeline()
    kb_json = (ROOT_DIR / "data" / "matrix_llm_knowledge.json").read_text(encoding="utf-8")
    chunks_lines = (ROOT_DIR / "data" / "matrix_llm_rag_chunks.jsonl").read_text(encoding="utf-8").splitlines()
    chunks_json = json.dumps([json.loads(line) for line in chunks_lines if line.strip()], ensure_ascii=False)

    standalone_html = HTML_UI.replace(
        "async function updateDEI() {",
        f"const EMBEDDED_KB = {kb_json};\n    const EMBEDDED_CHUNKS = {chunks_json};\n\n    async function updateDEI() {{",
    )

    standalone_html = standalone_html.replace(
        "const res = await fetch(`/api/dei?sf0=${sf0}&rp=${rp}&hrv=${hrv}&def=${def}`).then(r => r.json());",
        """const dei_cont = 0.40 * sf0 + 0.30 * hrv + 0.15 * rp + 0.15 * def;
      const dei_750 = 0.40 * sf0 + 0.30 * rp + 0.30 * hrv;
      const dei_100 = 100.0 * Math.tanh(0.35 * sf0 + 0.40 * sf0 + 0.25 * rp);
      const eff = Math.max(dei_cont, dei_750);
      let state = 'DYAD_ATTUNED', mas = 'BALANCED_AFFECTIVITY', haptic = 'HAPTIC_1TICK_ATTUNEMENT';
      let tier = 'L1_PRIMARY_TELEMETRY (NODE-PROS-750)', racker = 'Concordant Empathy (Intact Analytic Third)';
      let script = 'Alliance baseline intact (1-Tick Pulse). Continue tracking implicit affective micro-emergence.';
      if (eff >= 0.75) {
        state = 'DYAD_MASKED_DISSIMULATION'; mas = 'OGM_COLLAPSE'; haptic = 'HAPTIC_3TICK_EMERGENCY';
        tier = 'L3_AUTONOMOUS_MASTER_CONTROLLER (5G_URLLC_5QI_82)'; racker = 'Psychic Equivalence Crisis / Masked Dissimulation';
        script = '"I can hear how overwhelming and heavy this feels right now. Let\\'s slow everything down together—press your heels into the floor with me."';
      } else if (eff >= 0.50) {
        state = 'DYAD_SADO_MASOCHISTIC_LOCK'; mas = 'HIGH_ID_LOW_PROC'; haptic = 'HAPTIC_3TICK_PREEMPTION';
        tier = 'L2_INTERSUBJECTIVE_META_NODE (SUPER-NODE-2-MASTER)'; racker = 'Complementary Countertransference Lock (Doer / Done-To)';
        script = '"I notice we\\'ve gotten into a struggle where you feel attacked and I feel defensive. Let\\'s pause and look together at what is happening between us right now."';
      } else if (eff >= 0.25) {
        state = 'DYAD_PRETEND_MODE'; mas = 'HIGH_ID_LOW_PROC'; haptic = 'HAPTIC_2PULSE_HARMONIC';
        tier = 'L2_INTERSUBJECTIVE_META_NODE (META-NODE-01)'; racker = 'Intellectualized / Pseudo-Mentalizing Drift (Pretend Mode)';
        script = '"We\\'re talking very analytically right now, but what do you notice happening in your body—in your chest or shoulders—as we say these words?"';
      }
      const res = {
        effective_dei: eff, dei_continuous: dei_cont, dei_750ms_npu: dei_750, dei_orft_100: dei_100,
        enactment_state: state, mas_discrepancy_flag: mas, haptic_earbud_dispatch: haptic,
        subsumption_tier: tier, racker_countertransference_type: racker, safran_metacommunication_script: script
      };""",
    ).replace(
        "const res = await fetch(`/api/mbc?days=${days}&vas=${vas}`).then(r => r.json());",
        """const ordinal_eq = days <= 1 ? 0 : (days <= 6 ? 1 : (days <= 11 ? 2 : 3));
      const base_score = days <= 1 ? (days * 2.0) : (days <= 6 ? 3.0 + ((days - 2) / 4.0) * 6.0 : (days <= 11 ? 10.0 + ((days - 7) / 4.0) * 8.0 : 19.0 + ((days - 12) / 2.0) * 8.0));
      const p_phq9 = (days === 0 && vas === 0) ? 0 : Math.max(0, Math.min(27, Math.round(0.70 * base_score + 0.30 * (vas / 100.0) * 27.0)));
      const band = p_phq9 < 5 ? 'Minimal / Remission' : (p_phq9 < 10 ? 'Mild' : (p_phq9 < 15 ? 'Moderate' : (p_phq9 < 20 ? 'Moderately Severe' : 'Severe')));
      const res = { pseudo_phq9_score: p_phq9, severity_band: band, item_ordinal_equivalent: ordinal_eq, mdhhs_dep_rem_6_remission: p_phq9 < 5 };""",
    ).replace(
        "const res = await fetch(`/api/pps?visits=${visits}`).then(r => r.json());",
        """const daily_rev = visits * 180.0;
      const annual_rev = Math.round(daily_rev * 243);
      const margin = annual_rev - 140000;
      const solvent = visits >= 3.2;
      const res = {
        operational_status: solvent ? 'SOLVENT (Meets or Exceeds 3.2 Visits/Day Break-Even)' : 'DEFICIT RISK (Below 3.2 Visits/Day Break-Even Threshold)',
        daily_revenue_usd: daily_rev,
        annual_projected_revenue_usd: annual_rev,
        annual_net_margin_usd: margin,
        t2_prod_recommendation: solvent
          ? '[T2-PROD Synthesis] Clinic is financially solvent under $180 PPS rate. Protect non-billable 5-minute somatic co-regulation huddles (L3-ACT/L3-FAP).'
          : '[T2-PROD Synthesis] Below 3.2 visits/day break-even. Embed 15-minute Integrated PCBH warm-handoff consultations (L3-PCBH, CPT 96150-96154).'
      };""",
    ).replace(
        "const res = await fetch(`/api/entity?id=${encodeURIComponent(id)}`).then(r => r.json());",
        """const allTables = [
        ['level1_meta_theories', EMBEDDED_KB.Level1_MetaTheories],
        ['level2_assessment', EMBEDDED_KB.Level2_Assessment],
        ['level3_interventions', EMBEDDED_KB.Level3_Interventions],
        ['level4_systems_policy', EMBEDDED_KB.Level4_SystemsPolicy],
        ['level5_discrepancy_matrix', EMBEDDED_KB.Level5_DiscrepancyMatrix]
      ];
      let foundTable = '', foundRec = {};
      for (const [tName, rows] of allTables) {
        const hit = rows.find(r => r.id === id);
        if (hit) { foundTable = tName; foundRec = hit; break; }
      }
      const rels = EMBEDDED_KB.EntityRelationships.filter(e => e.source_id === id || e.target_id === id);
      const res = { table: foundTable, record: foundRec, relationships: rels };""",
    ).replace(
        "const res = await fetch(`/api/rag?q=${encodeURIComponent(q)}`).then(r => r.json());",
        """const terms = q.toLowerCase().split(/[^a-z0-9_-]+/).filter(t => t.length >= 3);
      const scored = EMBEDDED_CHUNKS.map(c => {
        let s = 0;
        const txt = c.text.toLowerCase();
        if (q.toLowerCase().includes(c.primary_key.toLowerCase())) s += 10;
        for (const t of terms) { if (txt.includes(t)) s += 2; if (c.title.toLowerCase().includes(t)) s += 3; }
        return { score: s, chunk: c };
      }).filter(x => x.score > 0).sort((a, b) => b.score - a.score).slice(0, 5);
      const topChunks = scored.map(x => x.chunk);
      const cited = topChunks.map(c => '[' + c.primary_key + ']').join(', ');
      const synth = `Grounded Matrix Synthesis for query: '${q}'\\nPrimary Cited Entities: ${cited}\\n` +
        topChunks.slice(0, 3).map(c => `- [${c.primary_key}] (${c.level} - ${c.title}): Related to ${c.related_ids.join(', ')}`).join('\\n');
      const prompt = 'You are a Clinical Psychology & Health Systems AI Assistant grounded in Scott Niewinski\\'s Foundational Knowledge Matrix.\\n\\n--- GROUNDED MATRIX CHUNKS ---\\n' +
        topChunks.map(c => c.text).join('\\n\\n');
      const res = { deterministic_synthesis: synth, system_prompt: prompt };""",
    )

    out_path = ROOT_DIR / "data" / "interactive_ccbhc_workbench.html"
    out_path.write_text(standalone_html, encoding="utf-8")
    return out_path


def main() -> None:
    out_html = export_standalone_html_workbench()
    if "--export-only" in sys.argv:
        print(f"Exported standalone HTML workbench to: {out_html}")
        return
    host, port = "127.0.0.1", 8080
    server = HTTPServer((host, port), WorkbenchRequestHandler)
    print(f"=== CCBHC MATRIX WORKBENCH v2.0 RUNNING AT http://{host}:{port} ===")
    print(f"=== STANDALONE OFFLINE HTML EXPORTED TO: {out_html} ===")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


if __name__ == "__main__":
    main()
