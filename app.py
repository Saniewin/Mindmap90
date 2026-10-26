#!/usr/bin/env python3
"""
ZERO-DEPENDENCY TURNKEY WORKBENCH SERVER (HTTP + REST API + INTERACTIVE UI)
Author: Scott Niewinski, LP & Senior Software Architect
Description: Laun
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
      <input type="range" id="sf0Input" min="0.00" max="1.00" step="0.01" value="0s_lines if line.strip()], ensure_ascii=Fal
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
