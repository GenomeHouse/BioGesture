"use client";

import { useState } from "react";

const sequence = "ATGCGTACGTTAGCGATCGATCGGCTAACGCTAGCTAGGCTTACGATCGATGCTAGCTAGCTA";
const navItems = ["Overview", "Sequences", "Analysis", "Experiments"];

const sequenceStats = [
  ["Length", "1,248 bp"],
  ["GC content", "48.7%"],
  ["Open reading frames", "7"],
];

export default function HomePage() {
  const [activeNav, setActiveNav] = useState("Overview");
  const [isCapturing, setIsCapturing] = useState(false);

  return (
    <main className="app-shell">
      <aside className="sidebar">
        <div className="brand-lockup">
          <div className="brand-mark">BG</div>
          <div><strong>BioGesture</strong><span>Research workspace</span></div>
        </div>
        <div className="project-switcher">
          <span className="project-dot" />
          <div><small>PROJECT</small><strong>Plant stress study</strong></div>
          <span className="chevron">⌄</span>
        </div>
        <nav aria-label="Primary navigation">
          <p className="nav-label">Workspace</p>
          {navItems.map((item, index) => (
            <button className={`nav-item ${activeNav === item ? "active" : ""}`} key={item} onClick={() => setActiveNav(item)} type="button">
              <span className="nav-icon">{["⌂", "▤", "◒", "◈"][index]}</span>{item}
              {item === "Sequences" && <span className="nav-count">12</span>}
            </button>
          ))}
          <p className="nav-label secondary-label">Manage</p>
          <button className="nav-item" type="button"><span className="nav-icon">⚙</span>Settings</button>
        </nav>
        <div className="sidebar-footer"><span className="avatar">AR</span><div><strong>Alex Rivera</strong><span>Researcher</span></div><span className="more">•••</span></div>
      </aside>

      <section className="main-content">
        <header className="topbar">
          <div><p className="breadcrumb">Plant stress study <span>/</span> {activeNav}</p><h1>Good morning, Alex</h1></div>
          <div className="top-actions"><button className="icon-button" type="button" aria-label="Search">⌕</button><button className="icon-button notification" type="button" aria-label="Notifications">♢</button><button className="help-button" type="button">? <span>Help center</span></button></div>
        </header>

        <div className="content-wrap">
          <div className="page-heading"><div><p className="eyebrow">{activeNav} · Updated just now</p><h2>Research overview</h2></div><button className="outline-button" type="button">＋ New analysis</button></div>

          <section className="summary-grid" aria-label="Research summary">
            <article className="summary-card primary-summary"><div className="card-heading"><div><p className="card-kicker">Active sequence</p><h3>Arabidopsis thaliana</h3></div><span className="live-tag"><i /> Live</span></div><p className="sequence-id">AT1G01010 · genomic fragment</p><div className="big-number">1,248 <span>bp</span></div><div className="sparkline" aria-label="Sequence composition trend"><span style={{ height: "34%" }} /><span style={{ height: "52%" }} /><span style={{ height: "40%" }} /><span style={{ height: "68%" }} /><span style={{ height: "55%" }} /><span style={{ height: "76%" }} /><span style={{ height: "48%" }} /><span style={{ height: "88%" }} /><span style={{ height: "62%" }} /><span style={{ height: "72%" }} /><span style={{ height: "94%" }} /><span style={{ height: "65%" }} /></div><div className="card-foot"><span>Last analyzed 4 min ago</span><button className="text-button" type="button">Open sequence →</button></div></article>
            <article className="summary-card"><div className="card-heading"><div><p className="card-kicker">Gesture stream</p><h3>Camera input</h3></div><span className={`connection-dot ${isCapturing ? "capturing" : ""}`} /></div><div className="camera-preview"><div className="scan-line" /><div className="hand-mark">⌁</div><span className="camera-label">{isCapturing ? "Listening for gesture" : "Ready to connect"}</span></div><button className={`capture-button ${isCapturing ? "active" : ""}`} onClick={() => setIsCapturing(!isCapturing)} type="button">{isCapturing ? "Stop capture" : "Start capture"}<span>{isCapturing ? "■" : "▶"}</span></button></article>
            <article className="summary-card"><div className="card-heading"><div><p className="card-kicker">Analysis health</p><h3>Model performance</h3></div><span className="health-badge">Healthy</span></div><div className="health-score"><strong>94.8%</strong><span>confidence</span></div><div className="progress-bar"><span /></div><div className="health-row"><span>Gesture classifier</span><b>Excellent</b></div><div className="health-row"><span>Last calibration</span><b>Today, 09:42</b></div></article>
          </section>

          <section className="lower-grid">
            <article className="panel sequence-panel"><div className="panel-header"><div><p className="card-kicker">Sequence workspace</p><h3>AT1G01010 · genomic fragment</h3></div><div className="panel-tools"><button className="tool-button active" type="button">Sequence</button><button className="tool-button" type="button">Annotations</button><button className="icon-button small" type="button" aria-label="More options">•••</button></div></div><div className="sequence-toolbar"><span>1 — 68</span><span className="legend"><i className="legend-a" /> A <i className="legend-t" /> T <i className="legend-g" /> G <i className="legend-c" /> C</span><button className="text-button" type="button">Show complement ↗</button></div><div className="sequence-view">{sequence.match(/.{1,10}/g)?.map((chunk, index) => <div className="sequence-row" key={`${chunk}-${index}`}><span className="row-number">{String(index * 10 + 1).padStart(3, "0")}</span><span>{chunk.split("").map((base, baseIndex) => <b className={`base base-${base}`} key={`${base}-${baseIndex}`}>{base}</b>)}</span></div>)}</div><div className="sequence-footer"><span><i className="selection-dot" /> Region selected · 68 bp</span><button className="outline-button compact" type="button">Run analysis</button></div></article>
            <div className="side-stack"><article className="panel"><div className="panel-header"><div><p className="card-kicker">Composition</p><h3>Base distribution</h3></div><button className="icon-button small" type="button" aria-label="Open composition details">↗</button></div><div className="composition"><div className="donut"><span>48.7%<small>GC content</small></span></div><div className="base-list"><div><i className="legend-a" /><span>Adenine</span><b>26.4%</b></div><div><i className="legend-t" /><span>Thymine</span><b>24.9%</b></div><div><i className="legend-g" /><span>Guanine</span><b>24.6%</b></div><div><i className="legend-c" /><span>Cytosine</span><b>24.1%</b></div></div></div></article><article className="panel activity-panel"><div className="panel-header"><div><p className="card-kicker">Recent activity</p><h3>Lab notes</h3></div><button className="text-button" type="button">View all</button></div><div className="activity"><span className="activity-icon orange">↗</span><div><strong>GC content analysis completed</strong><span>AT1G01010 · 4 minutes ago</span></div></div><div className="activity"><span className="activity-icon green">✦</span><div><strong>Sequence imported</strong><span>Arabidopsis reference set · 2 hours ago</span></div></div></article></div>
          </section>

          <div className="stats-strip">{sequenceStats.map(([label, value]) => <div key={label}><span>{label}</span><strong>{value}</strong></div>)}<div className="strip-action"><button className="text-button" type="button">View full report →</button></div></div>
        </div>
      </section>
    </main>
  );
}
